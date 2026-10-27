/* Discover Singapore trip planner. The trip is a list of place ids kept in
   localStorage on the visitor's device. window.DS_TRIP = {places, max} is
   prepended by make_trip.py. */
(function () {
  "use strict";
  var D = window.DS_TRIP || { places: {}, max: 10 };
  var P = D.places, MAX = D.max || 10, KEY = "ds-trip-v1";
  var JSPDF = "https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js";

  function load() {
    try {
      var v = JSON.parse(localStorage.getItem(KEY) || "[]");
      return Array.isArray(v) ? v.filter(function (id) { return P[id]; }).slice(0, MAX) : [];
    } catch (e) { return []; }
  }
  var trip = load();
  function save() { try { localStorage.setItem(KEY, JSON.stringify(trip)); } catch (e) {} }
  function has(id) { return trip.indexOf(id) !== -1; }
  function esc(s) {
    return String(s || "").replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function mapsUrl(p) { return "https://www.google.com/maps/search/?api=1&query=" + encodeURIComponent(p.q); }

  /* Toast and floating button */
  var toast, toastTimer, fab;
  function say(html) {
    if (!toast) {
      toast = document.createElement("div");
      toast.className = "triptoast";
      toast.setAttribute("role", "status");
      document.body.appendChild(toast);
    }
    toast.innerHTML = html;
    toast.classList.add("show");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { toast.classList.remove("show"); }, 3200);
  }
  var onTripPage = !!document.getElementById("tripList");

  function refresh() {
    var n = trip.length;
    document.querySelectorAll("[data-trip-count]").forEach(function (el) { el.textContent = n ? n : ""; });
    document.querySelectorAll(".addt").forEach(function (b) {
      var on = has(b.dataset.trip);
      b.setAttribute("aria-pressed", on ? "true" : "false");
      b.innerHTML = on ? "<b>✓</b><span>Added</span>" : "<b>+</b><span>Add to trip</span>";
      var name = P[b.dataset.trip] ? P[b.dataset.trip].n : "";
      b.setAttribute("aria-label", (on ? "Remove " + name + " from" : "Add " + name + " to") + " my trip");
    });
    if (!onTripPage && document.getElementById("hlGrid")) {
      if (!fab) {
        fab = document.createElement("a");
        fab.className = "tripfab";
        fab.href = "/trip";
        document.body.appendChild(fab);
      }
      fab.innerHTML = '<span class="n">' + n + "</span>My trip · free PDF";
      fab.classList.toggle("show", n > 0);
    }
    if (onTripPage) renderTrip();
  }

  function toggle(id) {
    var p = P[id];
    if (!p) return;
    if (has(id)) {
      trip.splice(trip.indexOf(id), 1);
      say("Removed " + esc(p.n) + " from your trip.");
    } else {
      if (trip.length >= MAX) {
        say("Your trip has " + MAX + " stops, the most one route can hold. Remove one to add another. <a href=\"/trip\">View my trip</a>");
        return;
      }
      trip.push(id);
      say("Added " + esc(p.n) + " to your trip. " + (onTripPage ? "" : "<a href=\"/trip\">View my trip</a>"));
    }
    save();
    refresh();
  }

  document.addEventListener("click", function (e) {
    var b = e.target.closest && e.target.closest(".addt");
    if (b) { e.preventDefault(); toggle(b.dataset.trip); }
  });
  window.addEventListener("storage", function (e) { if (e.key === KEY) { trip = load(); refresh(); } });

  /* Highlights: category chips and "Show more" */
  var grid = document.getElementById("hlGrid");
  if (grid) {
    var cards = [].slice.call(grid.querySelectorAll(".card.hl"));
    var chips = [].slice.call(document.querySelectorAll(".hl-chip"));
    var more = document.getElementById("hlMore");
    var LIMIT = cards.filter(function (c) { return !c.hasAttribute("hidden"); }).length || 12;
    var cat = "all", open = false;
    var show = function () {
      var shown = 0;
      cards.forEach(function (c) {
        var match = cat === "all" || (" " + c.dataset.cats + " ").indexOf(" " + cat + " ") !== -1;
        var vis = match && (cat !== "all" || open || shown < LIMIT);
        if (vis) shown++;
        c.hidden = !vis;
      });
      if (more) {
        more.hidden = cat !== "all";
        more.textContent = open ? "Show fewer highlights" : "Show more highlights";
        more.setAttribute("aria-expanded", open ? "true" : "false");
      }
    };
    chips.forEach(function (ch) {
      ch.addEventListener("click", function () {
        cat = ch.dataset.cat;
        chips.forEach(function (o) { o.setAttribute("aria-pressed", o === ch ? "true" : "false"); });
        show();
      });
    });
    if (more) more.addEventListener("click", function () {
      open = !open;
      show();
      if (!open) document.getElementById("highlights").scrollIntoView({ behavior: "smooth" });
    });
    show();
  }

  /* Trip page */
  function picture(p, sizes) {
    return p.i
      ? '<img src="' + p.i + '" alt="' + esc(p.n) + '" loading="lazy" decoding="async"' + (sizes ? ' sizes="' + sizes + '"' : "") + ">"
      : '<span class="card-ph" aria-hidden="true"></span>';
  }
  function renderTrip() {
    var list = document.getElementById("tripList");
    var empty = document.getElementById("tripEmpty");
    var note = document.getElementById("tripNote");
    var pdf = document.getElementById("tpPdf");
    var route = document.getElementById("tpRoute");
    list.innerHTML = trip.map(function (id, i) {
      var p = P[id];
      return '<li><span class="no">' + (i + 1) + '</span><span class="pic">' + picture(p) + "</span>" +
        "<div><h3>" + esc(p.n) + '</h3><p class="meta">' + esc(p.k) + " · " + esc(p.a) + '</p><p class="tg">' + esc(p.t) + "</p></div>" +
        '<span class="ctl">' +
        '<button type="button" data-mv="-1" data-id="' + id + '" aria-label="Move ' + esc(p.n) + ' up"' + (i === 0 ? " disabled" : "") + ">↑</button>" +
        '<button type="button" data-mv="1" data-id="' + id + '" aria-label="Move ' + esc(p.n) + ' down"' + (i === trip.length - 1 ? " disabled" : "") + ">↓</button>" +
        '<button type="button" data-rm="' + id + '" aria-label="Remove ' + esc(p.n) + '">×</button></span></li>';
    }).join("");
    empty.hidden = trip.length > 0;
    list.hidden = trip.length === 0;
    note.textContent = trip.length ? trip.length + " of " + MAX + " stops. Use the arrows to put them in the order you want to visit." : "";
    pdf.disabled = trip.length === 0;
    if (trip.length) {
      var qs = trip.map(function (id) { return P[id].q; });
      var url = "https://www.google.com/maps/dir/?api=1&travelmode=transit&origin=" + encodeURIComponent(qs[0]) +
        "&destination=" + encodeURIComponent(qs[qs.length - 1]);
      if (qs.length > 2) url += "&waypoints=" + encodeURIComponent(qs.slice(1, -1).join("|"));
      route.href = qs.length === 1 ? mapsUrl(P[trip[0]]) : url;
      route.removeAttribute("aria-disabled");
    } else {
      route.href = "https://www.google.com/maps";
      route.setAttribute("aria-disabled", "true");
    }
    var sug = document.getElementById("suggestGrid");
    var picks = Object.keys(P).filter(function (id) { return !has(id) && P[id].i; }).slice(0, 6);
    document.getElementById("tripSuggest").hidden = picks.length === 0 || trip.length >= MAX;
    sug.innerHTML = picks.map(function (id) {
      var p = P[id];
      return '<div class="card hl">' + picture(p, "(min-width: 760px) 20vw, 50vw") + '<span class="card-tag">' + esc(p.a) + "</span>" +
        '<button class="addt" type="button" data-trip="' + id + '" aria-pressed="false"><b>+</b><span>Add to trip</span></button>' +
        '<span class="card-body"><strong>' + esc(p.n) + "</strong><em>" + esc(p.t) + "</em></span></div>";
    }).join("");
  }

  if (onTripPage) {
    document.getElementById("tripList").addEventListener("click", function (e) {
      var b = e.target.closest("button");
      if (!b) return;
      if (b.dataset.rm) { toggle(b.dataset.rm); return; }
      var i = trip.indexOf(b.dataset.id), j = i + Number(b.dataset.mv);
      if (i < 0 || j < 0 || j >= trip.length) return;
      trip.splice(j, 0, trip.splice(i, 1)[0]);
      save();
      refresh();
      var again = document.querySelector('#tripList button[data-id="' + b.dataset.id + '"][data-mv="' + b.dataset.mv + '"]');
      if (again && !again.disabled) again.focus();
    });
    var form = document.getElementById("tripForm");
    try {
      var saved = JSON.parse(localStorage.getItem(KEY + "-me") || "{}");
      ["name", "from", "to"].forEach(function (k) { if (saved[k]) form.elements[k].value = saved[k]; });
    } catch (e) {}
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var me = { name: form.elements.name.value.trim(), from: form.elements.from.value, to: form.elements.to.value };
      try { localStorage.setItem(KEY + "-me", JSON.stringify(me)); } catch (err) {}
      makePdf(me);
    });
  }

  /* PDF itinerary */
  function loadScript(src) {
    return new Promise(function (ok, fail) {
      if (window.jspdf) return ok();
      var s = document.createElement("script");
      s.src = src; s.onload = ok; s.onerror = fail;
      document.head.appendChild(s);
    });
  }
  function toDataUrl(src) {
    return new Promise(function (ok) {
      if (!src) return ok(null);
      var img = new Image();
      img.onload = function () {
        try {
          var w = 800, h = Math.round(w * 9 / 16), c = document.createElement("canvas");
          c.width = w; c.height = h;
          var r = Math.max(w / img.width, h / img.height), iw = img.width * r, ih = img.height * r;
          c.getContext("2d").drawImage(img, (w - iw) / 2, (h - ih) / 2, iw, ih);
          ok(c.toDataURL("image/jpeg", 0.82));
        } catch (e) { ok(null); }
      };
      img.onerror = function () { ok(null); };
      img.src = src;
    });
  }
  function fmtDate(v) {
    if (!v) return "";
    var d = new Date(v + "T12:00:00");
    return isNaN(d) ? "" : d.toLocaleDateString("en-GB", { weekday: "short", day: "numeric", month: "long", year: "numeric" });
  }
  function dayCount(me) {
    if (!me.from || !me.to) return 0;
    var n = Math.round((new Date(me.to + "T12:00:00") - new Date(me.from + "T12:00:00")) / 864e5) + 1;
    return n > 0 && n < 60 ? n : 0;
  }

  function makePdf(me) {
    var status = document.getElementById("tpStatus"), btn = document.getElementById("tpPdf");
    if (!trip.length) return;
    btn.disabled = true;
    status.textContent = "Making your PDF…";
    var stops = trip.map(function (id) { return P[id]; });
    Promise.all([loadScript(JSPDF)].concat(stops.map(function (p) { return toDataUrl(p.i); })))
      .then(function (res) {
        var imgs = res.slice(1), doc = new window.jspdf.jsPDF({ unit: "mm", format: "a4" });
        var W = 210, H = 297, M = 18, INK = [14, 19, 23], RED = [200, 32, 47], MUTED = [90, 100, 107], TEAL = [12, 42, 48];
        var days = dayCount(me), perDay = days ? Math.ceil(stops.length / days) : 0;

        // Cover
        doc.setFillColor.apply(doc, INK); doc.rect(0, 0, W, H, "F");
        if (imgs[0]) {
          doc.addImage(imgs[0], "JPEG", 0, 0, W, W * 9 / 16);
          doc.setFillColor.apply(doc, INK);
        }
        doc.setFont("helvetica", "bold"); doc.setTextColor(255, 255, 255); doc.setFontSize(11);
        doc.text("DISCOVER SINGAPORE", M, 140);
        doc.setFillColor.apply(doc, RED); doc.rect(M, 146, 22, 1.6, "F");
        doc.setFontSize(38); doc.text("My Singapore", M, 166); doc.text("trip", M, 181);
        doc.setFont("helvetica", "normal"); doc.setFontSize(12); doc.setTextColor(210, 216, 220);
        var y = 198;
        if (me.name) { doc.text("Planned by " + me.name, M, y); y += 7; }
        var from = fmtDate(me.from), to = fmtDate(me.to);
        if (from && to) { doc.text(from + " to " + to + (days ? "  (" + days + (days === 1 ? " day)" : " days)") : ""), M, y); y += 7; }
        doc.text(stops.length + (stops.length === 1 ? " stop" : " stops"), M, y); y += 14;
        doc.setFontSize(10); doc.setTextColor(170, 180, 186);
        doc.text(doc.splitTextToSize("Every stop has a Google Maps link: tap 'Open in Google Maps' under any stop, or use the route on the last page.", W - 2 * M), M, y);
        doc.setFont("helvetica", "bold"); doc.setTextColor(255, 255, 255); doc.setFontSize(10);
        doc.text("discoversingapore.org", M, H - 16);

        // Stops, two per page
        var slot = 0;
        stops.forEach(function (p, i) {
          if (slot % 2 === 0) {
            doc.addPage();
            doc.setFillColor.apply(doc, INK); doc.rect(0, 0, W, 14, "F");
            doc.setFont("helvetica", "bold"); doc.setFontSize(8); doc.setTextColor(255, 255, 255);
            doc.text("DISCOVER SINGAPORE  ·  MY TRIP", M, 9);
          }
          var top = slot % 2 === 0 ? 24 : 158;
          slot++;
          if (perDay && i % perDay === 0) {
            var d = Math.floor(i / perDay);
            var label = "DAY " + (d + 1);
            if (me.from) {
              var dd = new Date(me.from + "T12:00:00"); dd.setDate(dd.getDate() + d);
              label += "  ·  " + dd.toLocaleDateString("en-GB", { weekday: "long", day: "numeric", month: "long" }).toUpperCase();
            }
            doc.setFont("helvetica", "bold"); doc.setFontSize(9); doc.setTextColor.apply(doc, RED);
            doc.text(label, M, top + 2);
          }
          var iy = top + 6, ih = (W - 2 * M) * 9 / 16 * 0.62, iw = ih * 16 / 9;
          if (imgs[i]) doc.addImage(imgs[i], "JPEG", M, iy, iw, ih);
          else {
            doc.setFillColor.apply(doc, TEAL); doc.rect(M, iy, iw, ih, "F");
            doc.setFont("helvetica", "bold"); doc.setFontSize(10); doc.setTextColor(255, 255, 255);
            doc.text(p.k.toUpperCase(), M + 6, iy + ih - 6);
          }
          var tx = M + iw + 8, tw = W - M - tx;
          doc.setFont("helvetica", "bold"); doc.setFontSize(26); doc.setTextColor.apply(doc, RED);
          doc.text(String(i + 1), tx, iy + 10);
          doc.setFontSize(15); doc.setTextColor.apply(doc, INK);
          var nameLines = doc.splitTextToSize(p.n, tw);
          doc.text(nameLines, tx, iy + 20);
          var ny = iy + 20 + nameLines.length * 6.2;
          doc.setFontSize(8); doc.setTextColor.apply(doc, RED);
          doc.text((p.k + "  ·  " + p.a).toUpperCase(), tx, ny);
          doc.setFont("helvetica", "normal"); doc.setFontSize(10); doc.setTextColor.apply(doc, MUTED);
          doc.text(doc.splitTextToSize(p.t, tw), tx, ny + 7);
          var by = iy + ih + 10;
          doc.setFontSize(10.5); doc.setTextColor.apply(doc, INK);
          var body = doc.splitTextToSize(p.d, W - 2 * M);
          doc.text(body, M, by, { lineHeightFactor: 1.45 });
          var ly = by + body.length * 5.4 + 6;
          doc.setFont("helvetica", "bold"); doc.setFontSize(10); doc.setTextColor.apply(doc, RED);
          doc.textWithLink("Open in Google Maps", M, ly, { url: mapsUrl(p) });
          doc.setDrawColor(220, 215, 205); doc.line(M, ly + 6, W - M, ly + 6);
        });

        // Route page
        doc.addPage();
        doc.setFillColor.apply(doc, TEAL); doc.rect(0, 0, W, H, "F");
        doc.setFont("helvetica", "bold"); doc.setTextColor(255, 255, 255); doc.setFontSize(24);
        doc.text("Your route", M, 40);
        doc.setFillColor.apply(doc, RED); doc.rect(M, 46, 22, 1.6, "F");
        doc.setFont("helvetica", "normal"); doc.setFontSize(12);
        var ry = 62;
        stops.forEach(function (p, i) {
          doc.setFont("helvetica", "bold"); doc.text((i + 1) + ".", M, ry);
          doc.textWithLink(p.n, M + 10, ry, { url: mapsUrl(p) });
          doc.setFont("helvetica", "normal"); doc.setTextColor(190, 205, 208);
          doc.text(p.a, W - M, ry, { align: "right" });
          doc.setTextColor(255, 255, 255);
          ry += 10;
        });
        var route = document.getElementById("tpRoute").href;
        if (stops.length > 1) {
          doc.setFont("helvetica", "bold"); doc.setTextColor(255, 154, 162);
          doc.textWithLink("Open the whole route in Google Maps", M, ry + 8, { url: route });
        }
        doc.setFont("helvetica", "normal"); doc.setFontSize(10); doc.setTextColor(190, 205, 208);
        doc.text(doc.splitTextToSize("Tips: tap a contactless bank card at the MRT gates instead of buying a ticket, carry water, and plan outdoor sights for the morning or evening. Opening hours change, so check each place before you go.", W - 2 * M), M, H - 50);
        doc.setFont("helvetica", "bold"); doc.setTextColor(255, 255, 255);
        doc.text("More guides at discoversingapore.org", M, H - 22);

        // Page numbers
        var pages = doc.getNumberOfPages();
        for (var k = 2; k < pages; k++) {
          doc.setPage(k);
          doc.setFont("helvetica", "normal"); doc.setFontSize(8); doc.setTextColor.apply(doc, MUTED);
          doc.text("discoversingapore.org", M, H - 8);
          doc.text(k + " / " + pages, W - M, H - 8, { align: "right" });
        }
        var blob = doc.output("blob"), url = URL.createObjectURL(blob), file = "my-singapore-trip.pdf";
        var a = document.createElement("a");
        a.href = url; a.download = file; a.rel = "noopener";
        document.body.appendChild(a); a.click(); a.remove();
        status.innerHTML = 'Your PDF is ready. Have a wonderful trip! If it did not download, <a href="' + url + '" download="' + file + '" target="_blank" rel="noopener">tap here to open your PDF</a>.';
      })
      .catch(function () {
        status.textContent = "Sorry, the PDF could not be made. Check your connection and try again.";
      })
      .then(function () { btn.disabled = trip.length === 0; });
  }

  refresh();
})();
