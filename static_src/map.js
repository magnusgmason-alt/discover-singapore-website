/* Discover Singapore interactive map. Uses window.DS_TRIP (places with
   coordinates) from trip.js and window.DSTrip for the "Add to trip" state.
   Leaflet is loaded only when the map scrolls near the viewport. */
(function () {
  "use strict";
  var root = document.getElementById("smap");
  if (!root || !window.DS_TRIP) return;
  var P = window.DS_TRIP.places;
  var CDN = "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/";
  var ids = Object.keys(P).filter(function (id) { return P[id].ll; });
  var canvas = document.getElementById("smapCanvas");
  var list = document.getElementById("smapList");
  var card = document.getElementById("smapCard");
  var chips = [].slice.call(document.querySelectorAll("#smapChips .hl-chip"));
  var cat = "all", active = null, map = null, markers = {};

  function esc(s) {
    return String(s || "").replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function inCat(id) { return cat === "all" || (" " + P[id].c + " ").indexOf(" " + cat + " ") !== -1; }
  function inTrip(id) { return window.DSTrip ? window.DSTrip.has(id) : false; }

  /* Side list (desktop) */
  function renderList() {
    var shown = ids.filter(inCat);
    list.innerHTML = '<p class="smap-count">' + shown.length + " places</p><ul>" + shown.map(function (id) {
      var p = P[id];
      return '<li><button type="button" data-id="' + id + '"' + (id === active ? ' aria-current="true"' : "") + ">" +
        "<strong>" + esc(p.n) + "</strong><span>" + esc(p.k) + " · " + esc(p.a) + "</span>" +
        (inTrip(id) ? '<i class="smap-in" aria-label="In your trip">✓</i>' : "") + "</button></li>";
    }).join("") + "</ul>";
  }
  list.addEventListener("click", function (e) {
    var b = e.target.closest("button[data-id]");
    if (b) select(b.dataset.id, true);
  });

  /* Preview card */
  function renderCard(id) {
    var p = P[id];
    var pic = p.i
      ? '<img src="' + p.i + '" alt="' + esc(p.n) + '" loading="lazy" decoding="async">'
      : '<span class="card-ph" data-kind="' + esc(p.k) + '" aria-hidden="true"></span>';
    var maps = "https://www.google.com/maps/search/?api=1&query=" + encodeURIComponent(p.q);
    card.innerHTML =
      '<button type="button" class="smap-close" aria-label="Close preview">×</button>' +
      '<div class="smap-pic">' + pic + '<span class="card-tag">' + esc(p.a) + "</span></div>" +
      '<div class="smap-body"><p class="smap-kind">' + esc(p.k) + "</p><h3>" + esc(p.n) + "</h3><p>" + esc(p.d) + "</p>" +
      '<div class="smap-actions"><button class="addt smap-addt" type="button" data-trip="' + id + '" aria-pressed="false"><b>+</b><span>Add to trip</span></button>' +
      '<a class="smap-link" href="' + maps + '" target="_blank" rel="noopener">Google Maps</a>' +
      (p.b ? '<a class="smap-link" href="/blog/' + p.b + '">Read our guide</a>' : "") +
      "</div></div>";
    card.hidden = false;
    if (window.DSTrip) window.DSTrip.refresh();
  }
  card.addEventListener("click", function (e) {
    if (e.target.closest(".smap-close")) { active = null; card.hidden = true; paint(); renderList(); }
  });

  function select(id, fly) {
    active = id;
    renderCard(id);
    renderList();
    paint();
    if (map && fly) {
      var z = Math.max(map.getZoom(), 15);
      map.flyTo(P[id].ll, z, { duration: 0.6 });
    }
    if (fly && window.matchMedia("(max-width: 860px)").matches) {
      root.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  }

  /* Markers */
  function icon(id) {
    var cls = "smap-pin" + (id === active ? " is-active" : "") + (inTrip(id) ? " is-trip" : "");
    return window.L.divIcon({ className: "smap-pin-wrap", html: '<span class="' + cls + '"></span>', iconSize: [26, 26], iconAnchor: [13, 13] });
  }
  function paint() {
    if (!map) return;
    ids.forEach(function (id) {
      var m = markers[id], show = inCat(id);
      if (show && !map.hasLayer(m)) m.addTo(map);
      if (!show && map.hasLayer(m)) map.removeLayer(m);
      if (show) { m.setIcon(icon(id)); m.setZIndexOffset(id === active ? 1000 : 0); }
    });
  }

  chips.forEach(function (ch) {
    ch.addEventListener("click", function () {
      cat = ch.dataset.cat;
      chips.forEach(function (o) { o.setAttribute("aria-pressed", o === ch ? "true" : "false"); });
      if (active && !inCat(active)) { active = null; card.hidden = true; }
      renderList();
      paint();
      if (map) {
        var pts = ids.filter(inCat).map(function (id) { return P[id].ll; });
        if (pts.length) map.flyToBounds(pts, { padding: [40, 40], maxZoom: 15, duration: 0.6 });
      }
    });
  });

  document.addEventListener("ds-trip-change", function () { renderList(); paint(); });

  function start() {
    var css = document.createElement("link");
    css.rel = "stylesheet"; css.href = CDN + "leaflet.min.css";
    document.head.appendChild(css);
    var s = document.createElement("script");
    s.src = CDN + "leaflet.min.js";
    s.onload = function () {
      var L = window.L;
      map = L.map(canvas, { scrollWheelZoom: false, zoomControl: true, tap: true, minZoom: 10, maxZoom: 18 });
      L.tileLayer("https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png", {
        subdomains: "abcd", maxZoom: 19,
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'
      }).addTo(map);
      ids.forEach(function (id) {
        markers[id] = L.marker(P[id].ll, { icon: icon(id), title: P[id].n, keyboard: true, riseOnHover: true })
          .on("click", function () { select(id, false); });
      });
      map.fitBounds(ids.map(function (id) { return P[id].ll; }), { padding: [30, 30] });
      map.on("focus click", function () { map.scrollWheelZoom.enable(); });
      map.on("mouseout", function () { map.scrollWheelZoom.disable(); });
      root.classList.add("is-ready");
      paint();
    };
    s.onerror = function () {
      canvas.innerHTML = '<p class="smap-fail">The map could not load. Pick a place from the list to see it.</p>';
    };
    document.head.appendChild(s);
  }

  renderList();
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      if (entries.some(function (e) { return e.isIntersecting; })) { io.disconnect(); start(); }
    }, { rootMargin: "600px 0px" });
    io.observe(root);
  } else {
    start();
  }
})();
