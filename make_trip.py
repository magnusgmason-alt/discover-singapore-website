"""Highlights grid (categories + "show more"), "Add to my trip" buttons, the /trip page
and the free PDF itinerary.

Everything runs in the visitor's browser (the trip is kept in localStorage), so the
site stays static. build.py calls make_trip.main() before copying files to dist/.

To add a highlight: add an entry to HIGHLIGHTS. "img" is an image slot from build.py
(SLOTS); leave it empty and the card shows a placeholder until a photo is added.
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "https://discoversingapore.org"
VISIBLE = 12   # cards shown before "Show more highlights"
MAX_PLACES = 10  # Google Maps route links take up to 10 stops

CATS = [
    ("all", "All"),
    ("icons", "Icons"),
    ("nature", "Gardens & nature"),
    ("culture", "Culture"),
    ("food", "Food"),
    ("nightlife", "Nightlife"),
    ("shopping", "Shopping"),
    ("family", "Family"),
]

# kind is printed on the PDF; area shows on the card tag.
HIGHLIGHTS = [
    dict(id="gardens-by-the-bay", name="Gardens by the Bay", area="Marina Bay", kind="Gardens",
         cats="icons nature family", img="hl-supertree-grove",
         tag="Supertrees and cooled glass domes.",
         desc="A 101-hectare garden on reclaimed land beside Marina Bay. The Supertree Grove and outdoor gardens are free; the Flower Dome and Cloud Forest are cooled conservatories with their own tickets.",
         q="Gardens by the Bay, Singapore"),
    dict(id="marina-bay-sands-skypark", name="Marina Bay Sands SkyPark", area="Marina Bay", kind="Viewpoint",
         cats="icons nightlife", img="hl-marina-bay-sands",
         tag="Three towers and a sky deck on top.",
         desc="The observation deck at the top of Marina Bay Sands, about 200 metres up, looks over the bay, the city skyline and the ships waiting in the strait. Go at sunset and stay for the lights.",
         q="Sands SkyPark Observation Deck, Singapore"),
    dict(id="merlion-park", name="Merlion Park", area="Downtown", kind="Landmark",
         cats="icons", img="hl-merlion",
         tag="Half lion, half fish, spouting into the bay.",
         desc="The 8.6-metre Merlion statue, Singapore's mascot, spouts water into Marina Bay with Marina Bay Sands across the water. Busy all day; early morning is quietest.",
         q="Merlion Park, Singapore"),
    dict(id="jewel-changi", name="Jewel Changi", area="Changi", kind="Landmark",
         cats="icons shopping family", img="hl-jewel",
         tag="The Rain Vortex, an indoor waterfall.",
         desc="A glass dome at Changi Airport around the Rain Vortex, a 40-metre indoor waterfall, with a forest valley, shops and restaurants. Easy to visit on arrival or before your flight home.",
         q="Jewel Changi Airport, Singapore"),
    dict(id="artscience-museum", name="ArtScience Museum", area="Marina Bay", kind="Museum",
         cats="culture family", img="hl-artscience",
         tag="The lotus-shaped museum on the bay.",
         desc="A lotus-shaped museum at Marina Bay Sands with changing exhibitions where art meets science, and the permanent digital art space Future World.",
         q="ArtScience Museum, Singapore"),
    dict(id="ocbc-skyway", name="OCBC Skyway", area="Gardens by the Bay", kind="Viewpoint",
         cats="nature", img="hl-skyway",
         tag="A walkway between the Supertrees.",
         desc="A 128-metre walkway 22 metres above the ground, strung between the Supertrees at Gardens by the Bay, with views over the gardens and the bay.",
         q="OCBC Skyway, Gardens by the Bay, Singapore"),
    dict(id="garden-rhapsody", name="Garden Rhapsody", area="Gardens by the Bay", kind="Light show",
         cats="nightlife nature family", img="hl-supertrees-above",
         tag="The Supertrees lit up after dark.",
         desc="A free light and music show at the Supertree Grove, held twice every evening. Lie back on the plaza and look up.",
         q="Supertree Grove, Gardens by the Bay, Singapore"),
    dict(id="singapore-flyer", name="Singapore Flyer", area="Marina Bay", kind="Viewpoint",
         cats="icons family", img="hl-flyer",
         tag="A 165-metre wheel over the bay.",
         desc="A 165-metre observation wheel at the edge of Marina Bay. One rotation takes about half an hour, with views over the city, the gardens and the strait.",
         q="Singapore Flyer, Singapore"),
    dict(id="marina-barrage", name="Marina Barrage", area="Marina South", kind="Park",
         cats="nature family", img="hl-marina-barrage",
         tag="A green roof between bay and sea.",
         desc="The dam that turned Marina Bay into a freshwater reservoir. Its grass-covered roof is a favourite for picnics, kite flying and sunset views of the skyline.",
         q="Marina Barrage, Singapore"),
    dict(id="fullerton-hotel", name="The Fullerton Hotel", area="Downtown", kind="Heritage",
         cats="culture icons", img="hl-fullerton",
         tag="The old post office on the waterfront.",
         desc="Built in 1928 as the General Post Office, this columned landmark at the mouth of the Singapore River is now a hotel and a national monument.",
         q="The Fullerton Hotel Singapore"),
    dict(id="spectra-show", name="Spectra light & water show", area="Marina Bay", kind="Light show",
         cats="nightlife family", img="hl-night-lights",
         tag="Lights, water and music by the bay.",
         desc="A free outdoor show of lights, water jets and music at the Event Plaza in front of Marina Bay Sands, held every evening.",
         q="Event Plaza, Marina Bay Sands, Singapore"),
    dict(id="marina-bay-promenade", name="Marina Bay waterfront", area="Marina Bay", kind="Walk",
         cats="nightlife icons", img="hl-bayfront-night",
         tag="A night walk around the bay.",
         desc="A walking loop of about 3.5 km around Marina Bay that links the Merlion, the Esplanade, the Helix Bridge and Marina Bay Sands. Best after dark.",
         q="Helix Bridge, Singapore"),
    # More highlights (shown with "Show more highlights" or a category)
    dict(id="chinatown", name="Chinatown", area="Chinatown", kind="Neighbourhood",
         cats="culture food shopping", img="journal-shophouses",
         tag="Temples, shophouses and hawker food.",
         desc="Shophouse streets around the Buddha Tooth Relic Temple and the Sri Mariamman Temple, Singapore's oldest Hindu temple, with hawker centres and markets on every block.",
         q="Chinatown, Singapore"),
    dict(id="maxwell-food-centre", name="Maxwell Food Centre", area="Chinatown", kind="Hawker centre",
         cats="food", img="",
         tag="Chicken rice and hawker classics.",
         desc="One of Singapore's best-known hawker centres, famous for Hainanese chicken rice. Go before noon or mid-afternoon to beat the office lunch crowd.",
         q="Maxwell Food Centre, Singapore"),
    dict(id="lau-pa-sat", name="Lau Pa Sat", area="Downtown", kind="Hawker centre",
         cats="food nightlife", img="",
         tag="Satay under a Victorian roof.",
         desc="A cast-iron market hall from 1894 in the financial district. In the evening, Boon Tat Street beside it closes to traffic and fills with satay grills.",
         q="Lau Pa Sat, Singapore"),
    dict(id="little-india", name="Little India", area="Little India", kind="Neighbourhood",
         cats="culture food shopping", img="",
         tag="Colour, spice and flower garlands.",
         desc="Temples, spice shops, garland stalls and South Indian restaurants around Serangoon Road, with Tekka Centre for food and fabric.",
         q="Little India, Singapore"),
    dict(id="kampong-glam", name="Kampong Glam", area="Kampong Glam", kind="Neighbourhood",
         cats="culture food shopping", img="",
         tag="The golden dome of Sultan Mosque.",
         desc="The historic Malay and Arab quarter around Sultan Mosque, with textile shops on Arab Street and Middle Eastern and Malay restaurants.",
         q="Sultan Mosque, Singapore"),
    dict(id="haji-lane", name="Haji Lane", area="Kampong Glam", kind="Street",
         cats="nightlife shopping", img="",
         tag="Murals, boutiques and bars.",
         desc="A narrow lane of painted shophouses with independent shops by day and small bars at night.",
         q="Haji Lane, Singapore"),
    dict(id="botanic-gardens", name="Singapore Botanic Gardens", area="Tanglin", kind="Gardens",
         cats="nature family", img="",
         tag="Orchids and old rainforest trees.",
         desc="A UNESCO World Heritage Site since 2015, with lakes, a patch of original rainforest and the National Orchid Garden. Free to enter; go early before the heat.",
         q="Singapore Botanic Gardens"),
    dict(id="national-gallery", name="National Gallery Singapore", area="Civic District", kind="Museum",
         cats="culture", img="",
         tag="Art in the old Supreme Court.",
         desc="Southeast Asian and Singaporean art in the former Supreme Court and City Hall buildings, with rooftop views over the Padang.",
         q="National Gallery Singapore"),
    dict(id="clarke-quay", name="Clarke Quay", area="Singapore River", kind="Riverside",
         cats="nightlife food", img="",
         tag="Riverside bars and boat rides.",
         desc="Restored riverside warehouses full of bars and restaurants. River cruises on traditional bumboats leave from here.",
         q="Clarke Quay, Singapore"),
    dict(id="orchard-road", name="Orchard Road", area="Orchard", kind="Shopping street",
         cats="shopping", img="",
         tag="Malls from end to end.",
         desc="Singapore's main shopping street, lined with malls, department stores and big hotels. Lit up for Christmas from November.",
         q="Orchard Road, Singapore"),
    dict(id="sentosa", name="Sentosa", area="Sentosa", kind="Island",
         cats="family", img="",
         tag="Beaches and Universal Studios.",
         desc="A resort island just south of the city with beaches, Universal Studios Singapore and a cable car. Reach it by monorail from VivoCity at HarbourFront.",
         q="Sentosa, Singapore"),
    dict(id="mandai", name="Singapore Zoo & Night Safari", area="Mandai", kind="Wildlife park",
         cats="family nature", img="",
         tag="Open-concept zoo and a night safari.",
         desc="The Mandai wildlife parks in the north: Singapore Zoo, the Night Safari after dark, Bird Paradise and River Wonders. Plan a full day or an evening.",
         q="Singapore Zoo"),
    dict(id="southern-ridges", name="Southern Ridges & Henderson Waves", area="Southern Ridges", kind="Walk",
         cats="nature", img="",
         tag="A bridge above the canopy.",
         desc="Trails and walkways that link a chain of hilltop parks. Henderson Waves, a wave-shaped wooden bridge high above the forest, is the highlight.",
         q="Henderson Waves, Singapore"),
    dict(id="pulau-ubin", name="Pulau Ubin", area="North-east", kind="Island",
         cats="nature", img="",
         tag="Bicycles, mangroves and old kampongs.",
         desc="A small island reached by bumboat from Changi Point Ferry Terminal, with village houses, cycling trails and the Chek Jawa wetlands.",
         q="Pulau Ubin, Singapore"),
    dict(id="tiong-bahru", name="Tiong Bahru", area="Tiong Bahru", kind="Neighbourhood",
         cats="food culture", img="",
         tag="Art Deco flats and cafés.",
         desc="A 1930s housing estate of Art Deco flats with a well-loved market and hawker centre, bakeries and independent cafés.",
         q="Tiong Bahru Market, Singapore"),
    dict(id="joo-chiat", name="Joo Chiat & Katong", area="East coast", kind="Neighbourhood",
         cats="culture food", img="",
         tag="Pastel Peranakan shophouses.",
         desc="Colourful Peranakan shophouses, especially on Koon Seng Road, plus Katong laksa and old-school bakeries.",
         q="Koon Seng Road, Singapore"),
    # Map only (not in the highlights grid)
    dict(id="raffles-hotel", name="Raffles Hotel", area="Civic District", kind="Heritage", grid=False,
         cats="culture icons", img="",
         tag="The colonial grand hotel of 1887.",
         desc="Singapore's most famous hotel opened in 1887. The Long Bar, where the Singapore Sling is said to have been created, and the arcade shops are open to non-guests.",
         q="Raffles Hotel Singapore"),
    dict(id="esplanade", name="Esplanade – Theatres on the Bay", area="Marina Bay", kind="Arts centre", grid=False,
         cats="culture nightlife", img="",
         tag="The spiky domes on the bay.",
         desc="The arts centre with two spiky domes that locals compare to durians. Look out for free performances on the outdoor stage by the water, and the rooftop terrace with bay views.",
         q="Esplanade Theatres on the Bay, Singapore"),
    dict(id="fort-canning", name="Fort Canning Park", area="Civic District", kind="Park", grid=False,
         cats="nature culture", img="",
         tag="The old royal hill above the city.",
         desc="A hill park in the city centre with centuries of history, from 14th-century Malay kings to a British fort and the wartime Battlebox bunker. Shady paths and gardens; quiet in the morning.",
         q="Fort Canning Park, Singapore"),
    dict(id="asian-civilisations-museum", name="Asian Civilisations Museum", area="Singapore River", kind="Museum", grid=False,
         cats="culture family", img="",
         tag="Asia's art and trade by the river.",
         desc="A museum on the Singapore River about the cultures and trade routes of Asia, including the cargo of a 9th-century shipwreck found off Indonesia.",
         q="Asian Civilisations Museum, Singapore"),
    dict(id="peranakan-museum", name="Peranakan Museum", area="Civic District", kind="Museum", grid=False,
         cats="culture", img="",
         tag="Beadwork, porcelain and Nyonya style.",
         desc="A museum in a former school on Armenian Street about Peranakan culture, the mixed heritage of the Straits Chinese and other communities, with fashion, jewellery and household treasures.",
         q="Peranakan Museum, Singapore"),
    dict(id="buddha-tooth-relic-temple", name="Buddha Tooth Relic Temple", area="Chinatown", kind="Temple", grid=False,
         cats="culture", img="",
         tag="A Tang-style temple in Chinatown.",
         desc="A large Buddhist temple in Chinatown built in the style of the Tang dynasty, with museum floors and a rooftop orchid garden. Free to visit; dress modestly and cover shoulders and knees.",
         q="Buddha Tooth Relic Temple, Singapore"),
    dict(id="thian-hock-keng", name="Thian Hock Keng Temple", area="Telok Ayer", kind="Temple", grid=False,
         cats="culture", img="",
         tag="Singapore's oldest Hokkien temple.",
         desc="A temple from the 1840s on Telok Ayer Street, once on the waterfront, where sailors gave thanks for a safe voyage. Look up at the carved stone, painted beams and roof figures.",
         q="Thian Hock Keng Temple, Singapore"),
    dict(id="chinatown-complex", name="Chinatown Complex Food Centre", area="Chinatown", kind="Hawker centre", grid=False,
         cats="food", img="",
         tag="Hundreds of stalls under one roof.",
         desc="One of Singapore's largest hawker centres, on the floor above a wet market. Wander the rows for claypot rice, noodles, dim sum and local craft beer.",
         q="Chinatown Complex Food Centre, Singapore"),
    dict(id="east-coast-park", name="East Coast Park", area="East coast", kind="Park", grid=False,
         cats="nature family food", img="",
         tag="Beaches, bikes and seafood.",
         desc="A long park along the east coast with beaches, cycling and skating paths, bike rental and barbecue pits, plus the East Coast Lagoon Food Village for satay and seafood.",
         q="East Coast Park, Singapore"),
    dict(id="macritchie-treetop-walk", name="MacRitchie TreeTop Walk", area="Central nature reserve", kind="Walk", grid=False,
         cats="nature", img="",
         tag="A suspension bridge above the rainforest.",
         desc="A free-standing suspension bridge high in the canopy of the Central Catchment Nature Reserve, reached by forest trails from MacRitchie Reservoir. Allow half a day, bring water and check opening days.",
         q="TreeTop Walk, MacRitchie, Singapore"),
    dict(id="bukit-timah", name="Bukit Timah Nature Reserve", area="Bukit Timah", kind="Nature reserve", grid=False,
         cats="nature", img="",
         tag="Old rainforest and Singapore's highest hill.",
         desc="One of the world's few patches of primary rainforest inside a city, around Bukit Timah Hill, Singapore's highest point at about 164 metres. Go early for monkeys, birds and cooler air.",
         q="Bukit Timah Nature Reserve, Singapore"),
    dict(id="sungei-buloh", name="Sungei Buloh Wetland Reserve", area="North-west", kind="Nature reserve", grid=False,
         cats="nature family", img="",
         tag="Mangroves, birds and monitor lizards.",
         desc="Boardwalks through mangroves on the north-west coast, with migratory shorebirds in the cooler months, mudskippers, monitor lizards and the occasional estuarine crocodile.",
         q="Sungei Buloh Wetland Reserve, Singapore"),
    dict(id="haw-par-villa", name="Haw Par Villa", area="Pasir Panjang", kind="Theme park", grid=False,
         cats="culture family", img="",
         tag="A park of Chinese myths in statues.",
         desc="A quirky garden of more than a thousand statues and dioramas from Chinese legends, built in the 1930s by the brothers behind Tiger Balm. The gardens are free.",
         q="Haw Par Villa, Singapore"),
    dict(id="dempsey-hill", name="Dempsey Hill", area="Tanglin", kind="Neighbourhood", grid=False,
         cats="food nightlife", img="",
         tag="Restaurants in old army barracks.",
         desc="Former British army barracks among the trees, now home to restaurants, bars, wine shops and galleries. Popular for weekend brunch and dinner, a short ride from the Botanic Gardens.",
         q="Dempsey Hill, Singapore"),
    dict(id="holland-village", name="Holland Village", area="Holland", kind="Neighbourhood", grid=False,
         cats="food nightlife", img="",
         tag="Cafés and bars with a village feel.",
         desc="A relaxed neighbourhood popular with expats and students, with cafés, bars and restaurants around Lorong Mambong and a hawker centre. Next to Holland Village MRT station.",
         q="Holland Village, Singapore"),
    dict(id="jurong-lake-gardens", name="Jurong Lake Gardens", area="Jurong", kind="Gardens", grid=False,
         cats="nature family", img="",
         tag="Lakeside gardens in the west.",
         desc="Singapore's national gardens in the west, around Jurong Lake, with grasslands, boardwalks and a large free water playground for children.",
         q="Jurong Lake Gardens, Singapore"),
    dict(id="old-airport-road", name="Old Airport Road Food Centre", area="East", kind="Hawker centre", grid=False,
         cats="food", img="",
         tag="A local favourite for hawker food.",
         desc="A big, well-loved hawker centre on the site of Singapore's old Kallang Airport, with many long-running stalls. Mostly locals; go hungry and share plates.",
         q="Old Airport Road Food Centre, Singapore"),
    dict(id="newton-food-centre", name="Newton Food Centre", area="Newton", kind="Hawker centre", grid=False,
         cats="food nightlife", img="",
         tag="Open-air hawker centre for late dinners.",
         desc="An open-air hawker centre near Orchard, busiest in the evening, known for satay, barbecued stingray and chilli crab. Check prices before you order seafood.",
         q="Newton Food Centre, Singapore"),
    dict(id="geylang-serai", name="Geylang Serai", area="East", kind="Neighbourhood", grid=False,
         cats="culture food shopping", img="",
         tag="The heart of Malay Singapore.",
         desc="A historic Malay neighbourhood around Geylang Serai Market, with nasi padang, kueh and textiles. It is at its liveliest during the Ramadan bazaar.",
         q="Geylang Serai Market, Singapore"),
    dict(id="coney-island", name="Coney Island Park", area="Punggol", kind="Park", grid=False,
         cats="nature", img="",
         tag="A wild little island in the north-east.",
         desc="A small island park joined to Punggol by bridges, with casuarina woods, quiet beaches and cycling trails. Left rustic, with few facilities, so bring water.",
         q="Coney Island Park, Singapore"),
    dict(id="bishan-amk-park", name="Bishan-Ang Mo Kio Park", area="Bishan", kind="Park", grid=False,
         cats="nature family", img="",
         tag="A canal turned back into a river.",
         desc="A big heartland park where a concrete canal was turned into a winding natural river. Locals come for jogs and picnics, and otters are often seen.",
         q="Bishan-Ang Mo Kio Park, Singapore"),
    dict(id="changi-village", name="Changi Village", area="Changi", kind="Hawker centre", grid=False,
         cats="food", img="",
         tag="Nasi lemak by the sea.",
         desc="A laid-back seaside village at the eastern tip of the island. Its hawker centre is famous for nasi lemak, and bumboats to Pulau Ubin leave from the nearby jetty.",
         q="Changi Village Hawker Centre, Singapore"),
]

# Map coordinates (lat, lng). The first ten come from OpenStreetMap (Nominatim).
COORDS = {
    "gardens-by-the-bay": (1.28454, 103.86470), "marina-bay-sands-skypark": (1.28370, 103.86072),
    "merlion-park": (1.28678, 103.85450), "jewel-changi": (1.36022, 103.98967),
    "artscience-museum": (1.28614, 103.85923), "ocbc-skyway": (1.28215, 103.86364),
    "garden-rhapsody": (1.28160, 103.86400), "singapore-flyer": (1.28944, 103.86326),
    "marina-barrage": (1.28140, 103.87257), "fullerton-hotel": (1.28620, 103.85307),
    "spectra-show": (1.28520, 103.85980), "marina-bay-promenade": (1.28770, 103.86040),
    "chinatown": (1.28380, 103.84440), "maxwell-food-centre": (1.28030, 103.84480),
    "lau-pa-sat": (1.28070, 103.85050), "little-india": (1.30660, 103.85180),
    "kampong-glam": (1.30230, 103.85900), "haji-lane": (1.30070, 103.85870),
    "botanic-gardens": (1.31380, 103.81590), "national-gallery": (1.29030, 103.85150),
    "clarke-quay": (1.28840, 103.84650), "orchard-road": (1.30400, 103.83190),
    "sentosa": (1.25000, 103.82200), "mandai": (1.40430, 103.79300),
    "southern-ridges": (1.27630, 103.81550), "pulau-ubin": (1.40440, 103.96250),
    "tiong-bahru": (1.28510, 103.83260), "joo-chiat": (1.31290, 103.90210),
    "raffles-hotel": (1.29480, 103.85440), "esplanade": (1.28980, 103.85560),
    "fort-canning": (1.29490, 103.84640), "asian-civilisations-museum": (1.28750, 103.85140),
    "peranakan-museum": (1.29440, 103.84900), "buddha-tooth-relic-temple": (1.28150, 103.84430),
    "thian-hock-keng": (1.28070, 103.84760), "chinatown-complex": (1.28260, 103.84300),
    "east-coast-park": (1.30090, 103.91200), "macritchie-treetop-walk": (1.35990, 103.81070),
    "bukit-timah": (1.35460, 103.77640), "sungei-buloh": (1.44680, 103.72990),
    "haw-par-villa": (1.28320, 103.78190), "dempsey-hill": (1.30530, 103.80980),
    "holland-village": (1.31170, 103.79600), "jurong-lake-gardens": (1.33860, 103.72930),
    "old-airport-road": (1.30800, 103.88560), "newton-food-centre": (1.31190, 103.83960),
    "geylang-serai": (1.31720, 103.89820), "coney-island": (1.40880, 103.92190),
    "bishan-amk-park": (1.36290, 103.84340), "changi-village": (1.38900, 103.98760),
}

# Journal article to link from a place's map preview.
GUIDES = {
    "gardens-by-the-bay": "gardens-by-the-bay-guide", "ocbc-skyway": "gardens-by-the-bay-guide",
    "garden-rhapsody": "gardens-by-the-bay-guide", "marina-bay-sands-skypark": "things-to-do-in-marina-bay",
    "merlion-park": "things-to-do-in-marina-bay", "artscience-museum": "things-to-do-in-marina-bay",
    "singapore-flyer": "things-to-do-in-marina-bay", "spectra-show": "singapore-at-night",
    "marina-bay-promenade": "singapore-at-night", "marina-barrage": "free-things-to-do-in-singapore",
    "jewel-changi": "jewel-changi-guide", "botanic-gardens": "free-things-to-do-in-singapore",
    "southern-ridges": "free-things-to-do-in-singapore", "clarke-quay": "singapore-at-night",
    "lau-pa-sat": "singapore-at-night", "esplanade": "things-to-do-in-marina-bay",
    "chinatown": "where-to-stay-in-singapore", "tiong-bahru": "where-to-stay-in-singapore",
}

esc = lambda s: html.escape(s or "", quote=True)


def card(h, i):
    hidden = " hidden" if i >= VISIBLE else ""
    if h["img"]:
        pic = (f'<img src="assets/img/{h["img"]}-1800.jpg" srcset="assets/img/{h["img"]}-800.jpg 800w, '
               f'assets/img/{h["img"]}-1800.jpg 1800w" sizes="(min-width: 900px) 25vw, (min-width: 600px) 50vw, 100vw" '
               f'alt="{esc(h["name"])}" loading="lazy" decoding="async">')
    else:
        pic = f'<span class="card-ph" data-kind="{esc(h["kind"])}" aria-hidden="true"></span>'
    return (f'<div class="card hl" data-cats="{h["cats"]}"{hidden}>{pic}'
            f'<span class="card-tag">{esc(h["area"])}</span>'
            f'<button class="addt" type="button" data-trip="{h["id"]}" aria-pressed="false" '
            f'aria-label="Add {esc(h["name"])} to my trip"><b>+</b><span>Add to trip</span></button>'
            f'<span class="card-body"><strong>{esc(h["name"])}</strong><em>{esc(h["tag"])}</em></span></div>')


def grid_html():
    chips = "".join(
        f'<button class="hl-chip" type="button" data-cat="{k}" aria-pressed="{"true" if k == "all" else "false"}">{v}</button>'
        for k, v in CATS)
    cards = "\n        ".join(card(h, i) for i, h in enumerate(h for h in HIGHLIGHTS if h.get("grid", True)))
    return f"""<!--HL:START-->
      <div class="hl-chips" role="group" aria-label="Filter highlights">{chips}</div>
      <div class="card-grid" id="hlGrid">
        {cards}
      </div>
      <div class="hl-foot">
        <button class="btn outline" type="button" id="hlMore">Show more highlights</button>
        <a class="btn primary" href="/trip">Plan my trip · free PDF</a>
      </div>
      <!--HL:END-->"""


def trip_data():
    places = {}
    for h in HIGHLIGHTS:
        places[h["id"]] = {"n": h["name"], "a": h["area"], "k": h["kind"], "t": h["tag"], "d": h["desc"],
                           "q": h["q"], "i": f"/assets/img/{h['img']}-800.jpg" if h["img"] else "",
                           "c": h["cats"], "ll": COORDS[h["id"]], "b": GUIDES.get(h["id"], "")}
    return {"places": places, "max": MAX_PLACES}


def map_html():
    chips = "".join(
        f'<button class="hl-chip" type="button" data-cat="{k}" aria-pressed="{"true" if k == "all" else "false"}">{v}</button>'
        for k, v in CATS)
    return f"""<!--MAP:START-->
      <div class="hl-chips" id="smapChips" role="group" aria-label="Filter the map">{chips}</div>
      <div class="smap" id="smap">
        <div class="smap-list" id="smapList" aria-label="Places on the map"></div>
        <div class="smap-stage">
          <div class="smap-canvas" id="smapCanvas" role="region" aria-label="Map of Singapore"><p class="smap-loading">Loading the map…</p></div>
          <div class="smap-card" id="smapCard" hidden></div>
        </div>
      </div>
      <!--MAP:END-->"""


def update_index():
    p = ROOT / "index.html"
    s = p.read_text(encoding="utf8")
    s, n = re.subn(r"<!--HL:START-->.*?<!--HL:END-->", lambda m: grid_html(), s, flags=re.S)
    if n != 1:
        raise SystemExit("index.html: highlights markers not found")
    s, n = re.subn(r"<!--MAP:START-->.*?<!--MAP:END-->", lambda m: map_html(), s, flags=re.S)
    if n != 1:
        raise SystemExit("index.html: map markers not found")
    p.write_text(s, encoding="utf8")


TRIP_BODY = """
<main id="top">
  <section class="t-hero">
    <div class="container">
      <p class="a-crumbs"><a href="/">Discover Singapore</a> / Plan your trip</p>
      <p class="eyebrow light">Plan your trip · free</p>
      <h1>My Singapore trip</h1>
      <span class="rule"></span>
      <p class="lead">Pick the sights, neighbourhoods and food stops you want to see, put them in order, then download your own itinerary as a free PDF with photos and Google Maps links for every stop.</p>
    </div>
  </section>
  <div class="container trip-wrap" id="trip">
    <div>
      <ol class="trip-list" id="tripList"></ol>
      <p class="trip-note" id="tripNote"></p>
      <div class="trip-empty" id="tripEmpty" hidden>
        <h2>Your trip is empty</h2>
        <p>Browse the highlights and tap <strong>+ Add to trip</strong> on anything you want to see. Your picks are saved on this device.</p>
        <div class="btn-row"><a class="btn primary" href="/#highlights">Browse the highlights</a></div>
      </div>
      <div class="trip-suggest" id="tripSuggest" hidden>
        <h2>Popular additions</h2>
        <div class="card-grid small" id="suggestGrid"></div>
      </div>
    </div>
    <aside class="trip-panel">
      <form class="trip-box" id="tripForm" novalidate>
        <h2>Your itinerary <span class="free">Free</span></h2>
        <p>Add your name and travel dates. They are printed on your PDF and never leave your device.</p>
        <label for="tpName">Your name</label>
        <input id="tpName" name="name" type="text" autocomplete="name" maxlength="60">
        <div class="tp-dates">
          <div><label for="tpFrom">Arrival</label><input id="tpFrom" name="from" type="date"></div>
          <div><label for="tpTo">Departure</label><input id="tpTo" name="to" type="date"></div>
        </div>
        <button class="btn primary tp-go" type="submit" id="tpPdf">Download my PDF itinerary</button>
        <p class="tp-status" id="tpStatus" role="status" aria-live="polite"></p>
      </form>
      <div class="trip-box">
        <h2>Take it to Google Maps</h2>
        <p>Open all your stops as one route in Google Maps, in the order on your list.</p>
        <a class="btn outline tp-go" id="tpRoute" href="https://www.google.com/maps" target="_blank" rel="noopener">Open route in Google Maps</a>
      </div>
      <div class="trip-box dark">
        <h2>Take Singapore with you</h2>
        <p>The Discover Singapore travel guide: neighbourhoods, food and maps, coming soon.</p>
        <a class="link-arrow dark" href="/#guides">See the guides →</a>
      </div>
    </aside>
  </div>
