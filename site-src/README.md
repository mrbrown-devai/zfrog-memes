# zfrog.xyz site source

What's here builds every page of https://www.zfrog.xyz except the media (`/media/*`). The media files only live on Vercel, in the project `zfrog-vercel-1`, and a deploy references them by hash.

- `live/index.html` and `live/memes_orig.html`: the homepage and /memes before the SEO pass. `build.py` adds titles, canonicals, OG tags, JSON-LD and internal links on top of them.
- `pages/*.html`: the article pages (`/earn-zama`, `/fhe`, `/frog-mark-1`). The first line is JSON metadata (title, description, FAQ), the rest is the body HTML.
- `mkpages.py`: writes `pages/*.html`. Edit the copy there.
- `article.css`: becomes `/assets/site.css`.
- `llms.txt`: the facts file for AI answer engines.

Build: copy `../memes.json` next to `build.py`, set `SRC` in `build.py` to `live/` (it currently points to `../v2`), then run `python3 build.py`. The output goes to `out/`.
Deploy: Vercel project `zfrog-vercel-1` (team mrbrown-devais-projects), domain www.zfrog.xyz.
