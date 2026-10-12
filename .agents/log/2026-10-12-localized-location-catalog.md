---
title: Localized location catalog
date: 2026-10-12
status: done
related_paths:
  - src/aerial_danger/locations/
  - src/aerial_danger/location_presets.py
  - src/aerial_danger/models.py
---

# Localized location catalog

## Decision

The user requested JSON presets and library-owned Ukrainian and English names,
superseding the label ownership in the
[extraction decision](2026-09-18-extract-danger-library.md). Keep one bundled JSON
file per region. Locality object keys are the ID source; do not repeat their IDs
inside records. Keep the existing dataclass/resolver API and expose `names` maps.
Preserve IDs and matcher patterns independently of display labels.

All existing HA labels are retained. Missing settlement names were checked against
the 2026-07-07 KATOTTG workbook within their region; neighbourhoods and landmarks
use city/owner sources. Coordinates, radii, and government IDs are deferred.

## Release coordination

The user requested separate library and HA PRs. The HA PR generates selector labels
from this catalog and stays draft until a release containing this library change is
published on PyPI. A chat heartbeat will update the HA project, lockfile, manifest,
and labels after publication. Neither PR is authorized for automatic merge, and
publishing remains the maintainer's action.

## Verification

- [x] 76 library tests pass; lint and formatting pass.
- [x] Wheel and sdist smoke tests pass on Python 3.10 and 3.14.
- [x] All 25 region and 168 existing HA locality labels match exactly in both languages.
- [x] Every one of the 788 localities has nonempty Ukrainian and English names.

## Implementation Notes

Merged current main before publication, restoring 12 released presets and newer
matcher fixes absent from the locality branch. The earlier Shuliavka failure is
resolved by preserving the released alias. Existing custom preset constructors
remain compatible through an empty default names map; bundled data requires both
languages. Research tools were temporary, not added as production dependencies.
