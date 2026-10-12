# ZFROG memes

Everything in here shows up on **https://zfrog.xyz/memes**.

## Add a meme

1. Open the right folder in `memes/` on GitHub.
2. **Add file → Upload files**, drop the image(s), **Commit changes**.
3. Wait about 2 minutes. The robot makes the thumbnail and the meme appears on the site, newest first.

Works from a phone too.

## The folders

| Folder | Shows as | What goes in |
|---|---|---|
| `memes/zama-news/` | Zama news | Ecosystem headlines, frog edition |
| `memes/privacy-mood/` | Privacy mood | Everyday life, encrypted |
| `memes/the-pond/` | The Pond | Community, Telegram, recruitment |

A **new folder becomes a new filter on the site** automatically (`memes/raid-kit/` → "Raid kit").

## Rules that keep it clean

- **Name the file after the meme**, e.g. `copy-traders-telepathy.jpg`. The name becomes the title on the site.
- One meme = one file. JPG, PNG, WebP or GIF. Square 1254px is the house format.
- To fix a title, add the meme text (it makes search work) or tags, edit `memes.json`. Your edits are never overwritten.
- To remove a meme, delete the file. The site drops it on the next build.
- To move a meme to another category, move the file to the other folder.

Never edit `thumbs/` or `og.jpg` by hand, the robot rebuilds them.

## What the robot does

`.github/workflows/build.yml` runs `scripts/build.py` on every change in `memes/`:
it adds new files to `memes.json`, makes 640px WebP thumbnails, removes deleted ones,
and redraws `og.jpg` (the preview card Telegram and X show for the link).
