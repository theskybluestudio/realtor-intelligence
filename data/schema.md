# Data schema

## Top-level keys

- `market`
  - `title`
  - `subtitle`
  - `last_updated`
  - `condition_label`
- `quarters`: ordered quarter labels for trend charts
- `distribution`: list of `{ label, pct }`
- `segments`: list of segment objects

## Segment object

- `id`
- `label`
- `median`
- `heat`
- `kpis`: list of `{ label, value, badge, note }`
- `series`
  - `median_price`
  - `average_price`
  - `dom_avg`
