"""Third batch of journal articles."""
from articles_more import fig, GBTB, MBS

ICA = "https://www.ica.gov.sg"
CHANGI = "https://www.changiairport.com"

BATCH3 = [
    {
        "slug": "singapore-itinerary-3-days",
        "short": "Singapore in 3 Days: A First-Timer's Itinerary",
        "title": "3 Days in Singapore: The Perfect First-Time Itinerary (2027)",
        "description": "A 3-day Singapore itinerary for first-timers: Marina Bay and Gardens by the Bay, Chinatown and Kampong Glam, the Botanic Gardens and Little India, with times for the free light shows and where to eat.",
        "category": "Planning · Itinerary",
        "teaser": "Marina Bay, the heritage quarters and the gardens, day by day.",
        "image": "guide-bay-day",
        "image_alt": "Marina Bay Sands and the garden domes across the water on a bright day",
        "stats": [
            ("3", "Days, each built around one part of the city"),
            ("2", "Free light shows on the first evening"),
            ("1", "Contactless card for every train and bus"),
        ],
        "body": f"""
<p>Three days is enough to see the best of Singapore without rushing. The city is compact, the trains are fast and the sights cluster neatly into neighbourhoods, so each day below stays in one part of town. Plan outdoor sights for the morning and evening, and keep the hottest hours for museums, malls and long lunches.</p>
<!--TOC-->
<h2>How should you plan 3 days in Singapore?</h2>
<ul>
<li><strong>Day 1:</strong> Marina Bay, Gardens by the Bay and the free evening light shows.</li>
<li><strong>Day 2:</strong> Chinatown, the Singapore River and Kampong Glam.</li>
<li><strong>Day 3:</strong> The Botanic Gardens, Little India and an easy last afternoon.</li>
</ul>
<p>Stay somewhere central with an MRT station nearby, such as Marina Bay, the Civic District, Chinatown or along the river. Our guide to <a href="/blog/where-to-stay-in-singapore">where to stay in Singapore</a> compares the areas.</p>

<h2>Day 1: Marina Bay and Gardens by the Bay</h2>
<p><strong>Morning:</strong> Start at the Merlion for the classic view across the bay, then walk the waterfront past the Fullerton Hotel and the Esplanade's spiky domes to the Helix Bridge.</p>
<p><strong>Afternoon:</strong> Escape the heat inside the cooled Flower Dome and Cloud Forest at Gardens by the Bay, then walk the OCBC Skyway between the Supertrees before sunset.</p>
<p><strong>Evening:</strong> Stay for Garden Rhapsody at the Supertree Grove at 7.45 pm, walk over to Marina Bay Sands for the 9 pm Spectra show on the water, and finish with satay at Lau Pa Sat. Both shows are free. Read our <a href="/blog/gardens-by-the-bay-guide">Gardens by the Bay guide</a> for tickets and times.</p>
{fig("hl-supertree-grove", "The Supertrees lit up at night with Marina Bay Sands behind", "Garden Rhapsody at the Supertree Grove, the best free show in town.", "50% 50%")}

<h2>Day 2: Chinatown, the river and Kampong Glam</h2>
<p><strong>Morning:</strong> Explore Chinatown before it gets hot. Visit the Buddha Tooth Relic Temple, the Sri Mariamman Temple and Thian Hock Keng, one of Singapore's oldest Chinese temples, then have an early lunch at Maxwell Food Centre.</p>
<p><strong>Afternoon:</strong> Follow the Singapore River past Boat Quay to the Asian Civilisations Museum or the National Gallery, both cool places to spend the hottest hours.</p>
<p><strong>Evening:</strong> Take the MRT to Bugis and wander Kampong Glam, with the golden dome of Sultan Mosque, the shophouses of Arab Street and the bars of Haji Lane. Dress modestly to visit the mosque.</p>
{fig("journal-shophouses", "Rows of shophouses with city towers rising behind them at night", "Old shophouses and new towers side by side, the story of Singapore in one view.", "50% 60%")}

<h2>Day 3: The Botanic Gardens, Little India and a last afternoon</h2>
<p><strong>Morning:</strong> Go early to the Singapore Botanic Gardens, a UNESCO World Heritage Site that is free to enter. Walk the rainforest trail and the lakes; the National Orchid Garden inside charges a small fee.</p>
<p><strong>Lunch:</strong> Head to Little India for biryani or a banana-leaf meal around Serangoon Road and Tekka Centre, and browse the spice shops and flower-garland stalls.</p>
<p><strong>Afternoon:</strong> Choose between a trip to Sentosa for the beaches, a shopping walk on Orchard Road, or the observation deck at Marina Bay Sands for one last view. If you fly out tonight, leave time to see the Rain Vortex at <a href="/blog/jewel-changi-guide">Jewel Changi</a> before check-in.</p>
{fig("hl-jewel", "The Rain Vortex falling through the glass dome of Jewel Changi", "Jewel's Rain Vortex: easy to see on your way home.", "50% 45%")}

<h2>How do you get around on this itinerary?</h2>
<p>Tap a contactless bank card or phone at the MRT gates and on buses; there is no need to buy a ticket. Every stop on this itinerary is close to an MRT station, and taxis or ride-hailing cars are easy for the evenings. See <a href="/blog/getting-around-singapore">getting around Singapore</a>.</p>

<h2>What if you have more or less time?</h2>
<ul>
<li><strong>One day:</strong> do Day 1, adding Chinatown for lunch.</li>
<li><strong>Five days:</strong> add a nature day at MacRitchie or Bukit Timah, an evening at the Night Safari, and a morning cycling on Pulau Ubin.</li>
<li><strong>A stopover:</strong> see our <a href="/blog/singapore-stopover-guide">Singapore stopover guide</a>.</li>
</ul>
<p>Want your own version? Add places from the <a href="/#highlights">highlights</a> or the <a href="/#map">map</a> to your trip, then download a free PDF itinerary from <a href="/trip">My trip</a>.</p>
""",
        "checked_note": "Facts checked October 2026. Show times and opening hours change, so check each place before you go.",
        "sources": [
            ("Garden Rhapsody (Gardens by the Bay)", f"{GBTB}/en/things-to-do/calendar-of-events/garden-rhapsody.html"),
            ("Spectra – A Light & Water Show (Marina Bay Sands)", f"{MBS}/attractions/spectra.html"),
            ("Opening Hours & Closures (Gardens by the Bay)", f"{GBTB}/en/plan-your-visit/opening-hours.html"),
        ],
    },
    {
        "slug": "singapore-travel-tips",
        "short": "Singapore Travel Tips: Rules, Money & Arrival",
        "title": "Singapore Travel Tips for First-Timers: Rules, Money and Arrival (2027)",
        "description": "Essential Singapore travel tips: the SG Arrival Card, laws visitors should know (vapes, gum, eating on the MRT), tipping and service charges, GST refunds, plugs, tap water, weather and etiquette.",
        "category": "Planning · Essentials",
        "teaser": "The arrival card, the rules, tipping, money and plugs.",
        "image": "nomad-cbd-night",
        "image_alt": "The Singapore financial district lit up at night",
        "stats": [
            ("3 days", "Window to submit the free SG Arrival Card before arrival"),
            ("S$100", "Minimum spend per retailer for a GST refund"),
            ("9%", "Goods and services tax on most prices"),
            ("Type G", "Plug sockets, the three-pin British type"),
        ],
        "body": f"""
<p>Singapore is one of the easiest cities in Asia to visit: it is safe, clean, English-speaking and well organised. A few local rules and habits are worth knowing before you land, from the arrival card you must fill in online to the things you cannot do on a train.</p>
<!--TOC-->
<h2>Do you need to fill in an arrival card for Singapore?</h2>
<p>Yes. All travellers entering Singapore must submit the SG Arrival Card, with an electronic health declaration, before they arrive. You can submit it in the three days before arrival, counting the day you arrive, through the official ICA website or the free MyICA Mobile app. It is free; ignore websites that charge a fee to submit it for you.</p>
<p>Passengers transferring at Changi without passing through immigration do not need to submit it. Whether you need a visa depends on your passport, so check the ICA visa requirements before you book.</p>

<h2>What are the rules visitors should know?</h2>
<ul>
<li><strong>Vapes are illegal.</strong> Using, buying or possessing e-cigarettes is against the law, and since September 2025 penalties have been stricter, including fines and, for foreigners in serious cases, deportation. Leave vapes at home or bin them at the airport.</li>
<li><strong>No eating or drinking on the MRT</strong> or in paid areas of stations, not even water. Fines can reach S$500.</li>
<li><strong>No durians on trains and buses</strong>, because of the smell.</li>
<li><strong>Chewing gum</strong> is not sold in Singapore and importing it is banned, so do not pack any.</li>
<li><strong>Smoking</strong> is banned in most public places, and in much of the city centre you may only smoke in marked smoking areas. Littering brings fines.</li>
<li><strong>Drug laws</strong> are among the strictest in the world, with very severe penalties.</li>
</ul>
<p>Day to day, none of this feels heavy; the rules are simply enforced, which is one reason the city works so well.</p>
{fig("strip-artscience", "The white lotus-shaped ArtScience Museum under a blue sky", "Clean, safe and easy to navigate: Singapore rewards a little preparation.", "50% 45%")}

<h2>Should you tip in Singapore?</h2>
<p>Tipping is not expected. Most restaurants and hotels add a 10% service charge, and prices usually also include or add 9% GST, which is why menus often show "++" after prices. At hawker centres there is no service charge and no tipping. Leave a little extra only if service was exceptional.</p>

<h2>How can tourists get a GST refund?</h2>
<p>Visitors can claim back the 9% GST on goods they take out of the country through the electronic Tourist Refund Scheme. You need to spend at least S$100, including GST, at one retailer; up to three same-day receipts from the same shop can be combined. You must be 16 or over.</p>
<p>At Changi, scan your passport at an eTRS kiosk. Claim in the departure check-in hall, before you check in the goods, if they are going in your hold luggage, or in the transit area after immigration if you carry them on board. Customs may ask to see the goods and receipts.</p>

<h2>What should you know about money in Singapore?</h2>
<ul>
<li>The currency is the Singapore dollar (S$).</li>
<li>Cards and phone payments are accepted almost everywhere, and contactless cards work on the MRT and buses.</li>
<li>Carry a little cash for older hawker stalls, although many now take QR or card payments.</li>
<li>For a full breakdown of costs, read our <a href="/blog/singapore-trip-budget">Singapore trip budget</a>.</li>
</ul>

<h2>What plugs, water and phone service does Singapore have?</h2>
<ul>
<li><strong>Plugs:</strong> three-pin Type G sockets, as in the UK, at 230 volts.</li>
<li><strong>Water:</strong> tap water is safe to drink, so bring a refillable bottle.</li>
<li><strong>Phone:</strong> tourist SIM cards and eSIMs are sold at Changi Airport and in convenience stores; free Wi-Fi is common in malls and at the airport.</li>
</ul>
{fig("hl-fullerton", "The Fullerton Hotel and financial district reflected in the bay at sunset", "The Fullerton Hotel, once the General Post Office, at the mouth of the Singapore River.", "50% 55%")}

<h2>How do you deal with the heat and rain?</h2>
<p>It is hot and humid all year, usually 25°C to 32°C, with short, heavy downpours. Plan outdoor sights for the early morning and evening, carry water and a small umbrella, and use the air-conditioned malls, museums and underground walkways in the afternoon. Indoor spaces are often cold, so bring a light layer. See <a href="/blog/best-time-to-visit-singapore">the best time to visit Singapore</a>.</p>

<h2>What etiquette should you follow?</h2>
<ul>
<li>Dress modestly and remove your shoes when visiting temples and mosques.</li>
<li>Queue patiently; Singaporeans queue for everything, especially good food.</li>
<li>At hawker centres, a packet of tissues on a seat means it is taken. Return your tray when you finish.</li>
<li>Stand on the left on escalators and let people walk past on the right.</li>
</ul>
""",
        "checked_note": "Facts checked October 2026. Entry rules, fines and refund conditions are set by the Singapore government and can change; check the official sources before you travel.",
        "sources": [
            ("SG Arrival Card (Immigration & Checkpoints Authority)", f"{ICA}/enter-depart/arriving/overview/sg-arrival-card"),
            ("Tourist Refund Scheme (Singapore Customs)", "https://www.customs.gov.sg/at-customs/departing-singapore/tourist-refund-scheme/"),
            ("Stricter rules for e-cigarettes from 1 September 2025 (Embassy of Sweden in Singapore)", "https://www.swedenabroad.se/en/embassies/singapore-singapore/current/news/stricter-rules-for-e-cigarettes-vaping-in-singapore--from-september-1-2025/"),
            ("What consumers need to know about the 9% GST rate (IRAS)", "https://www.iras.gov.sg/who-we-are/what-we-do/annual-reports-and-publications/taxbytes-iras/gst/what-consumers-need-to-know-with-the-new-gst-rate-from-1-jan-2024"),
        ],
    },
    {
        "slug": "singapore-trip-budget",
        "short": "How Much Does a Trip to Singapore Cost?",
        "title": "How Much Does a Trip to Singapore Cost? A Daily Budget Guide (2027)",
        "description": "How much to budget for Singapore: typical daily costs for hotels, hawker food, transport and attractions, with real ticket prices for Gardens by the Bay and Marina Bay Sands, and tips to save money.",
        "category": "Planning · Budget",
        "teaser": "Daily costs for hotels, food, transport and sights.",
        "image": "hl-marina-barrage",
        "image_alt": "Aerial view of the garden domes and Marina Barrage beside the sea",
        "stats": [
            ("S$5–8", "Typical hawker centre meal"),
            ("S$46", "Flower Dome & Cloud Forest, non-resident adult"),
            ("S$35", "SkyPark Observation Deck, off-peak adult"),
            ("Free", "Garden Rhapsody, Spectra and the outdoor gardens"),
        ],
        "body": f"""
<p>Singapore has a reputation as an expensive city, and hotels and drinks certainly are. But food can be very cheap, public transport costs little, and many of the best sights are free. Here is what a day in Singapore really costs, and where your money goes.</p>
<!--TOC-->
<h2>How much should you budget per day in Singapore?</h2>
<p>As a rough guide per person, excluding flights, and assuming you share a room:</p>
<div class="table-wrap"><table>
<thead><tr><th>Style</th><th>Per day</th><th>What it looks like</th></tr></thead>
<tbody>
<tr><td>Budget</td><td>S$100–150</td><td>Hostel or simple hotel, hawker food, MRT, mostly free sights</td></tr>
<tr><td>Mid-range</td><td>S$250–400</td><td>Three- or four-star hotel, hawkers and some restaurants, one paid attraction a day</td></tr>
<tr><td>Luxury</td><td>S$600+</td><td>Five-star hotel, restaurants and bars, taxis, ticketed experiences</td></tr>
</tbody></table></div>
<p>Hotel rates swing a lot with the season and big events such as the Formula 1 race weekend, so book early for those dates.</p>

<h2>How much is food in Singapore?</h2>
<p>Hawker centres are the best value in the city. A plate of chicken rice, noodles or a rice set usually costs about S$5 to S$8, and a fresh juice or kopi a couple of dollars more. A 2023 study by the Institute of Policy Studies found that three hawker meals a day cost about S$17 on average; prices have crept up since. Restaurants are much more expensive, especially with the 10% service charge and 9% GST added to the bill.</p>

<h2>How much does transport cost?</h2>
<p>Very little. Most MRT and bus trips cost between about S$1 and S$2.50 with a contactless card, and you do not need a pass. A taxi from Changi Airport to the city costs about S$25 to S$45 on the meter, plus an airport surcharge. See <a href="/blog/getting-around-singapore">getting around Singapore</a>.</p>
{fig("hl-skyway", "The OCBC Skyway walkway between the Supertrees at Gardens by the Bay", "The OCBC Skyway, one of the cheaper paid attractions at S$14 for a non-resident adult.", "50% 50%")}

<h2>How much do attractions cost?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Attraction</th><th>Non-resident adult</th></tr></thead>
<tbody>
<tr><td>Flower Dome &amp; Cloud Forest, Gardens by the Bay</td><td>S$46</td></tr>
<tr><td>OCBC Skyway, Gardens by the Bay</td><td>S$14</td></tr>
<tr><td>SkyPark Observation Deck, Marina Bay Sands (off-peak)</td><td>S$35</td></tr>
<tr><td>Garden Rhapsody, Spectra, Jewel's Rain Vortex</td><td>Free</td></tr>
</tbody></table></div>
<p>Big ticketed days out such as Universal Studios on Sentosa or the Mandai wildlife parks cost more, so check prices and bundles on their official sites.</p>

<h2>What can you do for free?</h2>
<p>A lot: the outdoor gardens and Supertree Grove at Gardens by the Bay, the Singapore Botanic Gardens, the Merlion and the Marina Bay waterfront, the temples of Chinatown, Kampong Glam and Little India, and three free light shows every evening. Our list of <a href="/blog/free-things-to-do-in-singapore">free things to do in Singapore</a> has the details.</p>
{fig("hl-supertrees-above", "Supertrees lit purple and red seen from above at night", "The Supertrees light up for free twice every evening.", "50% 50%")}

<h2>How can you save money in Singapore?</h2>
<ul>
<li>Eat at hawker centres and food courts rather than restaurants.</li>
<li>Drink tap water, which is safe, and refill a bottle.</li>
<li>Look for happy hours: alcohol is heavily taxed, so drinks are expensive.</li>
<li>Use the MRT instead of taxis, and tap your own contactless card.</li>
<li>Plan your evenings around the free light shows.</li>
<li>Claim the GST refund on bigger purchases; see our <a href="/blog/singapore-travel-tips">Singapore travel tips</a>.</li>
</ul>
{fig("guide-bay-day", "Marina Bay Sands and the garden domes across the water on a bright day", "The view across the bay from Marina Barrage costs nothing.", "50% 60%")}
""",
        "checked_note": "Facts checked October 2026. Ticket prices are non-resident rates set by each attraction. Daily budgets and food prices are estimates; hotel rates in particular vary with season and events.",
        "sources": [
            ("Flower Dome (Gardens by the Bay)", f"{GBTB}/en/things-to-do/attractions/flower-dome.html"),
            ("OCBC Skyway (Gardens by the Bay)", f"{GBTB}/en/things-to-do/attractions/ocbc-skyway.html"),
            ("SkyPark Observation Deck (Marina Bay Sands)", f"{MBS}/attractions/skypark-observation-deck.html"),
            ("Eating out at hawker centres three times a day costs about S$17: IPS study (Mothership, via LKY School)", "https://lkyspp.nus.edu.sg/docs/default-source/ips/mothership_eating-out-at-hawker-centres-food-courts-kopitiams-3-times-a-day-costs-about-s17_-ips-study_230314.pdf"),
        ],
    },
    {
        "slug": "singapore-stopover-guide",
        "short": "Singapore Stopover: Layover Tours & Ideas",
        "title": "Singapore Stopover Guide: Free Changi Tours and What to Do on a Layover (2027)",
        "description": "How to spend a Singapore layover: the Free Singapore Tour from Changi with times and eligibility, what to do in 6, 12 or 24 hours, getting into the city, and what to see without leaving the airport.",
        "category": "Planning · Changi",
        "teaser": "Free airport tours and what to do in 6, 12 or 24 hours.",
        "image": "strip-jewel",
        "image_alt": "The Rain Vortex falling through the glass dome of Jewel Changi, surrounded by trees",
        "stats": [
            ("5.5–24 h", "Layover needed for the Free Singapore Tour"),
            ("2.5 h", "Length of each free tour"),
            ("3 days", "Window to submit the SG Arrival Card"),
        ],
        "body": f"""
<p>Changi is one of the best airports in the world to be stuck in, and Singapore is one of the easiest cities to see on a layover. With a few hours you can see the Rain Vortex at Jewel; with half a day you can be at the Merlion and back. Here is how to plan it.</p>
<!--TOC-->
<h2>Can you leave Changi Airport on a layover?</h2>
<p>Yes, if your passport allows you to enter Singapore. Many nationalities can visit without a visa; others need one, and some can use the Visa Free Transit Facility for up to 96 hours if they meet its conditions. Check the ICA visa requirements, and submit the free SG Arrival Card in the three days before you land. You will pass immigration, so allow time to clear security again on the way back.</p>

<h2>What is the Free Singapore Tour?</h2>
<p>Changi runs free guided city tours of about two and a half hours for transit passengers with a layover of 5.5 to 24 hours. Your checked bags must be through-checked to your final destination, and you can only pass through immigration once during the layover. Tours include a Heritage and Culture tour, a City Sights tour, a Singapore River and Marina Bay Sands tour, and a newer Sentosa Discovery tour, with start times from 10 am to 7 pm.</p>
<p>You can pre-book on the Changi Airport website up to 50 days ahead, or walk in to a tour booth in the transit area of Terminal 2 or 3, subject to seats. Arrive at the booth at least 90 minutes before the tour starts, and do not clear immigration first.</p>
{fig("hl-merlion", "The Merlion statue lit gold at night, spouting water into the bay", "The Merlion, a stop on many layover tours.", "30% 60%")}

<h2>What can you do with 6 hours?</h2>
<p>Take a free tour if the times fit, or stay at the airport: walk through Jewel to see the Rain Vortex, explore the gardens inside the terminals, and eat well. Jewel is on the public side, so you need to clear immigration to reach it. Read our <a href="/blog/jewel-changi-guide">Jewel Changi guide</a> for the light show times.</p>

<h2>What can you do with 12 hours?</h2>
<p>Head into the city. The MRT reaches the centre in well under an hour, or take a taxi for about S$25 to S$45. Spend the afternoon at Gardens by the Bay and the Marina Bay waterfront, eat at Lau Pa Sat or Maxwell, and if your flight is late, catch the 7.45 pm Garden Rhapsody show. Aim to be back at Changi at least two to three hours before departure.</p>
{fig("hl-marina-bay-sands", "Marina Bay Sands lit red at night with the ArtScience Museum in front", "Marina Bay Sands is under an hour from Changi by train.", "50% 55%")}

<h2>What can you do with 24 hours?</h2>
<p>Book a hotel and see the highlights: Marina Bay and the light shows in the evening, Chinatown and Kampong Glam the next morning. Our <a href="/blog/singapore-itinerary-3-days">3-day Singapore itinerary</a> has more ideas to choose from, and <a href="/blog/things-to-do-in-marina-bay">things to do in Marina Bay</a> covers the area closest to the airport.</p>

<h2>What should you know before you go?</h2>
<ul>
<li>Store bulky bags at the airport's baggage storage before heading out.</li>
<li>Tap a contactless card on the MRT; there is no need to buy a ticket. See <a href="/blog/getting-around-singapore">getting around Singapore</a>.</li>
<li>It is hot and humid: carry water and wear light clothes.</li>
<li>Leave your vape at home: e-cigarettes are illegal in Singapore. See <a href="/blog/singapore-travel-tips">Singapore travel tips</a>.</li>
</ul>
""",
        "checked_note": "Facts checked October 2026. Tour times and eligibility are set by Changi Airport, and entry rules by ICA; both can change, so check before you fly.",
        "sources": [
            ("Free Singapore Tour (Changi Airport)", f"{CHANGI}/en/experience/tours/free-singapore-tour.html"),
            ("Visa Free Transit Facility (Immigration & Checkpoints Authority)", f"{ICA}/enter-transit-depart/entering-singapore/visa-free-transit-facility"),
            ("SG Arrival Card (Immigration & Checkpoints Authority)", f"{ICA}/enter-depart/arriving/overview/sg-arrival-card"),
            ("Jewel Rain Vortex (Jewel Changi Airport)", "https://www.jewelchangiairport.com/en/attractions/rain-vortex.html"),
        ],
    },
]
