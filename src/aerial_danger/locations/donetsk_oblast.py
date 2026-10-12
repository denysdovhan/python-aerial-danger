"""Location presets for donetsk oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

DONETSK_OBLAST_REGION: Final = RegionPreset(
    id="donetsk_oblast",
    patterns=(
        r"\bдонеччин(а|и|і|у|ою)\b",
        r"\bдонецьк(а|ої|ій|у|ою) област(ь|і|ю)\b",
    ),
    localities={
        "donetsk_oblast_donetsk": LocalityPreset(
            id="donetsk_oblast_donetsk",
            patterns=(r"\bдонецьк(у|ом|і)?\b",),
        ),
    },
)
