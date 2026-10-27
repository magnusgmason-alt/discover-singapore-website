"""Second batch of journal articles. Images use photo slots from build.py.
fig() places a photo inside an article."""


def fig(slot, alt, caption, pos="50% 50%"):
    return (f'<figure class="a-figure"><img src="/assets/img/{slot}-1800.jpg" '
            f'srcset="/assets/img/{slot}-800.jpg 800w, /assets/img/{slot}-1800.jpg 1800w" '
            f'sizes="(min-width: 800px) 760px, 100vw" alt="{alt}" style="object-position: {pos}" '
            f'loading="lazy" decoding="async"><figcaption>{caption}</figcaption></figure>')


GBTB = "https://www.gardensbythebay.com.sg"
MBS = "https://www.marinabaysands.com"

MORE = [
    {
        "slug": "gardens-by-the-bay-guide",
        "short": "Gardens by the Bay: Tickets, Supertrees & Light Show",
        "title": "Gardens by the Bay Guide: Tickets, Supertrees, Domes and the Light Show (2027)",
        "description": "How to visit Gardens by the Bay in Singapore: what is free, Flower Dome and Cloud Forest ticket prices, OCBC Skyway, Garden Rhapsody show times, opening hours and how to get there.",
        "category": "Highlights · Marina Bay",
        "teaser": "What is free, what to book, and when to see the Supertrees light up.",
        "image": "hl-supertree-grove",
        "image_alt": "The Supertrees at Gardens by the Bay lit up at night with Marina Bay Sands behind",
        "stats": [
            ("Free", "Outdoor gardens and Supertree Grove, 5 am to 2 am"),
            ("7.45 & 8.45 pm", "Garden Rhapsody light show, every evening"),
            ("S$46", "Flower Dome & Cloud Forest, non-resident adult"),
            ("22 m", "Height of the OCBC Skyway above the ground"),
        ],
        "body": f"""
<p>Gardens by the Bay is the garden city at its most theatrical: giant steel Supertrees, two cooled glass domes and a free light show every night, all on reclaimed land beside Marina Bay. Much of it costs nothing. Here is what is free, what needs a ticket, and how to plan a visit so you see the gardens by day and the Supertrees after dark.</p>
<!--TOC-->
<h2>Is Gardens by the Bay free?</h2>
<p>Yes, the outdoor gardens are free. That includes the Supertree Grove, the Heritage Gardens, the Serene Garden, the World of Plants and the Dragonfly and Kingfisher lakes, which are open daily from 5 am to 2 am. The nightly Garden Rhapsody light show is free too.</p>
<p>You pay for the indoor and elevated attractions: the Flower Dome, the Cloud Forest, Floral Fantasy, the OCBC Skyway and the Supertree Observatory.</p>
{fig("strip-supertrees", "Supertrees covered in ferns and vines under a blue sky at Gardens by the Bay", "The Supertree Grove by day. The vertical gardens on each trunk hold more than 150,000 plants across the grove.")}

<h2>What are the Supertrees?</h2>
<p>The Supertrees are tall steel structures covered in ferns, orchids and climbing plants, with canopies that open out like trees. They collect rainwater, vent air from the conservatories and light up at night. Most stand in the Supertree Grove, the heart of the gardens, where you can walk among them for free.</p>

<h2>How much are the Flower Dome and Cloud Forest?</h2>
<p>For visitors from overseas, a combined ticket for the Flower Dome and the Cloud Forest costs S$46 for adults and S$32 for children aged 3 to 12, according to Gardens by the Bay. Singapore residents pay less. Bundles that add Floral Fantasy and a shuttle cost more.</p>
<ul>
<li><strong>Flower Dome:</strong> a huge glass conservatory kept cool and dry, with plants from the Mediterranean and other semi-arid regions and a central field of seasonal flower displays.</li>
<li><strong>Cloud Forest:</strong> a cool, misty dome built around an indoor mountain covered in plants, with walkways that climb to the top and a tall indoor waterfall. It currently features Jurassic World: The Experience.</li>
</ul>
<p>Both domes open daily from 9 am to 9 pm. Last admission is 8.30 pm for the Flower Dome and 8 pm for the Cloud Forest, and each closes once a month for maintenance, so check the closure dates before you go. Allow about two hours for both.</p>

<h2>Is the OCBC Skyway worth it?</h2>
<p>If you like a view, yes. The Skyway is a 128-metre walkway suspended 22 metres above the ground between two Supertrees, with views across the gardens to Marina Bay Sands. A visit takes about 15 minutes. Non-resident tickets cost S$14 for adults and S$10 for children.</p>
<p>It opens from 9 am to 9 pm, with last admission at 8.30 pm, and can close in bad weather or on maintenance days. For a higher view of the grove, the Supertree Observatory sits on top of the tallest Supertree and keeps the same hours.</p>
{fig("hl-skyway", "The OCBC Skyway walkway curving between Supertrees above the gardens", "The OCBC Skyway, strung between two Supertrees 22 metres above the gardens.")}

<h2>When is the Garden Rhapsody light show?</h2>
<p>Garden Rhapsody runs every evening at 7.45 pm and 8.45 pm at the Supertree Grove, and it is free. The Supertrees light up and change colour in time with music, and the soundtrack changes through the year with themes such as Chinese New Year and National Day.</p>
<p>Arrive 15 minutes early, find a spot on the plaza or the benches under the trees, and look up. Some visitors lie on the ground for the best view. During special ticketed events, such as the Christmas Wonderland season, entry to the grove may be charged.</p>

<h2>How long do you need at Gardens by the Bay?</h2>
<p>Plan for half a day. A good plan is to arrive in the late afternoon, visit the two domes while it is hot, walk the Skyway before sunset, then stay for the 7.45 pm Garden Rhapsody. If you only want the free gardens and the show, two hours in the evening is enough.</p>

<h2>How do you get to Gardens by the Bay?</h2>
<p>The easiest way is the Thomson-East Coast Line to Gardens by the Bay station, which opens right by the gardens. You can also take the Circle or Downtown line to Bayfront station and walk through the underpass and across the bridge from Marina Bay Sands, about 10 minutes. Taxis and ride-hailing cars drop off at the main entrance on Marina Gardens Drive.</p>
{fig("hl-marina-barrage", "Aerial view of the two glass conservatories at Gardens by the Bay beside the water, with Marina Barrage and ships offshore", "The Flower Dome and Cloud Forest from above, with Marina Barrage and the strait beyond.")}

<h2>What else is nearby?</h2>
<p>Marina Bay Sands, the ArtScience Museum and the Spectra light and water show are a short walk across the bridge. On a clear evening, walk east to Marina Barrage for sunset over the skyline. Read our guide to <a href="/blog/things-to-do-in-marina-bay">things to do in Marina Bay</a> to plan the rest of the day, and see <a href="/blog/free-things-to-do-in-singapore">free things to do in Singapore</a> for more that costs nothing.</p>
""",
        "checked_note": "Facts checked October 2026. Prices are non-resident rates in Singapore dollars. Opening hours, show times and ticket prices are set by Gardens by the Bay and can change; check the official site before you go.",
        "sources": [
            ("Opening Hours & Closures (Gardens by the Bay)", f"{GBTB}/en/plan-your-visit/opening-hours.html"),
            ("Flower Dome (Gardens by the Bay)", f"{GBTB}/en/things-to-do/attractions/flower-dome.html"),
            ("OCBC Skyway (Gardens by the Bay)", f"{GBTB}/en/things-to-do/attractions/ocbc-skyway.html"),
            ("Garden Rhapsody (Gardens by the Bay)", f"{GBTB}/en/things-to-do/calendar-of-events/garden-rhapsody.html"),
        ],
    },
    {
        "slug": "things-to-do-in-marina-bay",
        "short": "Things to Do in Marina Bay: Day and Night",
        "title": "Things to Do in Marina Bay, Singapore: Sights, Views and Free Shows (2027)",
        "description": "The best things to do in Marina Bay, Singapore: Marina Bay Sands SkyPark, the Merlion, the ArtScience Museum, the Helix Bridge, Singapore Flyer and the free Spectra show, with times and tips.",
        "category": "Highlights · Marina Bay",
        "teaser": "The skyline, the Merlion and the free shows, with times and tips.",
        "image": "hl-marina-bay-sands",
        "image_alt": "Marina Bay Sands lit red at night with the lotus-shaped ArtScience Museum in front",
        "stats": [
            ("Level 56", "SkyPark Observation Deck, Marina Bay Sands"),
            ("S$35", "SkyPark off-peak adult ticket"),
            ("Free", "Spectra light & water show, every evening"),
            ("8.6 m", "Height of the Merlion statue"),
        ],
        "body": f"""
<p>Marina Bay is the Singapore of postcards: Marina Bay Sands with its ship-shaped SkyPark, the Merlion, the lotus-shaped ArtScience Museum and the Esplanade's spiky domes, all around one calm bay. Most of it is free to walk around, and the best of it happens after dark. Here is what to do, in the order a day here usually flows.</p>
<!--TOC-->
<h2>What is the best way to see Marina Bay?</h2>
<p>On foot. A promenade of about 3.5 km loops around the bay, linking the Merlion, the Esplanade, the Helix Bridge and Marina Bay Sands, with views in every direction. Start in the late afternoon, catch sunset from a viewpoint, and finish with the evening light shows.</p>

<h2>Is the Marina Bay Sands SkyPark worth it?</h2>
<p>For the view, yes. The SkyPark Observation Deck is on level 56 of Hotel Tower 3 and looks over the bay, the city, Gardens by the Bay and the ships in the strait. Marina Bay Sands lists off-peak hours from 9.30 am to 4.30 pm, with an adult ticket of S$35, and peak hours from 5 pm to 10 pm, with last entry at 9.30 pm.</p>
<p>Sunset slots sell out first, so book online. The famous rooftop infinity pool is for hotel guests only; the observation deck is the public way up. From the deck at night you also look down on the Spectra show.</p>

<h2>When is the Spectra light and water show?</h2>
<p>Spectra is a free 15-minute outdoor show of fountains, lights, lasers and music on the water at the Event Plaza in front of Marina Bay Sands. It runs every evening at 8 pm and 9 pm from Sunday to Thursday, with an extra 10 pm show on Fridays and Saturdays.</p>
<p>Watch from the steps of the Event Plaza for the full effect, or from the Merlion side of the bay for the skyline behind it.</p>
{fig("hl-night-lights", "Glowing pink egg-shaped lights on the water beneath the three towers of Marina Bay Sands at night", "Marina Bay Sands after dark, when the bay fills with light shows and night walkers.", "50% 60%")}

<h2>Where is the Merlion?</h2>
<p>The Merlion stands in Merlion Park beside One Fullerton, at the mouth of the Singapore River. The 8.6-metre statue, half lion and half fish, spouts water into the bay with Marina Bay Sands directly across the water, which makes it the classic photo spot. It is busy all day; early morning and late evening are calmest.</p>
{fig("hl-merlion", "The Merlion statue lit gold at night, spouting water towards the bay", "The Merlion at night, spouting water into Marina Bay.", "30% 60%")}

<h2>What is inside the ArtScience Museum?</h2>
<p>The lotus-shaped museum at Marina Bay Sands hosts changing exhibitions where art meets science and technology, plus Future World, a permanent space of interactive digital art that is popular with children. The building, designed by architect Moshe Safdie, is worth seeing from outside even if you skip the exhibitions.</p>
{fig("hl-artscience", "The white lotus-shaped ArtScience Museum under a bright blue sky with palm trees in front", "The ArtScience Museum, the lotus on the bay.", "50% 45%")}

<h2>Is the Singapore Flyer worth it?</h2>
<p>The Singapore Flyer is a 165-metre observation wheel on the east side of the bay. One rotation takes about 30 minutes and gives a slower, wider view than the SkyPark, including the gardens, the Formula 1 circuit and the anchored ships. It suits families and anyone who prefers a seat to standing on a deck.</p>

<h2>What else is there to do around Marina Bay?</h2>
<ul>
<li><strong>Helix Bridge:</strong> a curving pedestrian bridge inspired by the shape of DNA, lit up at night, linking the Esplanade side to Marina Bay Sands.</li>
<li><strong>Esplanade – Theatres on the Bay:</strong> the spiky "durian" domes host concerts and often free outdoor performances by the water.</li>
<li><strong>Gardens by the Bay:</strong> behind Marina Bay Sands, with the free Garden Rhapsody show at 7.45 pm and 8.45 pm. See our <a href="/blog/gardens-by-the-bay-guide">Gardens by the Bay guide</a>.</li>
<li><strong>Marina Barrage:</strong> a grassy rooftop on the dam, east of the gardens, for picnics and sunset views of the skyline.</li>
<li><strong>Lau Pa Sat:</strong> a Victorian market hall a short walk from the bay, with satay grills on the street outside in the evening.</li>
</ul>

<h2>How do you get to Marina Bay?</h2>
<p>Bayfront station, on the Circle and Downtown lines, opens into Marina Bay Sands. Marina Bay station serves the North-South, Circle and Thomson-East Coast lines, and Raffles Place station on the North-South and East-West lines is closest to the Merlion. See <a href="/blog/getting-around-singapore">getting around Singapore</a> for paying with a contactless card.</p>
""",
        "checked_note": "Facts checked October 2026. Opening hours, show times and ticket prices are set by each attraction and can change; check before you go.",
        "sources": [
            ("SkyPark Observation Deck (Marina Bay Sands)", f"{MBS}/attractions/skypark-observation-deck.html"),
            ("Spectra – A Light & Water Show (Marina Bay Sands)", f"{MBS}/attractions/spectra.html"),
            ("Garden Rhapsody (Gardens by the Bay)", f"{GBTB}/en/things-to-do/calendar-of-events/garden-rhapsody.html"),
        ],
    },
    {
        "slug": "free-things-to-do-in-singapore",
        "short": "Free Things to Do in Singapore",
        "title": "Free Things to Do in Singapore: Light Shows, Gardens and Views (2027)",
        "description": "The best free things to do in Singapore: the Garden Rhapsody and Spectra light shows, Gardens by the Bay's outdoor gardens, the Merlion, Jewel's Rain Vortex, the Botanic Gardens and more, with times.",
        "category": "Planning · Budget",
        "teaser": "Light shows, gardens and views that cost nothing.",
        "image": "hl-supertrees-above",
        "image_alt": "Three Supertrees lit purple and red, seen from above at night",
        "stats": [
            ("3", "Free nightly light shows: Supertrees, Spectra and Jewel"),
            ("5 am–2 am", "Gardens by the Bay outdoor gardens, free"),
            ("40 m", "Jewel's Rain Vortex, the world's tallest indoor waterfall"),
        ],
        "body": f"""
<p>Singapore has a reputation for being expensive, but many of its best experiences cost nothing. Three light shows run free every night, the gardens that made the city famous are open to everyone, and the views are free from the waterfront. Here are the best free things to do, with times so you can plan your evenings.</p>
<!--TOC-->
<h2>What are the best free things to do in Singapore?</h2>
<ul>
<li>Watch Garden Rhapsody at the Supertree Grove (7.45 pm and 8.45 pm).</li>
<li>Watch the Spectra light and water show at Marina Bay Sands (from 8 pm).</li>
<li>Walk the outdoor gardens at Gardens by the Bay (5 am to 2 am).</li>
<li>See the Merlion and walk the Marina Bay promenade.</li>
<li>Visit the Rain Vortex at Jewel Changi Airport, with its own evening light show.</li>
<li>Explore the Singapore Botanic Gardens, a UNESCO World Heritage Site.</li>
<li>Picnic and watch the sunset on the roof of Marina Barrage.</li>
<li>Walk the Southern Ridges and the Henderson Waves bridge.</li>
</ul>

<h2>Which light shows are free in Singapore?</h2>
<p>Three, and you can see two in one evening at Marina Bay:</p>
<div class="table-wrap"><table>
<thead><tr><th>Show</th><th>Where</th><th>Times</th></tr></thead>
<tbody>
<tr><td>Garden Rhapsody</td><td>Supertree Grove, Gardens by the Bay</td><td>Daily, 7.45 pm and 8.45 pm</td></tr>
<tr><td>Spectra</td><td>Event Plaza, Marina Bay Sands</td><td>Sun–Thu 8 pm and 9 pm; Fri–Sat 8, 9 and 10 pm</td></tr>
<tr><td>Rain Vortex Light &amp; Music Showcase</td><td>Jewel Changi Airport</td><td>Mon–Thu 8 pm and 9 pm; Fri–Sun, public holidays and eves 8, 9 and 10 pm</td></tr>
</tbody></table></div>
<p>To see two shows in one night, watch Garden Rhapsody at 7.45 pm, then walk across the bridge to Marina Bay Sands for the 9 pm Spectra, about 15 minutes away.</p>
{fig("hl-night-lights", "Glowing pink lights on the water below Marina Bay Sands at night", "Marina Bay Sands at night, home of the free Spectra show.", "50% 60%")}

<h2>What is free at Gardens by the Bay?</h2>
<p>All the outdoor gardens, including the Supertree Grove, are free and open from 5 am to 2 am. Only the domes, Floral Fantasy, the OCBC Skyway and the Supertree Observatory charge entry. Our <a href="/blog/gardens-by-the-bay-guide">Gardens by the Bay guide</a> has the details.</p>

<h2>Can you visit Jewel Changi for free?</h2>
<p>Yes. Jewel sits on the public side of Changi Airport, so you do not need a flight to visit. The Rain Vortex, a 40-metre indoor waterfall that falls seven storeys through a glass dome, runs from 10 am to 10 pm, and the forest valley around it is free to walk. Only Canopy Park on the top level charges entry. Read our <a href="/blog/jewel-changi-guide">Jewel Changi guide</a>.</p>
{fig("strip-jewel", "The Rain Vortex waterfall falling through the glass dome of Jewel Changi, surrounded by trees", "Jewel's Rain Vortex, free to visit from 10 am to 10 pm.", "50% 40%")}

<h2>Is the Singapore Botanic Gardens free?</h2>
<p>Yes, entry is free. The gardens became Singapore's first UNESCO World Heritage Site in 2015 and include lakes, a patch of original rainforest and lawns that host free concerts on some weekends. Only the National Orchid Garden inside charges an entrance fee. Go early in the morning, before the heat.</p>

<h2>Where can you see Singapore's skyline for free?</h2>
<ul>
<li><strong>Merlion Park:</strong> the classic view across the bay to Marina Bay Sands.</li>
<li><strong>Marina Bay promenade:</strong> a loop of about 3.5 km around the bay, best after dark.</li>
<li><strong>Marina Barrage:</strong> a grassy rooftop with the whole skyline across the water at sunset.</li>
<li><strong>Helix Bridge:</strong> lit up at night, with views of the bay in both directions.</li>
</ul>
{fig("guide-bay-day", "Marina Bay Sands and the garden domes seen across the water from Marina Barrage, with flowers in front", "The skyline from Marina Barrage, one of the best free viewpoints.", "50% 60%")}

<h2>What other free things can you do in Singapore?</h2>
<ul>
<li><strong>Southern Ridges:</strong> trails and walkways linking hilltop parks, with Henderson Waves, a wave-shaped wooden bridge high above the forest.</li>
<li><strong>Chinatown temples:</strong> the Buddha Tooth Relic Temple and the Sri Mariamman Temple welcome visitors; dress modestly.</li>
<li><strong>Kampong Glam and Haji Lane:</strong> street art, Sultan Mosque and shophouse lanes to wander.</li>
<li><strong>Esplanade:</strong> the arts centre on the bay often hosts free outdoor performances.</li>
</ul>

<h2>How can you keep a trip to Singapore cheap?</h2>
<ul>
<li>Eat at hawker centres, where a meal usually costs a fraction of a restaurant.</li>
<li>Drink tap water, which is safe, and refill a bottle.</li>
<li>Tap a contactless bank card on the MRT instead of buying passes; see <a href="/blog/getting-around-singapore">getting around Singapore</a>.</li>
<li>Plan your evenings around the free light shows.</li>
</ul>
""",
        "checked_note": "Facts checked October 2026. Show times and opening hours are set by each venue and can change, especially on public holidays and during special events; check before you go.",
        "sources": [
            ("Garden Rhapsody (Gardens by the Bay)", f"{GBTB}/en/things-to-do/calendar-of-events/garden-rhapsody.html"),
            ("Opening Hours & Closures (Gardens by the Bay)", f"{GBTB}/en/plan-your-visit/opening-hours.html"),
            ("Spectra – A Light & Water Show (Marina Bay Sands)", f"{MBS}/attractions/spectra.html"),
            ("Jewel Rain Vortex (Jewel Changi Airport)", "https://www.jewelchangiairport.com/en/attractions/rain-vortex.html"),
        ],
    },
    {
        "slug": "jewel-changi-guide",
        "short": "Jewel Changi: Rain Vortex, Light Show & Layovers",
        "title": "Jewel Changi Airport Guide: Rain Vortex, Light Show Times and Layover Tips (2027)",
        "description": "How to visit Jewel Changi Airport: Rain Vortex opening hours, the light and music show times, Canopy Park, how to get there from each terminal and whether you can visit on a layover.",
        "category": "Highlights · Changi",
        "teaser": "The Rain Vortex, show times and how to fit it into a layover.",
        "image": "hl-jewel",
        "image_alt": "The Rain Vortex falling through the glass dome of Jewel Changi into a pool surrounded by trees",
        "stats": [
            ("40 m", "Rain Vortex, the world's tallest indoor waterfall"),
            ("10 am–10 pm", "Rain Vortex running hours, daily"),
            ("Free", "Entry to Jewel and the forest valley"),
        ],
        "body": f"""
<p>Jewel is the reason many travellers now arrive at Changi early. Under a glass and steel dome beside Terminal 1, a waterfall pours seven storeys through a terraced forest, surrounded by shops and restaurants. It is free to visit, open to anyone, and easy to fit in on arrival, before a flight or on a layover.</p>
<!--TOC-->
<h2>What is Jewel Changi Airport?</h2>
<p>Jewel is a nature-themed complex at Changi Airport, built around the Rain Vortex, which Jewel describes as the world's tallest indoor waterfall. Around it are a terraced indoor forest, Canopy Park on the top level, and several floors of shops, cafés and restaurants. It sits on the public side of the airport, before immigration, so you do not need a boarding pass to visit.</p>

<h2>When does the Rain Vortex run?</h2>
<p>The Rain Vortex runs daily from 10 am to 10 pm. Water falls 40 metres from an opening in the roof into a pool in the basement. By day, sunlight catches the spray; after dark it becomes the screen for a light and music show.</p>

<h2>What time is the Jewel light show?</h2>
<p>The Light &amp; Music Showcase on the Rain Vortex runs at 8 pm and 9 pm from Monday to Thursday, and at 8 pm, 9 pm and 10 pm from Friday to Sunday, on public holidays and on the eve of public holidays. It is free. Good viewing spots are the lower levels facing the waterfall and the walkways around the forest valley.</p>
{fig("strip-jewel", "The Rain Vortex seen from above, falling into a pool ringed by trees and walkways inside Jewel", "Looking down on the Rain Vortex from the forest valley terraces.", "50% 45%")}

<h2>What is there to do at Jewel besides the waterfall?</h2>
<ul>
<li><strong>Forest valley:</strong> terraced gardens with walking trails around the waterfall, free to explore.</li>
<li><strong>Canopy Park:</strong> the ticketed top level, with walking and bouncing nets strung among the trees, hedge and mirror mazes, and a glass-floored bridge with views of the Rain Vortex.</li>
<li><strong>Food and shopping:</strong> several floors of restaurants, cafés and shops, open to everyone.</li>
</ul>

<h2>How do you get to Jewel from each terminal?</h2>
<p>Jewel connects directly to Terminal 1 and is linked to Terminals 2 and 3 by walkways on the public side, a few minutes on foot. From Terminal 4, take the free shuttle bus to Terminal 2 and walk from there. From the city, take the MRT to Changi Airport station, which sits between Terminals 2 and 3, and follow the signs to Jewel.</p>

<h2>Can you visit Jewel on a layover?</h2>
<p>Only if you can leave the transit area. Jewel is on the public side of the airport, so transit passengers must pass through immigration to reach it and go back through security afterwards. Check whether your passport lets you enter Singapore, submit the free SG Arrival Card before you land, and allow plenty of time to return. On a short connection, stay airside: Changi's terminals have their own gardens and free attractions.</p>

<h2>When is the best time to visit Jewel?</h2>
<p>Weekday mornings are quietest. For the light show, arrive by 7.45 pm and stay for the 8 pm performance; weekend evenings and public holidays are busiest. If you are flying out, visit before you check in or drop your bags, then head to your terminal.</p>
<p>For the rest of your arrival, read <a href="/blog/getting-around-singapore">getting around Singapore</a>, and see <a href="/blog/free-things-to-do-in-singapore">free things to do in Singapore</a> for more free sights.</p>
""",
        "checked_note": "Facts checked October 2026. Running hours and show times are set by Jewel Changi Airport and can change; check the official site before you go.",
        "sources": [
            ("Jewel Rain Vortex (Jewel Changi Airport)", "https://www.jewelchangiairport.com/en/attractions/rain-vortex.html"),
            ("Attractions (Jewel Changi Airport)", "https://www.jewelchangiairport.com/en/attractions.html"),
            ("Leaving the airport (Changi Airport)", "https://www.changiairport.com/en/airport-guide/transport/leaving-the-airport.html"),
            ("SG Arrival Card (Immigration & Checkpoints Authority)", "https://www.ica.gov.sg/enter-depart/arriving/overview/sg-arrival-card"),
        ],
    },
    {
        "slug": "singapore-at-night",
        "short": "Singapore at Night: Light Shows, Views & Night Walks",
        "title": "Singapore at Night: Light Shows, Skyline Views and the Best Night Walks (2027)",
        "description": "The best things to do in Singapore at night: free light shows with times, skyline viewpoints, the Marina Bay night walk, hawker suppers, the Night Safari and riverside bars.",
        "category": "Highlights · Nightlife",
        "teaser": "Free shows, skyline views and where to eat after dark.",
        "image": "hero-skyline-night",
        "image_alt": "The Singapore skyline lit up at night, with colourful reflections across Marina Bay",
        "stats": [
            ("7.45 pm", "First Garden Rhapsody show at the Supertrees"),
            ("8 pm", "First Spectra show at Marina Bay Sands"),
            ("10 pm", "SkyPark Observation Deck closes; last entry 9.30 pm"),
        ],
        "body": f"""
<p>Singapore comes alive after dark. The heat eases, the skyline lights up, and the city puts on free shows over the water every evening. Here is how to spend a night in Singapore, from the light shows and the best viewpoints to supper at a hawker centre.</p>
<!--TOC-->
<h2>What is the best thing to do in Singapore at night?</h2>
<p>Spend an evening at Marina Bay. Watch Garden Rhapsody at the Supertree Grove at 7.45 pm, walk across the bridge for the 9 pm Spectra show at Marina Bay Sands, then walk around the bay past the Helix Bridge and the Merlion with the skyline lit up across the water. All of it is free.</p>
{fig("editions-supertree-night", "Close-up of a plant-covered Supertree lit white and red at night", "A Supertree lit up for Garden Rhapsody.", "50% 35%")}

<h2>What time are the light shows?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Show</th><th>Where</th><th>Times</th></tr></thead>
<tbody>
<tr><td>Garden Rhapsody</td><td>Supertree Grove, Gardens by the Bay</td><td>Daily, 7.45 pm and 8.45 pm</td></tr>
<tr><td>Spectra</td><td>Event Plaza, Marina Bay Sands</td><td>Sun–Thu 8 pm and 9 pm; Fri–Sat 8, 9 and 10 pm</td></tr>
<tr><td>Rain Vortex show</td><td>Jewel Changi Airport</td><td>Mon–Thu 8 pm and 9 pm; Fri–Sun and public holidays 8, 9 and 10 pm</td></tr>
</tbody></table></div>
<p>All three are free. Shows can be cancelled in heavy rain or lightning, and the Supertree Grove may charge entry during special ticketed events.</p>

<h2>Where are the best night views of the skyline?</h2>
<ul>
<li><strong>SkyPark Observation Deck:</strong> level 56 of Marina Bay Sands, open until 10 pm with last entry at 9.30 pm. Peak evening slots cost more, so book ahead.</li>
<li><strong>Merlion Park:</strong> the classic free view of Marina Bay Sands across the water.</li>
<li><strong>The Helix Bridge:</strong> lit up at night, with views of the bay and the city.</li>
<li><strong>Marina Barrage:</strong> the skyline from across the water, quieter than the bay itself.</li>
<li><strong>Rooftop bars:</strong> the city has many; check dress codes and expect to pay for drinks.</li>
</ul>
{fig("checklist-mbs-night", "Marina Bay Sands and the ArtScience Museum lit up at night across the dark water of the bay", "Marina Bay Sands and the ArtScience Museum from across the bay after dark.", "50% 65%")}

<h2>Where should you eat in Singapore at night?</h2>
<p>At a hawker centre. Lau Pa Sat, the Victorian market hall in the financial district, is the best-known evening stop: Boon Tat Street beside it fills with satay grills after dark. Many neighbourhood hawker centres stay busy into the evening too, and late-night supper is a Singapore tradition.</p>

<h2>Where is the nightlife in Singapore?</h2>
<ul>
<li><strong>Clarke Quay:</strong> riverside bars, clubs and restaurants in restored warehouses, busy late.</li>
<li><strong>Robertson Quay:</strong> calmer riverside bars and restaurants upstream.</li>
<li><strong>Haji Lane and Kampong Glam:</strong> small bars in painted shophouses.</li>
<li><strong>Duxton and Keong Saik roads:</strong> cocktail bars and restaurants in Tanjong Pagar.</li>
</ul>
<p>Drinks are expensive in Singapore because of high alcohol taxes, so look out for happy hours.</p>

<h2>Is the Night Safari worth it?</h2>
<p>For families and animal lovers, yes. The Night Safari in Mandai, in the north of the island, opens in the evening so you can see nocturnal animals by tram and on walking trails. It is ticketed and popular, so book ahead and allow time to get there and back from the city.</p>

<h2>Is Singapore safe at night?</h2>
<p>Singapore is one of the safest cities in the world to walk around at night, and the MRT runs until around midnight. Usual care still applies: watch your belongings in crowds, and take a taxi or ride-hailing car if you are out after the trains stop. In an emergency, call 999 for police or 995 for an ambulance or fire.</p>
{fig("hl-bayfront-night", "Marina Bay Sands seen between two lit bridges, reflected in the water at night", "The bayfront after dark, on the loop walk around Marina Bay.", "50% 55%")}
<p>For the full day plan, read <a href="/blog/things-to-do-in-marina-bay">things to do in Marina Bay</a> and <a href="/blog/free-things-to-do-in-singapore">free things to do in Singapore</a>.</p>
""",
        "checked_note": "Facts checked October 2026. Show times, opening hours and prices are set by each venue and can change; check before you go.",
        "sources": [
            ("Garden Rhapsody (Gardens by the Bay)", f"{GBTB}/en/things-to-do/calendar-of-events/garden-rhapsody.html"),
            ("Spectra – A Light & Water Show (Marina Bay Sands)", f"{MBS}/attractions/spectra.html"),
            ("SkyPark Observation Deck (Marina Bay Sands)", f"{MBS}/attractions/skypark-observation-deck.html"),
            ("Jewel Rain Vortex (Jewel Changi Airport)", "https://www.jewelchangiairport.com/en/attractions/rain-vortex.html"),
        ],
    },
]

