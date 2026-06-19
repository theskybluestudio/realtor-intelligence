# Application Blueprint

This document defines the initial folder/file blueprint for the `realtor-intelligence` Streamlit application.

## Goal

Build a Streamlit webapp that recreates the core experience of `../ref/RealEstateIntelligenceDashboard.jsx` in a Streamlit-native way.

## Runtime baseline

- Python version: **3.12**
- Virtual environment: project-local **`.venv/`** inside `application/`

Build target:
- dark branded market dashboard
- segment summary strip
- tabbed analysis views
- KPI cards
- interactive time-series charts
- comparison view across price tiers

---

## Proposed Folder Structure

```text
application/
  BLUEPRINT.md                 # This file: structure + implementation intent
  README.md                    # Project overview, setup, run instructions
  requirements.txt             # Python dependencies for Streamlit app
  app.py                       # Main Streamlit entrypoint

  .streamlit/
    config.toml                # Theme + Streamlit UI configuration

  components/
    __init__.py
    theme.py                   # Shared colors, typography tokens, style helpers
    header.py                  # Top banner / market overview block
    segment_strip.py           # Segment summary strip
    kpi_cards.py               # KPI card rendering helpers
    charts.py                  # Reusable Plotly chart builders
    sections.py                # Section headers, badges, alerts, shared UI pieces
    layout.py                  # Common layout helpers / wrappers

  data/
    __init__.py
    sample_market.json         # Initial static fixture mirroring the reference artifact
    schema.md                  # Human-readable data contract
    loaders.py                 # Load data from JSON / CSV / future APIs
    transforms.py              # Convert raw data into UI-ready structures
    selectors.py               # Data access helpers by market/segment/time range

  pages/
    __init__.py
    full_market.py             # Full-market tab content
    segment.py                 # Segment tab content
    comparison.py              # Cross-segment comparison content
    reports.py                 # Placeholder for export/report workflows

  utils/
    __init__.py
    formatters.py              # Currency, percentages, date labels, KPI text
    constants.py               # Tab ids, labels, market condition thresholds
    state.py                   # Session state helpers

  assets/
    styles.css                 # Custom CSS injected into Streamlit
    logo/                      # Optional branding assets

  docs/
    roadmap.md                 # Phased build plan
    decisions.md               # Architecture and design decisions log
```

---

## File Responsibilities

## Root files

### `app.py`
Primary app entrypoint.

Responsibilities:
- configure page settings
- load theme/CSS
- load market data
- initialize session state
- render header
- render segment strip
- create tabs
- dispatch tab content to page modules

### `requirements.txt`
Initial expected dependencies:
- `streamlit`
- `plotly`
- `pandas`
- `pydantic` (optional but recommended for schema validation)

### `README.md`
Should cover:
- purpose
- local setup
- how to run the app
- project structure
- development roadmap

---

## `.streamlit/`

### `config.toml`
Used for:
- dark theme defaults
- app chrome preferences
- consistent palette foundation

---

## `components/`
Reusable UI building blocks.

### `theme.py`
Defines:
- color palette
- semantic colors
- spacing constants
- chart theme helpers

### `header.py`
Renders:
- title
- market name
- metadata pills
- market status badge
- last updated timestamp

### `segment_strip.py`
Renders the horizontal summary strip for:
- Full Market
- $200K–$500K
- $500K–$1M
- $1M–$2M
- $2M+

Should support selected-state styling and interaction through `st.session_state`.

### `kpi_cards.py`
Renders KPI blocks with:
- label
- value
- optional badge
- optional note
- accent color

### `charts.py`
Reusable Plotly chart builders for:
- single-line trend chart
- multi-line trend chart
- inventory/supply dual-axis or normalized chart
- histogram / distribution chart
- optional heat-score visualization

### `sections.py`
Reusable presentation pieces:
- section headers
- badge styles
- alert banners
- summary lists

### `layout.py`
Helpers for:
- card containers
- grid wrappers
- consistent spacing

---

## `data/`
The app should be data-driven from the start.

### `sample_market.json`
Initial seed dataset copied conceptually from the reference JSX.

Should include:
- market metadata
- segments
- KPIs
- quarterly series
- distribution buckets
- market condition values

### `schema.md`
Human-readable definition of expected data fields and meaning.

### `loaders.py`
Functions for:
- loading local JSON fixture
- future CSV ingestion
- future external API ingestion

### `transforms.py`
Functions for:
- converting raw input to chart series
- flattening KPI structures
- generating comparison datasets

### `selectors.py`
Convenience helpers like:
- get full market segment
- get segment by id
- get all comparison series

---

## `pages/`
Tab content modules.

### `full_market.py`
Contains the full-market dashboard sections:
- pricing metrics
- time-on-market metrics
- inventory & supply
- market intelligence summary

### `segment.py`
Reusable renderer for individual segment views.

### `comparison.py`
Cross-segment overlay charts and comparison summaries.

### `reports.py`
Initially placeholder-only.
Later used for:
- CSV export
- PDF/report controls
- scheduled reporting workflows

---

## `utils/`
Non-UI helpers.

### `formatters.py`
Functions like:
- currency formatting
- percent formatting
- days labels
- quarter labels

### `constants.py`
Shared constants such as:
- tab ids
- segment ids
- labels
- market thresholds for seller/buyer/balanced states

### `state.py`
Functions for safe Streamlit session state initialization and updates.

---

## `assets/`
Static visual assets.

### `styles.css`
Custom CSS for:
- dark card styling
- badges
- borders
- spacing polish
- typography overrides where needed

### `logo/`
Optional future branding assets.

---

## `docs/`
Project documentation.

### `roadmap.md`
Phase plan:
1. static prototype
2. data abstraction
3. analyst features
4. export/reporting
5. deployment

### `decisions.md`
Capture choices like:
- Plotly over Altair
- single-page tabs over multipage app for v1
- JSON fixture before live source integration

---

## MVP Build Order

### Phase 1 — Blueprint + setup
- finalize structure
- create dependency list
- set up app entrypoint
- create theme + CSS foundation

### Phase 2 — Static dashboard shell
- header
- segment strip
- tabs
- KPI cards
- empty chart containers

### Phase 3 — Sample-data dashboard
- load `sample_market.json`
- render full-market view
- render segment views
- render comparison charts

### Phase 4 — Polish
- spacing
- badges
- alerts
- visual parity improvements vs reference

### Phase 5 — Analyst utilities
- export controls
- download tables
- notes / commentary sections

---

## Recommended First Files to Actually Build

When implementation starts, build in this order:

1. `requirements.txt`
2. `app.py`
3. `.streamlit/config.toml`
4. `assets/styles.css`
5. `data/sample_market.json`
6. `data/loaders.py`
7. `components/theme.py`
8. `components/header.py`
9. `components/kpi_cards.py`
10. `components/charts.py`
11. `pages/full_market.py`
12. `pages/segment.py`
13. `pages/comparison.py`

---

## Notes

- The app should be built as a Streamlit-native adaptation, not a line-by-line React port.
- Reusability matters: avoid putting large rendering logic directly into `app.py`.
- All new implementation work should stay within `application/`.
