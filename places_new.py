"""Extra map places (added Oct 2026). Same fields as make_trip.HIGHLIGHTS; tag/desc are
filled from places_content.json when present. All are map-only (grid=False)."""
NEW = [
    dict(id="sri-mariamman-temple", name="Sri Mariamman Temple", area="Chinatown", kind="Temple", cats="culture", q="Sri Mariamman Temple, South Bridge Road, Singapore"),
    dict(id="masjid-sultan", name="Masjid Sultan", area="Kampong Glam", kind="Mosque", cats="culture icons", q="Masjid Sultan, Muscat Street, Singapore"),
    dict(id="sri-veeramakaliamman", name="Sri Veeramakaliamman Temple", area="Little India", kind="Temple", cats="culture", q="Sri Veeramakaliamman Temple, Serangoon Road, Singapore"),
    dict(id="national-museum", name="National Museum of Singapore", area="Civic District", kind="Museum", cats="culture family", q="National Museum of Singapore"),
    dict(id="helix-bridge", name="Helix Bridge", area="Marina Bay", kind="Bridge", cats="icons nightlife", q="The Helix Bridge, Singapore"),
    dict(id="victoria-theatre", name="Victoria Theatre and Concert Hall", area="Civic District", kind="Heritage", cats="culture", q="Victoria Theatre and Concert Hall, Singapore"),
    dict(id="universal-studios", name="Universal Studios Singapore", area="Sentosa", kind="Theme park", cats="family", q="Universal Studios Singapore"),
    dict(id="siloso-beach", name="Siloso Beach", area="Sentosa", kind="Beach", cats="nature family", q="Siloso Beach, Sentosa, Singapore"),
    dict(id="fort-siloso", name="Fort Siloso", area="Sentosa", kind="Heritage", cats="culture family", q="Fort Siloso, Sentosa, Singapore"),
    dict(id="singapore-oceanarium", name="Singapore Oceanarium", area="Sentosa", kind="Aquarium", cats="family", q="Singapore Oceanarium, Sentosa"),
    dict(id="night-safari", name="Night Safari", area="Mandai", kind="Wildlife park", cats="family nightlife nature", q="Night Safari, Mandai, Singapore"),
    dict(id="bird-paradise", name="Bird Paradise", area="Mandai", kind="Wildlife park", cats="family nature", q="Bird Paradise, Mandai, Singapore"),
    dict(id="tekka-centre", name="Tekka Centre", area="Little India", kind="Hawker centre", cats="food", q="Tekka Centre, Buffalo Road, Singapore"),
    dict(id="mustafa-centre", name="Mustafa Centre", area="Little India", kind="Shopping", cats="shopping", q="Mustafa Centre, Syed Alwi Road, Singapore"),
    dict(id="bugis-street", name="Bugis Street", area="Bugis", kind="Market", cats="shopping food", q="Bugis Street, Victoria Street, Singapore"),
    dict(id="emerald-hill", name="Emerald Hill", area="Orchard", kind="Street", cats="culture", q="Emerald Hill Road, Singapore"),
    dict(id="changi-chapel-museum", name="Changi Chapel and Museum", area="Changi", kind="Museum", cats="culture", q="Changi Chapel and Museum, Upper Changi Road North, Singapore"),
    dict(id="kranji-war-memorial", name="Kranji War Memorial", area="Kranji", kind="Memorial", cats="culture", q="Kranji War Memorial, Singapore"),
    dict(id="henderson-waves", name="Henderson Waves", area="Southern Ridges", kind="Bridge", cats="nature icons", q="Henderson Waves, Singapore"),
    dict(id="singapore-cable-car", name="Singapore Cable Car", area="Mount Faber", kind="Viewpoint", cats="family icons", q="Mount Faber Peak, Singapore Cable Car"),
    dict(id="kusu-island", name="Kusu Island", area="Southern Islands", kind="Island", cats="nature culture", q="Kusu Island, Singapore"),
    dict(id="rail-corridor", name="Rail Corridor", area="Bukit Timah", kind="Walk", cats="nature", q="Bukit Timah Railway Station, Rail Corridor, Singapore"),
]

NEW_COORDS = {"sri-mariamman-temple":(1.28268,103.84519),"masjid-sultan":(1.30222,103.859),"sri-veeramakaliamman":(1.30795,103.8524),"national-museum":(1.29655,103.84832),"helix-bridge":(1.28800,103.86025),"victoria-theatre":(1.28836,103.85141),"chijmes":(1.29521,103.85211),"universal-studios":(1.2542,103.82267),"siloso-beach":(1.25437,103.81333),"fort-siloso":(1.25877,103.8088),"singapore-oceanarium":(1.25835,103.82048),"night-safari":(1.40135,103.789),"bird-paradise":(1.40546,103.78099),"tekka-centre":(1.30619,103.85061),"mustafa-centre":(1.31012,103.85532),"bugis-street":(1.29938,103.85579),"emerald-hill":(1.30238,103.83913),"changi-chapel-museum":(1.36219,103.97402),"kranji-war-memorial":(1.41906,103.75804),"henderson-waves":(1.27605,103.81541),"singapore-cable-car":(1.27121,103.81941),"kusu-island":(1.22311,103.8612),"rail-corridor":(1.33427,103.78113)}