# Photos to add inside the first three articles: (slug, heading to insert before, figure)
EXTRA_FIGS = [
    ("best-time-to-visit-singapore", "<h2>When is the rainy season in Singapore?</h2>",
     fig("strip-marina-bay-day", "Marina Bay Sands and the garden domes under a grey sky", "A typical cloudy afternoon over Marina Bay. Storms usually pass within an hour or two.", "50% 60%")),
    ("best-time-to-visit-singapore", "<h2>Is there haze in Singapore, and when?</h2>",
     fig("quiet-dusk", "Heavy clouds at dusk over the Singapore skyline and the waterfront", "Storm clouds at dusk over the city. Afternoon and evening thunderstorms are common between monsoons.", "50% 40%")),
    ("where-to-stay-in-singapore", "<h2>What is the Civic District like?</h2>",
     fig("hl-marina-bay-sands", "Marina Bay Sands lit red at night with the ArtScience Museum in front", "Marina Bay Sands, the landmark of Singapore's priciest hotel district.", "50% 55%")),
    ("where-to-stay-in-singapore", "<h2>Is Clarke Quay or Robertson Quay better?</h2>",
     fig("hl-fullerton", "The Fullerton Hotel and the financial district reflected in the bay at sunset", "The Fullerton Hotel at the mouth of the Singapore River, a short walk from Clarke Quay.", "50% 55%")),
    ("getting-around-singapore", "<h2>How do you get from Changi Airport to the city?</h2>",
     fig("hl-jewel", "The Rain Vortex inside Jewel Changi Airport", "Jewel at Changi Airport, on the public side of the terminals, worth a stop on arrival.", "50% 45%")),
    ("getting-around-singapore", "<h2>Should you take a taxi or a Grab in Singapore?</h2>",
     fig("hl-bayfront-night", "Marina Bay Sands seen between two road bridges at night", "Marina Bay's bridges at night. Taxis add surcharges after midnight.", "50% 55%")),
]
