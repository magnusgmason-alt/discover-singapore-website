"""Place pages: /places/<id> for every pin on the map, plus /places (all places).

Data: make_trip.HIGHLIGHTS (+ places_new.NEW), places_content.json (text written from the
fact-checked book), photos/places/manifest.json (Pexels photos chosen per place).
extend(make_trip) is called before the map/trip data are written; main() writes the pages;
build_images(IMG) resizes the photos during the site build.
"""
import html
import json
import math
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "https://discoversingapore.org"
CONTENT = json.loads((ROOT / "places_content.json").read_text(encoding="utf8"))
MANIFEST_P = ROOT / "photos" / "places" / "manifest.json"
MANIFEST = json.loads(MANIFEST_P.read_text(encoding="utf8")) if MANIFEST_P.exists() else []
esc = lambda s: html.escape(s or "", quote=True)


def photos_for(pid):
    out = []
    for m in MANIFEST:
        if m["pl"] == pid and (ROOT / "photos" / "places" / f"px-{m['id']}.jpg").exists():
            out.append(m)
    return sorted(out, key=lambda m: m["k"])


def extend(M):
    """Add the new places and the book-checked tag/desc to make_trip's data."""
    import places_new as N
    have = {h["id"] for h in M.HIGHLIGHTS}
    for n in N.NEW:
        if n["id"] in have:
            continue
        M.HIGHLIGHTS.append(dict(n, grid=False, img="", tag="", desc=""))
    M.COORDS.update(N.NEW_COORDS)
    for h in M.HIGHLIGHTS:
        c = CONTENT.get(h["id"])
        if c:
            h["tag"] = c["tag"] or h["tag"]
            h["desc"] = c["desc"] or h["desc"]
        ph = photos_for(h["id"])
        h["pimg"] = f"/assets/img/places/px-{ph[0]['id']}-800.jpg" if ph else ""
    # drop places we cannot describe from the book
    M.HIGHLIGHTS[:] = [h for h in M.HIGHLIGHTS if h["id"] in CONTENT]


def build_images(img_dir):
    from PIL import Image
    out = Path(img_dir) / "places"
    out.mkdir(parents=True, exist_ok=True)
    n = 0
    for f in sorted((ROOT / "photos" / "places").glob("px-*.jpg")):
        with Image.open(f) as im:
            im = im.convert("RGB")
            for w in (800, 1600):
                r = im if im.width <= w else im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
                r.save(out / f"{f.stem}-{w}.jpg", quality=82, optimize=True, progressive=True)
        n += 1
    print("place photos", n)


def dist_km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 6371 * 2 * math.asin(math.sqrt(h))


