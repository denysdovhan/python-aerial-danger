# Aerial Danger

[![CI][ci-badge-img]][ci-badge-url]
[![PyPI version][pypi-badge-img]][pypi-badge-url]

Match Ukrainian aerial danger messages with regular expressions.

A match is not an official alert. A non-match does not mean that an area is safe.

## Install

With uv:

```sh
uv add aerial-danger
```

With pip, inside your virtual environment:

```sh
python -m pip install aerial-danger
```

With Poetry:

```sh
poetry add aerial-danger
```

## Usage

Detect danger for your region and locality:

```python
from aerial_danger import DangerDetector, DangerType

detector = DangerDetector(
    regions=[r"\bкиїв\b"],
    localities=[r"\bнивк\w*"],
)
result = detector.danger("КИЇВ ШВИДКІСНА!")
assert result.danger
assert result.type == DangerType.BALLISTIC
assert result.matched_area == "КИЇВ"
assert result.message == "КИЇВ ШВИДКІСНА!"

assert detector.drone_danger("Шахед на Нивки!").danger
assert not detector.danger("Привіт").danger
```

Use built-in area presets instead of custom patterns:

```python
from aerial_danger import DangerDetector
from aerial_danger.pattern_utils import (
    resolve_locality_patterns,
    resolve_region_patterns,
)

detector = DangerDetector(
    regions=resolve_region_patterns([], ["kyiv"]),
    localities=resolve_locality_patterns([], ["kyiv"], ["kyiv_nyvky"]),
)
assert detector.drone_danger("Шахед на Нивки!").danger
```

Preset IDs and patterns are in [`aerial_danger.location_presets.LOCATION_PRESETS`](src/aerial_danger/location_presets.py).
The registry loads bundled [JSON files](src/aerial_danger/locations), one per region,
into `RegionPreset` and `LocalityPreset` objects. Pattern sequences remain tuples.
Pass custom patterns as the first argument to each resolver to combine them with presets.
Each region and locality has an `id` matching its registry key, such as `kyiv_nyvky`.
The library has no display names or translations. Your application supplies labels for these IDs.

## Methods

```python
DangerDetector(regions: Iterable[str], localities: Iterable[str])
DangerDetector.validate_patterns(*pattern_groups: Iterable[str]) -> None

detector.danger(message: str) -> Detection
detector.irbm_danger(message: str) -> Detection
detector.mlrs_danger(message: str) -> Detection
detector.guided_bomb_danger(message: str) -> Detection
detector.ballistic_danger(message: str) -> Detection
detector.cruise_missile_danger(message: str) -> Detection
detector.drone_danger(message: str) -> Detection
detector.generic_danger(message: str) -> Detection
detector.is_safe(message: str) -> bool
detector.is_ignored(message: str) -> bool
```

`danger()` checks the danger types in the order listed above and returns the first match.
IRBM alerts need no location. Drones, MLRS, and guided bombs need a locality match.
Other alerts need a region or locality match.

### Detection results

Each detector method returns a `Detection` with the original `message`, a
`danger` boolean, and a `DetectionStatus`:

| Status    | `danger` | Meaning                               | Source state         |
| --------- | -------- | ------------------------------------- | -------------------- |
| `DANGER`  | `True`   | An active alert matched.              | Store the detection. |
| `SAFE`    | `False`  | Explicit all-clear wording matched.   | Clear the detection. |
| `IGNORED` | `False`  | Excluded wording or no alert matched. | Keep the detection.  |

Danger results include the threat type, matched text, and regex patterns.
Other results have no match details. IRBM results have no matched area.

`Detection(danger=..., message=...)` accepts an optional keyword-only `status`,
which defaults to `IGNORED`. Detector methods set both values explicitly.

### Wording checks

- `is_safe()` checks explicit all-clear wording.
- `is_ignored()` checks historical, forecast, and reconnaissance exclusions.

Both checks can match one message. Detection checks exclusions first, so a
historical report quoting an all-clear stays `IGNORED`. Unmatched messages also
return `IGNORED`, even when `is_ignored()` is `False`.

These checks do not confirm real-world safety. Invalid regexes raise `re.error`.

## Development

```sh
uv sync --locked
uv run pre-commit install
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv build --no-sources
```

After installation, pre-commit runs Ruff on Python files, checks JSON/YAML/TOML, and formats Markdown and configuration files before each commit.
See [contribution guidelines](CONTRIBUTING.md) for local integration setup.

## License

[MIT License](LICENSE.md) © [Denys Dovhan][denysdovhan].

[ci-badge-img]: https://img.shields.io/github/actions/workflow/status/denysdovhan/python-aerial-danger/ci.yml?branch=main&style=flat-square
[ci-badge-url]: https://github.com/denysdovhan/python-aerial-danger/actions/workflows/ci.yml
[pypi-badge-img]: https://img.shields.io/pypi/v/aerial-danger?style=flat-square
[pypi-badge-url]: https://pypi.org/project/aerial-danger/
[denysdovhan]: https://github.com/denysdovhan
