# Discover Singapore

Landing page for discoversingapore.org, hosted on Cloudflare Pages.

## How it builds
- `index.html` is the site.
- `photos/` holds the original photos. `build.py` resizes them into `dist/assets/img/` (800 px and 1800 px versions). The `SLOTS` list in `build.py` says which photo goes where.
- Cloudflare Pages settings: build command `pip install pillow && python3 build.py`, build output directory `dist`.

## Book covers
Add the final covers to `photos/` as `cover-guide.jpg` and `cover-nomad.jpg` (or .png). Until then the build makes a simple placeholder cover for each book.

## Sign-up form
Set `data-endpoint` on `<form id="signup">` in `index.html` to your form service URL. Until then the form does not collect addresses.
