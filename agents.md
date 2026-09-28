# AI Coding Agents Guide

## Working style

- Keep changes small and replies concise. Ask before changing unclear behavior.
- Preserve unrelated edits, existing comments, and debugging logs.
- Prefer the standard library and native uv features over custom scripts or abstractions.
- Commit, push, or publish only when requested. Use `<type>(<scope>): summary` with a summary of at most 40 characters.
- Keep tests generic and data-driven. Add locality aliases and inflections to shared preset examples, not area-specific test functions. Use dedicated tests only for distinct edge cases.

## Decision history

- Before repository work, read [.agents/log/index.md](.agents/log/index.md). Search entries by touched paths and task keywords, then read matching entries in full.
- Newer decisions supersede older ones. Keep finalized `done` entries unchanged. Continue a matching `wip` entry for significant work and finalize only at the user's request or when asked to create a PR for designed changesk.
- Read [the import guide](.agents/log/README.md) for historical path mappings. Old HA paths, commands, and test counts are historical, not current library instructions.
- The [extraction decision](.agents/log/2026-09-18-extract-danger-library.md) supersedes library-owned display names and bundled-package paths. HA entities and source aggregation remain consumer responsibilities.

## Library boundaries

- Distribution: `aerial-danger`. Import: `aerial_danger`. Keep the `src/aerial_danger/` layout and `uv_build` backend.
- Support Python 3.10 and later. Keep matching independent of Home Assistant and network access.
- `danger.py` owns detection, `keywords.py` owns regex templates, and `models.py` owns results. `location_presets.py` owns `LOCATION_PRESETS`; `pattern_utils.py` resolves patterns and IDs.
- Applications provide localized labels, collect messages, and manage active-danger state. Do not add display names or translations to this library.

## Matching contract

- First match wins: IRBM, MLRS, guided bomb, ballistic, cruise, drone, then generic danger.
- IRBM is nationwide. MLRS, guided bombs, and drones require a configured locality. Other types require a configured region or locality.
- Channel context must not bypass area matching. Do not infer weapon types from locations or target counts alone.
- `SAFETY` vetoes every danger type. `is_safe()` reports a regex match, not real-world safety. A non-match is not an all-clear.
- Preserve the original message, exact matched text, and matching regexes. Keep invalid-regex errors visible to callers.

## Research and regexes

- Reproduce mistakes with the exact message before changing patterns. Fix the owning domain rather than a downstream symptom.
- Search public histories with `https://telegram.me/s/<channel>?q=<term>`. Use `operinform`, `war_monitor`, `AerisRimor`, and `kpszsu`; for Kyiv, also use `nebo_raketa`, `kyiv_airdef`, and `kyiv_monit0ring`.
- Read neighboring posts. Separate active alerts from forecasts, analysis, aftermath, and all-clear messages. Search abbreviations, inflections, slang, and location stems.
- Prefer separate one-line regexes for different word orders. Group equivalent spellings and inflections. Use the smallest observed bounded gap instead of `.*`; cross lines only when examples require it.
- Keep weapon wording in its domain list and type-neutral target or direction wording in `GENERIC_DANGER`. Anchor bare-area and direction-only generic patterns to the whole message.
- Reserve `☄` and `☄️` for ballistic detection and `🛵` for drones. These markers must not fall through generic matching.
- Use strict positive MLRS and guided-bomb patterns. Their forecasts and aftermath stay non-matching, not new `SAFETY` rules.
- Preserve newer explicit safety exceptions, including `підготовка до пусків` and `планується залучення`. Do not classify all forecast wording as safety.

## Locations and tests

- Keep IDs stable, lowercase Latin snake_case, and equal to their registry keys. Nest localities under their owning region and keep keys sorted.
- Regions represent oblasts, with Kyiv city as a separate region. Localities include settlements, neighborhoods, and landmarks. Keep nearby settlements outside Kyiv city.
- Resolve custom patterns first, then presets, with stable deduplication. Ignore unknown IDs and respect selected-region ownership.
- Test real `LOCATION_PRESETS` data instead of mocking or duplicating the registry. Add spellings to `PRESET_EXAMPLES` in `tests/test_location_presets.py`.
- Put message regressions in the owning domain test. Reuse `REGION_PATTERNS` and `LOCALITY_PATTERNS` from `tests/common.py`.
- Preserve punctuation, case, emojis, and line breaks. Exclude channel names and message IDs from fixtures; keep research provenance in logs.
- Cover positive alerts and negative forecasts, aftermath, unrelated areas, and substring collisions. Deduplicate examples differing only by location.

## Validation

Run from this repository after code changes:

```sh
uv sync --locked
uv run ruff format --check .
uv run ruff check .
uv run pytest
```

For packaging or public API changes, also run `uv build --no-sources` and the installed wheel and source-distribution checks from [.github/workflows/ci.yml](.github/workflows/ci.yml).

Install hooks with `uv run pre-commit install`. Do not bypass failing hooks without permission. Keep lockfiles on public registries.

## Local integration testing

Follow [CONTRIBUTING.md](CONTRIBUTING.md#test-with-home-assistant). From the sibling HA checkout, use `uv add --editable ../python-aerial-danger`, then run its tests. Do not commit the local source override or its lockfile changes.

Pass `--skip-pip-packages aerial-danger` when starting development HA. Never put the integration's `custom_components` directory directly on `PYTHONPATH`: it shadows this library. Use its parent directory.

## Documentation and maintenance

- Keep the README short, with installation commands, Usage examples, and method declarations. Use reference-style badge links and credit Denys Dovhan in the license section.
- Releases belong to the maintainer. Preserve release-tag versioning and PyPI trusted publishing through the `pypi` environment. Do not publish without approval.
- Keep HA manifest synchronization in the integration repository, not in library release steps.
