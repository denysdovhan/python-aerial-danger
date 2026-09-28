# Imported matcher history

Copied unchanged from `ha-aerial-danger/.agents/log` on 2026-09-28.
Start with [the index](index.md) and [the extraction decision](2026-09-18-extract-danger-library.md).
Newer decisions supersede older ones. Completed entries remain frozen.

Historical paths refer to the integration repository:

- `custom_components/aerial_danger/danger/` now maps to `src/aerial_danger/`.
- `presets.py` is now `location_presets.py`, exporting `LOCATION_PRESETS`.
- `tests/danger/` now maps to `tests/`.

The library owns matching and location IDs/patterns. Display names, translations,
source aggregation, entities, and triggers belong to the consuming application.
The linked aggregation, diagnostic-sensor, and trigger logs are historical
context, not instructions to implement Home Assistant features in this library.
Old test counts and commands describe checks at the time, not current results.