PLACE_CSS = """
.p-hero { position: relative; min-height: 78svh; display: flex; align-items: flex-end; color: var(--white); background: var(--teal); overflow: hidden; }
.p-hero > img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
.p-hero .shade { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(8,12,16,.5) 0%, rgba(8,12,16,.1) 35%, rgba(8,12,16,.85) 100%); }
.p-hero.noimg .shade { background: radial-gradient(120% 90% at 85% 10%, rgba(200,32,47,.35), transparent 60%); }
.p-hero-inner { position: relative; width: 100%; max-width: 1180px; margin: 0 auto; padding: calc(var(--header-h) + 48px) 24px 54px; }
.p-hero .a-crumbs a { color: inherit; }
.p-kind { display: inline-block; font: 700 .68rem var(--sans); letter-spacing: .18em; text-transform: uppercase; background: var(--red); padding: 6px 12px; border-radius: 999px; margin-bottom: 18px; }
.p-hero h1 { font-size: clamp(2.3rem, 6vw, 4.6rem); font-weight: 800; letter-spacing: -.035em; line-height: 1.02; max-width: 16ch; text-wrap: balance; }
.p-hero .p-tag { font: 400 clamp(1.05rem, 2vw, 1.35rem)/1.45 var(--serif); font-style: italic; margin-top: 14px; max-width: 46ch; opacity: .95; }
.p-hero .p-credit { position: absolute; right: 16px; bottom: 12px; font-size: .68rem; opacity: .75; }
.p-hero .p-credit a { color: inherit; }
.p-wrap { max-width: 1180px; margin: 0 auto; padding: 56px 24px 24px; display: grid; grid-template-columns: minmax(0, 1fr) 340px; gap: 56px; align-items: start; }
.p-main .lead { font: 400 1.32rem/1.6 var(--serif); color: var(--ink); margin-bottom: 1.1em; }
.p-main p { font-size: 1.06rem; line-height: 1.78; margin-bottom: 1.1em; max-width: 68ch; }
.p-gallery { display: grid; grid-template-columns: repeat(6, 1fr); grid-auto-rows: 150px; gap: 10px; margin: 34px 0 10px; }
.p-gallery figure { position: relative; margin: 0; overflow: hidden; border-radius: var(--radius); background: var(--stone); cursor: zoom-in; grid-column: span 3; grid-row: span 2; }
.p-gallery figure:nth-child(3n+1) { grid-column: span 6; grid-row: span 3; }
.p-gallery figure img { width: 100%; height: 100%; object-fit: cover; transition: transform .6s ease; }
.p-gallery figure:hover img { transform: scale(1.04); }
.p-gallery figcaption { position: absolute; left: 0; right: 0; bottom: 0; padding: 26px 12px 8px; font-size: .72rem; color: #fff; background: linear-gradient(transparent, rgba(8,12,16,.7)); }
.p-gallery figcaption a { color: inherit; }
.p-side { position: sticky; top: calc(var(--header-h) + 20px); display: grid; gap: 16px; }
.p-card { background: var(--white); border: 1px solid var(--stone); border-radius: 10px; padding: 22px; }
.p-card h2 { margin: 0 0 14px; line-height: 1.3; font-size: .72rem; letter-spacing: .18em; text-transform: uppercase; margin-bottom: 14px; color: var(--muted); }
.p-facts { display: grid; gap: 12px; margin: 0; }
.p-facts div { border-top: 1px solid var(--stone); padding-top: 10px; }
.p-facts dt { font: 700 .66rem var(--sans); letter-spacing: .14em; text-transform: uppercase; color: var(--red); }
.p-facts dd { margin: 3px 0 0; font-size: .95rem; line-height: 1.5; }
.p-checked { font-size: .75rem; color: var(--muted); margin-top: 14px; }
.p-tip { background: var(--teal); color: #fff; border-radius: 10px; padding: 20px 22px; }
.p-tip h2 { font-size: .72rem; letter-spacing: .18em; text-transform: uppercase; margin: 0 0 10px; color: #d9dee0; line-height: 1.3; }
.p-tip p { font: 400 1.02rem/1.55 var(--serif); }
.p-actions { display: grid; gap: 10px; }
.p-actions .addt { position: static; justify-content: center; height: 46px; width: 100%; font-size: .7rem; box-shadow: none; border: 1px solid var(--ink); }
.p-actions .addt span { display: inline !important; }
.p-actions .btn { width: 100%; justify-content: center; text-align: center; }
.p-book { display: flex; gap: 14px; align-items: center; text-decoration: none; color: inherit; }
.p-book img { width: 64px; height: auto; border-radius: 3px; box-shadow: 0 6px 16px rgba(8,12,16,.25); }
.p-book strong { display: block; font-size: .95rem; }
.p-book span { font-size: .82rem; color: var(--muted); }
.p-map { height: 300px; border-radius: 10px; overflow: hidden; border: 1px solid var(--stone); background: var(--stone); }
.p-near { max-width: 1180px; margin: 0 auto; padding: 40px 24px 80px; }
.p-near h2 { font-size: clamp(1.5rem, 3vw, 2rem); margin-bottom: 20px; }
.p-near-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 16px; }
.p-near-grid a { display: block; text-decoration: none; color: inherit; background: var(--white); border-radius: 10px; overflow: hidden; border: 1px solid var(--stone); transition: transform .2s; }
.p-near-grid a:hover { transform: translateY(-3px); }
.p-near .ph { aspect-ratio: 4 / 3; background: var(--teal); position: relative; }
.p-near .ph img { width: 100%; height: 100%; object-fit: cover; }
.p-near .ph .card-ph { position: absolute; inset: 0; }
.p-near .tx { padding: 14px 16px 16px; }
.p-near .tx small { font: 700 .62rem var(--sans); letter-spacing: .14em; text-transform: uppercase; color: var(--red); }
.p-near .tx strong { display: block; font-size: 1.02rem; margin: 4px 0 2px; }
.p-near .tx span { font-size: .82rem; color: var(--muted); }
.lb { position: fixed; inset: 0; z-index: 200; background: rgba(8,12,16,.94); display: flex; align-items: center; justify-content: center; padding: 24px; }
.lb[hidden] { display: none; }
.lb img { max-width: 100%; max-height: 86vh; border-radius: 4px; }
.lb button { position: absolute; top: 14px; right: 16px; width: 44px; height: 44px; border-radius: 50%; border: 0; background: rgba(255,255,255,.12); color: #fff; font-size: 1.5rem; cursor: pointer; }
.lb p { position: absolute; left: 0; right: 0; bottom: 14px; text-align: center; color: #cfd6da; font-size: .8rem; }
.lb p a { color: inherit; }
.pl-filter { display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 26px; }
@media (max-width: 960px) {
  .p-wrap { grid-template-columns: 1fr; gap: 32px; }
  .p-side { position: static; }
  .p-gallery { grid-auto-rows: 110px; }
}
@media (max-width: 560px) {
  .p-gallery { grid-template-columns: 1fr 1fr; grid-auto-rows: 120px; }
  .p-gallery figure, .p-gallery figure:nth-child(3n+1) { grid-column: span 2; grid-row: span 2; }
}
"""

