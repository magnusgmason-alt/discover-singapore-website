"""Build the Discover Singapore site into dist/.

Resizes the original photos in photos/ into dist/assets/img/ (800 px and
1800 px wide versions) and copies the page files. Cloudflare Pages runs:
    pip install pillow && python3 build.py
with build output directory: dist
"""
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).parent
PHOTOS = ROOT / "photos"
DIST = ROOT / "dist"
IMG = DIST / "assets" / "img"

# Image slot used in index.html -> original photo in photos/
SLOTS = {
    "hero-skyline-night": "14cb7489-image.jpg",
    "strip-supertrees": "35612b21-image.jpg",
    "strip-marina-bay-day": "4a7806c0-image.jpg",
    "strip-jewel": "a201bd3c-image.jpg",
    "strip-artscience": "fa2abd11-image.jpg",
    "editions-supertree-night": "7b5fbe19-image.jpg",
    "guide-bay-day": "4a7806c0-image.jpg",
    "nomad-cbd-night": "5b797241-image.jpg",
    "garden-jewel": "35e56174-image.jpg",
    "journal-skyline-dusk": "d2733fba-image.jpg",
    "journal-shophouses": "7a58f5e0-image.jpg",
    "journal-cbd": "5b797241-image.jpg",
    "quiet-dusk": "229e958b-image.jpg",
    "checklist-mbs-night": "ab39ff59-image.jpg",
    "hl-supertree-grove": "3e938099-image.jpg",
    "hl-marina-bay-sands": "e8386486-image.jpg",
    "hl-jewel": "35e56174-image.jpg",
    "hl-artscience": "94741835-image.jpg",
    "hl-skyway": "16ab58e2-image.jpg",
    "hl-marina-barrage": "7d01a487-image.jpg",
    "hl-fullerton": "d2733fba-image.jpg",
    "hl-merlion": "merlion-night.jpg",
    "hl-flyer": "fea3e8d1-image.jpg",
    "hl-night-lights": "9916a914-image.jpg",
    "hl-bayfront-night": "fd34662d-image.jpg",
    "hl-supertrees-above": "eed7ad4b-image.jpg",
    "guides-mbs-teal": "528ebd4c-image.jpg",
}

# Book covers: add photos/cover-guide.jpg (or .png) and photos/cover-nomad.jpg
# to replace the placeholders.
COVERS = {
    "cover-guide": "THE COMPLETE TRAVEL GUIDE",
    "cover-nomad": "EXPAT & DIGITAL NOMAD EDITION",
}

PAGE_FILES = ["index.html", "trip.html", "robots.txt", "sitemap.xml"]
PAGE_DIRS = ["blog", "static"]


def save_sizes(im, name, widths):
    im = im.convert("RGB")
    for w in widths:
        r = min(1, w / im.width)
        out = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
        out.save(IMG / f"{name}-{w}.jpg", quality=80, optimize=True, progressive=True)


def font(size):
    try:
        return ImageFont.load_default(size=size)
    except TypeError:
        return ImageFont.load_default()


def placeholder_cover(subtitle):
    im = Image.new("RGB", (900, 1350), (14, 19, 23))
    d = ImageDraw.Draw(im)
    d.rectangle([90, 560, 190, 570], fill=(200, 32, 47))
    d.text((90, 600), "DISCOVER", font=font(64), fill=(255, 255, 255))
    d.text((90, 680), "SINGAPORE", font=font(64), fill=(255, 255, 255))
    d.text((90, 790), subtitle, font=font(32), fill=(170, 180, 186))
    return im


def version_assets():
    """Add ?v=<content hash> to /static/ links so browsers fetch new versions."""
    import hashlib
    tags = {}
    for f in (DIST / "static").iterdir():
        tags[f"/static/{f.name}"] = hashlib.md5(f.read_bytes()).hexdigest()[:8]
    for page in DIST.rglob("*.html"):
        s = page.read_text(encoding="utf8")
        for url, h in tags.items():
            s = s.replace(f'"{url}"', f'"{url}?v={h}"')
        page.write_text(s, encoding="utf8")


def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    IMG.mkdir(parents=True)

    import make_trip
    make_trip.main()  # updates index.html highlights, writes trip.html and static/
    import make_articles
    make_articles.main()

    for f in PAGE_FILES:
        shutil.copy(ROOT / f, DIST / f)
    for d in PAGE_DIRS:
        shutil.copytree(ROOT / d, DIST / d)

    version_assets()

    for slot, photo in SLOTS.items():
        with Image.open(PHOTOS / photo) as im:
            save_sizes(im, slot, (800, 1800))
        print("photo", slot)

    for name, subtitle in COVERS.items():
        found = [p for p in (PHOTOS / f"{name}.jpg", PHOTOS / f"{name}.png") if p.exists()]
        if found:
            with Image.open(found[0]) as im:
                save_sizes(im, name, (500, 900))
            print("cover", name)
        else:
            save_sizes(placeholder_cover(subtitle), name, (500, 900))
            print("cover placeholder", name)


if __name__ == "__main__":
    main()
