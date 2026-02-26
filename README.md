# 🏈 GritOS CFB Recruiting Map

**An interactive intelligence tool for college football recruiting — built for student-athletes, families, and coaches who want to find the right fit, not just the biggest name.**

🔗 **[[View the Live Map]([[https://verifygrit-admin.github.io/CFB-mapping/cfbrecruit-map.html]**

---

## What This Tool Does

The GritOS CFB Recruiting Map displays **661 college football programs** across the United States on a filterable, interactive map. Every pin represents a real program with a full data card — covering division, conference, academic selectivity, financial metrics, admission and graduation rates, and direct links to recruiting questionnaires where available.

The map is built around a core GritOS philosophy: **the "Platinum Opportunity."** Rather than chasing full D1 scholarships that may never materialize, this tool helps families identify programs at academically selective institutions — many offering partial or no athletic scholarships — that deliver the highest long-term return on investment through career placement, alumni networks, and institutional prestige.

---

## Who This Is For

### Student-Athletes & Families
Use this map to build a realistic, strategic school list. You can:
- See every program geographically so proximity and region factor into your decision
- Filter by division tier, academic selectivity, and conference to find programs that fit your profile
- Identify high-value programs you may never have considered — strong ADLTV rank, high graduation rates, and meaningful merit aid
- Click any pin to see financial data, admission rates, and link directly to a school's recruiting questionnaire

### High School Coaches
Use this map to broaden your recruiting conversations with players:
- Quickly surface realistic fits for players across the full spectrum of ability and academic profile
- Use the ADLTV rank filter to identify programs with strong career value regardless of division label
- Find programs in specific geographic regions or conferences matching a player's profile
- Access recruiting questionnaire links directly from any program card

### College Football Coaches
- Understand the competitive landscape visually
- See how your program's selectivity tier, ADLTV rank, and conference compare to peers
- Identify geographic clusters of programs competing for the same recruit profiles

---

## Navigating the Map

### The Sidebar Filters

The left panel contains six filters that work together in real time. Every change immediately updates both the map pins and the **program count** displayed in the header ("Showing X programs"). Filters stack — each one narrows the results further.

---

#### 🔍 Search
Type any school name, city, or state abbreviation. Results update as you type. This is the fastest path to a specific school or to narrow geographically (e.g., type "NY" to see only New York programs).

---

#### 🏷️ Division Tier
Six colored toggle buttons represent the six division tiers. Click any button to show or hide that tier. Click **All** to toggle every tier on or off at once.

| Button Color | Tier | Conferences Included |
|---|---|---|
| 🟠 **Orange** | Power 4 | ACC, Big Ten, Big 12, SEC, Pac-12 |
| 🔵 **Blue** | Group of 5 | American, CUSA, MAC, Mountain West, Sun Belt |
| 🟣 **Purple** | FBS Independent | Notre Dame, UConn, UMass |
| 🟢 **Green** | FCS | Ivy League, Patriot, CAA, Pioneer, Big Sky, SWAC, MEAC, and more |
| 🔴 **Red** | Division II | NSIC, PSAC, GLIAC, SAC, RMAC, and more |
| ⚪ **Gray** | Division III | NESCAC, MIAC, ODAC, Centennial, CCIW, SCIAC, and more |

**Power tip:** Toggle off Power 4 and Group of 5, leaving only FCS + D-II + D-III active — this reveals the full landscape of programs where a student-athlete may have a genuine opportunity while still attending a high-quality institution.

---

#### 🎓 School Type (Selectivity)
Filters programs by academic admission selectivity, derived from IPEDS data:

| Tier | Approximate Admission Rate |
|---|---|
| Super Elite | Under 10% — Ivy League, MIT, Stanford, etc. |
| Elite | 10–20% — Georgetown, Duke, Tufts, Davidson, etc. |
| Very Selective | 20–30% — Holy Cross, Richmond, Villanova, Cal Poly, etc. |
| Selective | 30–50% — Many strong liberal arts and regional universities |
| Somewhat Selective | 50–65% — Broad mix across all divisions |
| Standard | 65%+ — Open or near-open enrollment |

**Power tip:** Combine **Elite + FCS** to surface the Ivy League, Patriot League, and Pioneer League — the highest academic/athletic overlap in the country.

---

#### 🏟️ Conference
Narrows the map to a single athletic conference. All 50+ conferences in the dataset are available. Useful when a player has a specific conference target or when a coach is researching a particular league.

---

#### 📊 ADLTV Rank (Top N)
**ADLTV (Athletic Degree Lifetime Value)** is GritOS's proprietary metric estimating the long-term career earnings premium associated with each institution's degree — incorporating graduation rates, median post-graduate earnings, and institutional reputation in the context of athletic opportunity.

Filter to **Top 25, 50, 100, 150, or 200** to isolate the programs GritOS considers highest-value regardless of division.

A few examples from the Top 10:
- **#1 — MIT** (Division III, NEWMAC) · $4,308,227
- **#2 — Princeton** (FCS, Ivy League) · $3,834,084
- **#3 — University of Pennsylvania** (FCS, Ivy League) · $3,794,952
- **#4 — Stanford** (Power 4, ACC) · $3,593,990
- **#5 — Carnegie Mellon** (Division III, PAC) · $3,566,646
- **#6 — Bentley** (Division II, NE10) · $3,378,443

This filter is the map's most strategically important control. It deliberately cuts across divisions — a family filtering to Top 50 will see MIT, Harvard, Carnegie Mellon, and Villanova sitting alongside Power 4 schools. This is the GritOS thesis made visual: **division tier and career value are not the same thing.**

---

#### 🗺️ State
Filter to a single state. Useful for families with geographic constraints or coaches building regional pipelines.

---

#### ↺ Reset All Filters
Clears every active filter and restores all 661 programs to the map.

---

### Reading a Program Card

Click any pin to open its data card:

| Field | What It Means |
|---|---|
| **School Name & Location** | Institution name, city, state |
| **Tier Badge** | Division tier, color-coded to match the legend |
| **Conference** | Athletic conference |
| **School Type** | Academic selectivity tier |
| **ADLTV** | GritOS estimated lifetime degree value (dollar figure) |
| **ADLTV Rank** | GritOS rank out of 661 programs |
| **Admission Rate** | % of applicants admitted (IPEDS source) |
| **Graduation Rate** | 6-year graduation rate (IPEDS source) |
| **COA (Out-of-State)** | Total annual cost of attendance |
| **Est. Avg Merit** | Average institutional merit aid awarded |
| **Recruiting Questionnaire** | Direct link to submit your info to the coaching staff (where collected) |
| **UNITID** | IPEDS unique institution identifier |
| **Division Code** | Raw NCAA classification string (e.g., "3-Div III") |

If no questionnaire link is available, the button is not shown. Schools whose questionnaires are managed via Field Level are noted as such.

---

### Map Behavior

- **Pins cluster automatically** at lower zoom levels. Cluster bubbles shift color from **amber → orange → red** as density increases. Click any cluster to zoom in and expand the pins.
- **Pan and zoom** freely — scroll to zoom, click-drag to pan.
- **Popups close** when you click elsewhere or open a different pin.

---

## Design Philosophy

The UX is intentionally built around **progressive disclosure** — start with the full landscape, filter down to a precise target. The default view shows all 661 programs so users begin with complete awareness before narrowing. Filters are additive (AND logic), meaning you can simultaneously filter by tier + selectivity + ADLTV rank + state to arrive at a tightly scoped list.

**The dark color palette** (charcoal backgrounds, amber accent) matches GritOS brand standards and improves map legibility — the six tier colors read clearly against the Carto Dark Matter basemap even at maximum cluster density.

**The ADLTV filter** is positioned last in the sidebar but is the most strategically differentiated control in the tool. It surfaces a non-obvious truth: the programs most worth a family's serious attention are not always the ones with the most prominent football brands.

---

## For Developers

### Stack

| Layer | Technology | Version |
|---|---|---|
| Map rendering | Leaflet.js | 1.9.4 |
| Pin clustering | Leaflet.MarkerCluster | 1.5.3 |
| Basemap tiles | Carto Dark Matter | — |
| Typography | Google Fonts (Barlow, Barlow Condensed) | — |
| Runtime | Vanilla HTML/CSS/JavaScript | — |

No build step, no bundler, no server-side dependencies. All CDN assets load from `unpkg.com` and `fonts.googleapis.com`. The entire application is a **single static HTML file** deployable anywhere.

---

### Data Structure

All program data is embedded as a JavaScript constant `SCHOOLS` — an array of 661 objects at the top of the `<script>` block. Each object follows this schema:

```javascript
{
  "unitid":     "196866",        // IPEDS unique institution ID (string)
  "name":       "Union College", // Institution name
  "div":        "3-Div III",     // Raw division code ("1-FBS", "1-FCS", "2-Div II", "3-Div III")
  "tier":       "Division III",  // Display tier — maps to TIER_COLORS and filter buttons
  "conf":       "Liberty",       // Athletic conference abbreviation
  "city":       "Schenectady",   // City
  "state":      "NY",            // 2-letter state code
  "lat":        42.818097,       // Latitude (float)
  "lng":        -73.928788,      // Longitude (float)
  "type":       "Selective",     // Academic selectivity tier (6-level enum)
  "adltv":      "$2,180,951",    // ADLTV value (formatted dollar string)
  "adltv_rank": "78",            // ADLTV rank out of 661 (string integer)
  "adm_rate":   "43.79%",        // IPEDS admission rate (formatted string)
  "grad_rate":  "85.26%",        // IPEDS 6-year graduation rate (formatted string)
  "coa_out":    "$88,125.00",    // Out-of-state cost of attendance (formatted string)
  "merit":      "$21,855",       // Average institutional merit aid (formatted string, "$0" if none)
  "q_link":     ""               // Recruiting questionnaire URL; "" if none, "Field Level" if platform-managed
}
```

**`type` enum values** (6 levels):
`"Super Elite"` | `"Elite"` | `"Very Selective"` | `"Selective"` | `"Somewhat Selective"` | `"Standard"`

**`tier` enum values** (6 levels):
`"Power 4"` | `"Group of 5"` | `"FBS Ind"` | `"FCS"` | `"Division II"` | `"Division III"`

**Note on `div` vs `tier`:** The `div` field is the raw IPEDS/NCAA classification. The `tier` field reflects GritOS's subdivision of FBS into Power 4, Group of 5, and FBS Independent — used for pin coloring and filter logic. `div` appears in the popup footer.

**Note on duplicate UNITIDs:** Pennsylvania Western University (3 campuses) and Commonwealth University of Pennsylvania (2 campuses) each appear as multiple records sharing one `unitid` because each campus location fields a separate football program with a distinct city coordinate. This is intentional.

---

### Tier Color Mapping

Defined at the top of the script as `TIER_COLORS` and mirrored as CSS custom properties in `:root`:

```javascript
const TIER_COLORS = {
  'Power 4':     '#f5a623',  // amber
  'Group of 5':  '#4fc3f7',  // light blue
  'FBS Ind':     '#ce93d8',  // lavender
  'FCS':         '#81c784',  // green
  'Division II': '#ef9a9a',  // coral red
  'Division III':'#b0bec5',  // cool gray
};
```

CSS custom properties for use in other elements:
```css
:root {
  --p4:  #f5a623;
  --g5:  #4fc3f7;
  --fbs: #ce93d8;
  --fcs: #81c784;
  --d2:  #ef9a9a;
  --d3:  #b0bec5;
}
```

---

### Pin Rendering

Each pin is a `L.divIcon` — an inline SVG circle 14×14px, color-matched to tier, with a dark stroke for contrast against the map. This keeps rendering lightweight and avoids external icon dependencies.

```javascript
function makeIcon(tier) {
  const color = TIER_COLORS[tier] || '#aaa';
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 14 14">
    <circle cx="7" cy="7" r="6" fill="${color}" stroke="#0a0c10" stroke-width="1.5"/>
  </svg>`;
  return L.divIcon({ className: '', html: svg, iconSize: [14,14], iconAnchor: [7,7], popupAnchor: [0,-10] });
}
```

---

### Filtering Logic

All filters evaluate client-side in `applyFilters()`. Logic is additive **AND** — a marker must pass every active filter to render. The function:

1. Reads current state from all filter inputs
2. Calls `clusterGroup.clearLayers()` to remove all visible markers
3. Loops all 661 pre-built `allMarkers` entries
4. For each marker, evaluates these conditions in order:
   - **Tier** — is `s.tier` a member of `activeTiers` Set?
   - **Search** — does `s.name`, `s.state`, or `s.city` include the search string (case-insensitive)?
   - **Type** — exact string match against `s.type`
   - **Conference** — exact string match against `s.conf`
   - **State** — exact string match against `s.state`
   - **ADLTV Rank** — parses `s.adltv_rank` as integer, passes if `rank <= N`
5. Passes markers via `clusterGroup.addLayer(m)`
6. Updates the `#visibleCount` display

Tier state is tracked in an `activeTiers` Set, driven by the toggle button click handler. The **All** button toggles the full set on/off and syncs individual button active states.

---

### Adding or Updating Records

**To add a school:** Append a new object to the `SCHOOLS` array following the schema above. Coordinates can be sourced from the IPEDS institution lookup (IPEDS Data Center) or Google Maps. Match the `unitid` to the official IPEDS UNITID for data integrity.

**To update a questionnaire link:** Find the school by `name` in the `SCHOOLS` array and update its `q_link` value. Use `""` where no questionnaire exists. Use `"Field Level"` for programs whose questionnaire is managed exclusively through the Field Level platform — the popup render function checks `if (s.q_link)` before displaying the button, so non-URL truthy strings like `"Field Level"` will not generate a broken link.

**To update financial or academic data:** All `adm_rate`, `grad_rate`, `coa_out`, `merit`, and `adltv` fields are formatted strings. Update the string directly (e.g., `"43.79%"`, `"$88,125.00"`).

---

### Deployment

This is a single static HTML file with no server-side dependencies.

| Platform | Method |
|---|---|
| **GitHub Pages** | Push to `main` and configure Pages to serve from root, or push to a `gh-pages` branch |
| **Netlify / Vercel** | Drop the file or connect the repo — zero config required |
| **S3 + CloudFront** | Upload as a static asset, set index document |
| **Local** | Open directly in any browser — CDN assets load from `unpkg.com` and `fonts.googleapis.com` |

---

## Data Sources

| Field | Source |
|---|---|
| Division, Conference | NCAA / GritOS internal database |
| Admission Rate, Graduation Rate, COA | IPEDS (Integrated Postsecondary Education Data System) |
| Geographic Coordinates | IPEDS institution coordinates |
| ADLTV, ADLTV Rank | GritOS proprietary model |
| Merit Aid | IPEDS institutional grant aid averages |
| Recruiting Questionnaire URLs | Manually collected from athletic department websites |
| Academic Selectivity Tier | GritOS classification derived from IPEDS admission rates |

---

## About GritOS

GritOS is a college football recruiting advisory service that helps student-athletes and families navigate selective colleges offering partial or no athletic scholarships. We use data analysis, financial modeling, and recruiting strategy to identify market inefficiencies in college admissions and athletic recruiting — and help families capitalize on them.

**[gritos.com](https://www.gritos.com)** | Built by Chris Conroy

---

*661 programs · FBS through Division III · All 50 states · Updated February 2026*