PLACE_JS = """
<script>
(function () {
  var lb = document.getElementById('lb');
  if (lb) {
    var img = lb.querySelector('img'), cap = lb.querySelector('p');
    document.querySelectorAll('.p-gallery figure').forEach(function (f) {
      f.addEventListener('click', function (e) {
        if (e.target.closest('a')) return;
        img.src = f.dataset.full; img.alt = f.querySelector('img').alt; cap.innerHTML = f.querySelector('figcaption').innerHTML;
        lb.hidden = false;
      });
    });
    function close() { lb.hidden = true; img.src = ''; }
    lb.addEventListener('click', function (e) { if (e.target === lb || e.target.closest('button')) close(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
  }
  var el = document.getElementById('pmap');
  if (!el) return;
  var io = new IntersectionObserver(function (en) {
    if (!en[0].isIntersecting) return; io.disconnect();
    var CDN = 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/';
    var css = document.createElement('link'); css.rel = 'stylesheet'; css.href = CDN + 'leaflet.min.css'; document.head.appendChild(css);
    var s = document.createElement('script'); s.src = CDN + 'leaflet.min.js';
    s.onload = function () {
      var L = window.L, d = JSON.parse(el.dataset.pts);
      var m = L.map(el, { scrollWheelZoom: false, zoomControl: true }).setView(d[0].ll, 15);
      L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 19, attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>' }).addTo(m);
      d.forEach(function (p, i) {
        var ic = L.divIcon({ className: 'smap-pin-wrap', html: '<span class="smap-pin' + (i === 0 ? ' is-active' : '') + '"></span>', iconSize: [26, 26], iconAnchor: [13, 13] });
        var mk = L.marker(p.ll, { icon: ic, zIndexOffset: i === 0 ? 1000 : 0 }).addTo(m);
        mk.bindTooltip(p.n);
        if (i) mk.on('click', function () { location.href = '/places/' + p.id; });
      });
    };
    document.head.appendChild(s);
  }, { rootMargin: '300px' });
  io.observe(el);
})();
</script>
"""


