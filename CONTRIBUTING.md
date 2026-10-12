# Contributing

## Test matcher changes

Preserve exact alert text in tests, including punctuation, case, and line breaks.
Add non-matching examples for forecasts, reports of past events, and unrelated areas.
Run the commands in the [README](README.md#development) before opening a pull request.

## Edit location presets

Edit the region's JSON file in `src/aerial_danger/locations/`. Keep region filenames
and locality keys alphabetically sorted, and preserve pattern order. IDs must match
their filename or locality key and remain stable for saved application selections.

JSON regexes escape each backslash: write `"\\bкиїв\\b"`, not `"\bкиїв\b"`.
Use an optional `notes` string on a locality for matching rationale; the loader
does not expose these notes in the preset API. Run `uv run pytest` after edits.

## Test with Home Assistant

Clone `ha-aerial-danger` and `python-aerial-danger` into the same parent directory.
From `ha-aerial-danger`, run:

```sh
uv add --editable ../python-aerial-danger
scripts/test
scripts/develop --skip-pip-packages aerial-danger
```

uv records the editable path in `tool.uv.sources`; later `uv sync` and `uv run`
commands keep using the local code. Restart Home Assistant after changes.
The skip flag prevents HA from replacing the editable version.
Keep the source override and its lockfile changes out of commits.
To return to PyPI, remove that source entry, keep the published dependency pin,
and run `uv sync`.
