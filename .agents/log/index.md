# Agent Log Index

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

## Log Entries

| Date       | Name                                                                             | Status |
| ---------- | -------------------------------------------------------------------------------- | ------ |
| 2026-09-18 | [Standalone danger matching library](2026-09-18-extract-danger-library.md)       | done   |
| 2026-08-10 | [Planned-launch safety wording](2026-08-10-planned-launch-safety.md)             | done   |
| 2026-08-05 | [Source reset on non-danger messages](2026-08-05-source-reset-on-non-danger.md)  | done   |
| 2026-08-03 | [Regional area presets](2026-08-03-regional-area-presets.md)                     | done   |
| 2026-08-03 | [Generic danger precision](2026-08-03-generic-danger-precision.md)               | done   |
| 2026-07-31 | [MLRS and guided bomb detection](2026-07-31-mlrs-guided-bomb-detection.md)       | done   |
| 2026-07-28 | [Danger phrase precision](2026-07-28-danger-phrase-precision.md)                 | done   |
| 2026-07-27 | [Diagnostic match sensors](2026-07-27-diagnostic-match-sensors.md)               | done   |
| 2026-07-23 | [Target-based danger triggers](2026-07-23-target-danger-triggers.md)             | done   |
| 2026-07-22 | [Kyiv locality research](2026-07-22-kyiv-locality-research.md)                   | done   |
| 2026-07-21 | [Kyiv area presets](2026-07-21-area-presets.md)                                  | done   |
| 2026-07-21 | [IRBM danger detection](2026-07-21-irbm-danger-detection.md)                     | done   |
| 2026-07-20 | [Reactive drone detection](2026-07-20-reactive-drone-detection.md)               | done   |
| 2026-07-13 | [Cleanup attributes](2026-07-13-cleanup-attributes.md)                           | done   |
| 2026-07-10 | [Multi-entry source aggregation](2026-07-10-multi-entry-source-aggregation.md)   | done   |
| 2026-07-10 | [Aerial Danger product direction](2026-07-10-aerial-danger-product-direction.md) | done   |