</main>
"""

TRIP_CSS = (ROOT / "static_src" / "trip.css")
TRIP_JS = (ROOT / "static_src" / "trip.js")


def write_static():
    out = ROOT / "static"
    out.mkdir(exist_ok=True)
    (out / "trip.css").write_text(TRIP_CSS.read_text(encoding="utf8"), encoding="utf8")
    data = json.dumps(trip_data(), ensure_ascii=False, separators=(",", ":"))
    for f in ("map.css", "map.js"):
        (out / f).write_text((ROOT / "static_src" / f).read_text(encoding="utf8"), encoding="utf8")
    (out / "trip.js").write_text("window.DS_TRIP=" + data + ";\n" + TRIP_JS.read_text(encoding="utf8"), encoding="utf8")


def write_trip_page():
    import make_articles as A
    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>My Singapore Trip: Free Itinerary Planner · Discover Singapore</title>
<meta name="description" content="Build your own Singapore itinerary: pick the highlights you want to see, put them in order and download a free PDF with photos and Google Maps links.">
<link rel="canonical" href="{SITE}/trip">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Discover Singapore">
<meta property="og:title" content="My Singapore Trip: Free Itinerary Planner">
<meta property="og:description" content="Pick Singapore's highlights and download your own free PDF itinerary.">
<meta property="og:url" content="{SITE}/trip">
<meta property="og:image" content="{SITE}/assets/img/hero-skyline-night-1800.jpg">
{A.FONTS}
<link rel="stylesheet" href="/static/trip.css">
<style>{A.STYLE}{A.ARTICLE_CSS}</style>
</head>
<body class="trip-page">
{A.HEADER}
{TRIP_BODY}
{A.FOOTER}
{A.SCRIPT}
<script src="/static/trip.js" defer></script>
</body>
</html>
"""
    (ROOT / "trip.html").write_text(page, encoding="utf8")


def main():
    update_index()
    write_static()
    write_trip_page()
    print("trip planner:", len(HIGHLIGHTS), "highlights")


if __name__ == "__main__":
    main()