def credit(m):
    return (f'Photo: <a href="https://www.pexels.com/photo/{m["id"]}/" target="_blank" rel="noopener">'
            f'{esc(m["u"] or "Pexels")}</a> / Pexels')


def thumb(h):
    if h.get("pimg"):
        return f'<img src="{h["pimg"]}" alt="{esc(h["name"])}" loading="lazy" decoding="async">'
    if h.get("img"):
        return f'<img src="/assets/img/{h["img"]}-800.jpg" alt="{esc(h["name"])}" loading="lazy" decoding="async">'
    return f'<span class="card-ph" data-kind="{esc(h["kind"])}" aria-hidden="true"></span>'


def page(h, M, A):
    c = CONTENT[h["id"]]
    ph = photos_for(h["id"])
    url = f"{SITE}/places/{h['id']}"
    ll = M.COORDS[h["id"]]
    others = sorted((o for o in M.HIGHLIGHTS if o["id"] != h["id"]), key=lambda o: dist_km(ll, M.COORDS[o["id"]]))[:8]
    pts = [{"id": h["id"], "n": h["name"], "ll": ll}] + [{"id": o["id"], "n": o["name"], "ll": M.COORDS[o["id"]]} for o in others]

    if ph:
        hero_img = (f'<img src="/assets/img/places/px-{ph[0]["id"]}-1600.jpg" srcset="/assets/img/places/px-{ph[0]["id"]}-800.jpg 800w, '
                    f'/assets/img/places/px-{ph[0]["id"]}-1600.jpg 1600w" sizes="100vw" alt="{esc(ph[0]["a"] or ph[0]["t"])}" fetchpriority="high">')
        hero_credit = f'<p class="p-credit">{credit(ph[0])}</p>'
        og = f"{SITE}/assets/img/places/px-{ph[0]['id']}-1600.jpg"
    elif h.get("img"):
        hero_img = f'<img src="/assets/img/{h["img"]}-1800.jpg" alt="{esc(h["name"])}" fetchpriority="high">'
        hero_credit, og = "", f"{SITE}/assets/img/{h['img']}-1800.jpg"
    else:
        hero_img, hero_credit, og = "", "", f"{SITE}/assets/img/hero-skyline-night-1800.jpg"

    gal_items = []
    if h.get("img"):
        gal_items.append(f'<figure data-full="/assets/img/{h["img"]}-1800.jpg"><img src="/assets/img/{h["img"]}-800.jpg" alt="{esc(h["name"])}" loading="lazy" decoding="async"><figcaption>Photo: Discover Singapore</figcaption></figure>')
    for m in ph[1:]:
        gal_items.append(f'<figure data-full="/assets/img/places/px-{m["id"]}-1600.jpg"><img src="/assets/img/places/px-{m["id"]}-800.jpg" alt="{esc(m["a"] or m["t"])}" loading="lazy" decoding="async"><figcaption>{esc(m["t"])} · {credit(m)}</figcaption></figure>')
    gallery = f'<div class="p-gallery">{"".join(gal_items)}</div>' if gal_items else ""

    body = "".join(f"<p>{esc(p)}</p>" for p in c["body"])
    facts = "".join(f"<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>" for k, v in c["facts"])
    tip = f'<div class="p-tip"><h2>Good to know</h2><p>{esc(c["tip"])}</p></div>' if c.get("tip") else ""
    maps = "https://www.google.com/maps/search/?api=1&query=" + html.escape(h["q"]).replace(" ", "+")
    guide = M.GUIDES.get(h["id"])
    guide_link = f'<a class="btn outline" href="/blog/{guide}">Read our guide</a>' if guide else ""
    chap = c.get("chapter")
    book = (f'<a class="p-card p-book" href="/complete-guide"><img src="/assets/img/cover-guide-500.jpg?v=3" alt="Discover Singapore, the complete guide" width="64">'
            f'<div><strong>More in the book</strong><span>{"Chapter " + str(chap) + " of " if chap else ""}Discover Singapore, the Complete Guide 2027. 232 pages, 8 maps.</span></div></a>')
    near = "".join(
        f'<a href="/places/{o["id"]}"><div class="ph">{thumb(o)}</div><div class="tx"><small>{esc(o["kind"])} · {dist_km(ll, M.COORDS[o["id"]]):.1f} km</small><strong>{esc(o["name"])}</strong><span>{esc(o["tag"])}</span></div></a>'
        for o in others[:4])
    ld = {"@context": "https://schema.org", "@type": "TouristAttraction", "name": h["name"], "description": c["meta"],
          "url": url, "image": [og], "geo": {"@type": "GeoCoordinates", "latitude": ll[0], "longitude": ll[1]},
          "address": {"@type": "PostalAddress", "addressLocality": h["area"], "addressCountry": "SG"}}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Discover Singapore", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Places", "item": SITE + "/places"},
        {"@type": "ListItem", "position": 3, "name": h["name"], "item": url}]}
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(c['title'])} · Discover Singapore</title>
<meta name="description" content="{esc(c['meta'])}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Discover Singapore">
<meta property="og:title" content="{esc(c['title'])}">
<meta property="og:description" content="{esc(c['meta'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta name="twitter:card" content="summary_large_image">
{A.FONTS}
<script type="application/ld+json">{json.dumps(ld)}</script>
<script type="application/ld+json">{json.dumps(crumbs)}</script>
<link rel="stylesheet" href="/static/trip.css">
<link rel="stylesheet" href="/static/map.css">
<style>{A.STYLE}{A.ARTICLE_CSS}{PLACE_CSS}</style>
</head>
<body>
{A.HEADER}
<main id="top">
  <section class="p-hero{'' if hero_img else ' noimg'}">
    {hero_img}
    <div class="shade"></div>
    <div class="p-hero-inner">
      <p class="a-crumbs"><a href="/">Discover Singapore</a> / <a href="/places">Places</a> / {esc(h['area'])}</p>
      <span class="p-kind">{esc(h['kind'])} · {esc(h['area'])}</span>
      <h1>{esc(h['name'])}</h1>
      <p class="p-tag">{esc(h['tag'])}</p>
    </div>
    {hero_credit}
  </section>
  <div class="p-wrap">
    <article class="p-main">
      <p class="lead">{esc(c['lead'])}</p>
      {body}
      {gallery}
    </article>
    <aside class="p-side">
      <div class="p-actions">
        <button class="addt" type="button" data-trip="{h['id']}" aria-pressed="false"><b>+</b><span>Add to my trip</span></button>
        <a class="btn primary" href="{maps}" target="_blank" rel="noopener">Open in Google Maps</a>
        {guide_link}
      </div>
      <div class="p-card"><h2>Plan your visit</h2><dl class="p-facts">{facts}</dl><p class="p-checked">{esc(c.get('checked') or '')}</p></div>
      {tip}
      {book}
    </aside>
  </div>
  <section class="p-near">
    <h2>On the map nearby</h2>
    <div class="p-map" id="pmap" data-pts='{esc(json.dumps(pts))}' role="region" aria-label="Map of {esc(h['name'])} and nearby places"></div>
    <div class="p-near-grid" style="margin-top:18px">{near}</div>
    <p style="margin-top:26px"><a class="link-arrow" href="/places">All {len(M.HIGHLIGHTS)} places →</a> &nbsp; <a class="link-arrow" href="/#map">Back to the map →</a></p>
  </section>
  <div class="lb" id="lb" hidden><button type="button" aria-label="Close">×</button><img alt=""><p></p></div>
