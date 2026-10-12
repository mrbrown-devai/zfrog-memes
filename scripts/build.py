#!/usr/bin/env python3
"""Rebuild the ZFROG meme manifest.

Scans memes/<category>/<file>, then:
  - adds any new image to memes.json (title from the file name, dated today)
  - drops entries whose file was deleted
  - makes a 640px WebP thumbnail in thumbs/ for anything new or changed
  - creates a category for any new folder
  - redraws og.jpg (the preview Telegram/X show for zfrog.xyz/memes)

Existing titles, captions, tags and dates in memes.json are never overwritten,
so you can edit them by hand and they stick.

Run locally:  pip install pillow && python3 scripts/build.py
"""
import datetime as dt
import hashlib
import json
import os
import re
import sys

from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEMES = os.path.join(ROOT, "memes")
THUMBS = os.path.join(ROOT, "thumbs")
MANIFEST = os.path.join(ROOT, "memes.json")
OG = os.path.join(ROOT, "og.jpg")
EXTS = {".jpg", ".jpeg", ".png", ".webp", ".gif"}
THUMB_PX = 640


def slugify(s):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s or "meme"


def nice_title(stem):
    t = re.sub(r"[-_]+", " ", stem).strip()
    return t[:1].upper() + t[1:] if t else "Untitled"


def sha1(path):
    h = hashlib.sha1()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def load():
    if os.path.exists(MANIFEST):
        with open(MANIFEST, encoding="utf-8") as f:
            return json.load(f)
    return {"categories": [], "memes": []}


def make_thumb(src, dst):
    with Image.open(src) as im:
        im = ImageOps.exif_transpose(im)
        if getattr(im, "is_animated", False):
            im.seek(0)
        im = im.convert("RGB")
        w, h = im.size
        im.thumbnail((THUMB_PX, THUMB_PX * 2), Image.LANCZOS)
        im.save(dst, "WEBP", quality=78, method=6)
        return w, h


def make_og(memes):
    W, H, n = 1200, 630, 0
    canvas = Image.new("RGB", (W, H), (7, 7, 10))
    picks = memes[:8]
    if not picks:
        return
    cols, rows, gap = 4, 2, 6
    cw = (W - gap * (cols + 1)) // cols
    ch = (H - gap * (rows + 1)) // rows
    for i, m in enumerate(picks):
        p = os.path.join(THUMBS, m["id"] + ".webp")
        if not os.path.exists(p):
            continue
        with Image.open(p) as im:
            im = ImageOps.fit(im.convert("RGB"), (cw, ch), Image.LANCZOS, centering=(0.5, 0.35))
        x = gap + (i % cols) * (cw + gap)
        y = gap + (i // cols) * (ch + gap)
        canvas.paste(im, (x, y))
        n += 1
    if n:
        canvas.save(OG, "JPEG", quality=84, optimize=True, progressive=True)


def main():
    today = dt.date.today().isoformat()
    data = load()
    cats = {c["id"]: c for c in data.get("categories", [])}
    by_path = {m["file"]: m for m in data.get("memes", [])}
    used_ids = {m["id"] for m in data.get("memes", [])}
    os.makedirs(THUMBS, exist_ok=True)

    found, added, changed = [], [], []
    for cat in sorted(os.listdir(MEMES)):
        cdir = os.path.join(MEMES, cat)
        if not os.path.isdir(cdir) or cat.startswith("."):
            continue
        cid = slugify(cat)
        if cid not in cats:
            cats[cid] = {"id": cid, "label": nice_title(cat), "folder": cat}
        cats[cid].setdefault("folder", cat)
        for name in sorted(os.listdir(cdir)):
            stem, ext = os.path.splitext(name)
            if ext.lower() not in EXTS or name.startswith("."):
                continue
            rel = f"memes/{cat}/{name}"
            src = os.path.join(cdir, name)
            digest = sha1(src)
            m = by_path.get(rel)
            if m is None:
                base, i = slugify(stem), 2
                mid = base
                while mid in used_ids:
                    mid, i = f"{base}-{i}", i + 1
                used_ids.add(mid)
                m = {"id": mid, "file": rel, "category": cid, "title": nice_title(stem),
                     "caption": "", "tags": [], "added": today}
                added.append(rel)
            m["category"] = cid
            thumb = os.path.join(THUMBS, m["id"] + ".webp")
            if m.get("hash") != digest or not os.path.exists(thumb):
                w, h = make_thumb(src, thumb)
                m["w"], m["h"], m["hash"] = w, h, digest
                m["thumb"] = f"thumbs/{m['id']}.webp"
                if rel not in added:
                    changed.append(rel)
            found.append(m)

    live_ids = {m["id"] for m in found}
    for fn in os.listdir(THUMBS):
        if fn.endswith(".webp") and fn[:-5] not in live_ids:
            os.remove(os.path.join(THUMBS, fn))
    removed = [p for p in by_path if p not in {m["file"] for m in found}]

    order = {m["id"]: i for i, m in enumerate(data.get("memes", []))}
    found.sort(key=lambda m: (m["added"], -order.get(m["id"], -1)), reverse=True)
    used_cats = {m["category"] for m in found}
    cat_list = [c for c in cats.values() if c["id"] in used_cats]
    old_order = [c["id"] for c in data.get("categories", [])]
    cat_list.sort(key=lambda c: old_order.index(c["id"]) if c["id"] in old_order else 999)

    stamp = data.get("updated")
    if added or removed or changed or cat_list != data.get("categories") or not stamp:
        stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    out = {"updated": stamp, "categories": cat_list, "memes": found}
    with open(MANIFEST, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
        f.write("\n")
    if added or removed or not os.path.exists(OG):
        make_og(found)
    print(f"{len(found)} memes · +{len(added)} new · {len(changed)} updated · -{len(removed)} removed")
    for p in added:
        print("  + " + p)
    for p in removed:
        print("  - " + p)


if __name__ == "__main__":
    sys.exit(main())
