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
```

`danger()` checks the danger types in the order listed above and returns the first match.
IRBM alerts need no location. Drones, MLRS, and guided bombs need a locality match.
Other alerts need a region or locality match.

The result tells you whether danger matched, its type, and the original message.
It also includes the matched text and regex patterns. With no match, `danger` is
`False` and the match details are `None`. IRBM results have no matched area.

`is_safe()` checks for wording that blocks a danger match. It does not confirm that
an area is safe. Invalid regex patterns raise `re.error`.

## Development

```sh
uv sync --locked
uv run pre-commit install
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv build --no-sources
```

After installation, pre-commit runs Ruff linting and formatting on changed Python files before each commit.
See [contribution guidelines](CONTRIBUTING.md) for local integration setup.

## License

[MIT License](LICENSE.md) © [Denys Dovhan][denysdovhan].

[ci-badge-img]: https://img.shields.io/github/actions/workflow/status/denysdovhan/python-aerial-danger/ci.yml?branch=main&style=flat-square
[ci-badge-url]: https://github.com/denysdovhan/python-aerial-danger/actions/workflows/ci.yml
[pypi-badge-img]: https://img.shields.io/pypi/v/aerial-danger?style=flat-square
[pypi-badge-url]: https://pypi.org/project/aerial-danger/
[denysdovhan]: https://github.com/denysdovhan
