# Contributing

## Test matcher changes

Preserve exact alert text in tests, including punctuation, case, and line breaks.
Add non-matching examples for forecasts, reports of past events, and unrelated areas.
Run the commands in the [README](README.md#development) before opening a pull request.

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