</main>
{A.FOOTER}
{A.SCRIPT}
<script src="/static/trip.js" defer></script>
{PLACE_JS}
</body>
</html>
"""


def index_page(M, A):
    order = sorted(M.HIGHLIGHTS, key=lambda h: h["name"])
    cats = M.CATS
    chips = "".join(f'<button class="hl-chip" type="button" data-cat="{k}" aria-pressed="{"true" if k == "all" else "false"}">{v}</button>' for k, v in cats)
    cards = "".join(
        f'<a href="/places/{h["id"]}" data-cats="{h["cats"]}"><div class="ph">{thumb(h)}</div><div class="tx"><small>{esc(h["kind"])} · {esc(h["area"])}</small><strong>{esc(h["name"])}</strong><span>{esc(h["tag"])}</span></div></a>'
        for h in order)
    desc = f"All {len(order)} places on the Discover Singapore map: sights, gardens, temples, hawker centres and neighbourhoods, each with photos, practical facts and a map."
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Places to Visit in Singapore: {len(order)} Sights With Photos · Discover Singapore</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{SITE}/places">
<meta property="og:type" content="website">
<meta property="og:title" content="Places to Visit in Singapore">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{SITE}/places">
<meta property="og:image" content="{SITE}/assets/img/hero-skyline-night-1800.jpg">
{A.FONTS}
<link rel="stylesheet" href="/static/trip.css">
<style>{A.STYLE}{A.ARTICLE_CSS}{PLACE_CSS}</style>
</head>
<body>
{A.HEADER}
<main id="top">
  <section class="t-hero" style="background:var(--teal);color:#fff;padding:calc(var(--header-h) + 56px) 0 48px">
    <div class="container">
      <p class="a-crumbs"><a href="/" style="color:inherit">Discover Singapore</a> / Places</p>
      <h1 style="font-size:clamp(2.2rem,5.5vw,4rem);letter-spacing:-.03em;line-height:1.05;margin-top:10px">Places to visit in Singapore</h1>
      <p class="lead" style="max-width:60ch;margin-top:14px;color:#d9dee0">{esc(desc)}</p>
    </div>
  </section>
  <section class="p-near">
    <div class="pl-filter" role="group" aria-label="Filter places">{chips}</div>
    <div class="p-near-grid" id="plGrid">{cards}</div>
  </section>
</main>
{A.FOOTER}
{A.SCRIPT}
<script src="/static/trip.js" defer></script>
<script>
(function () {{
  var chips = [].slice.call(document.querySelectorAll('.pl-filter .hl-chip')), cards = [].slice.call(document.querySelectorAll('#plGrid > a'));
  chips.forEach(function (ch) {{ ch.addEventListener('click', function () {{
    var c = ch.dataset.cat;
    chips.forEach(function (o) {{ o.setAttribute('aria-pressed', o === ch ? 'true' : 'false'); }});
    cards.forEach(function (a) {{ a.hidden = !(c === 'all' || (' ' + a.dataset.cats + ' ').indexOf(' ' + c + ' ') !== -1); }});
  }}); }});
}})();
</script>
</body>
</html>
"""


def main():
    import make_trip as M
    import make_articles as A
    out = ROOT / "places"
    out.mkdir(exist_ok=True)
    for f in out.glob("*.html"):
        f.unlink()
    for h in M.HIGHLIGHTS:
        (out / f"{h['id']}.html").write_text(page(h, M, A), encoding="utf8")
    (out / "index.html").write_text(index_page(M, A), encoding="utf8")
    # sitemap
    sm = (ROOT / "sitemap.xml").read_text(encoding="utf8")
    import re
    sm = re.sub(r"\s*<url><loc>https://discoversingapore.org/places[^<]*</loc>[^\n]*</url>", "", sm)
    add = "".join(f"\n  <url><loc>{SITE}/places/{h['id']}</loc><lastmod>2026-10-30</lastmod></url>" for h in M.HIGHLIGHTS)
    sm = sm.replace("</urlset>", f"  <url><loc>{SITE}/places</loc><lastmod>2026-10-30</lastmod></url>{add}\n</urlset>")
    (ROOT / "sitemap.xml").write_text(sm, encoding="utf8")
    print("place pages", len(M.HIGHLIGHTS))
