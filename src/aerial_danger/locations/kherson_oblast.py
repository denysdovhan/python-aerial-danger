"""Location presets for kherson oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

KHERSON_OBLAST_REGION: Final = RegionPreset(
    id="kherson_oblast",
    patterns=(
        r"\bхерсонщин(а|и|і|у|ою)\b",
        r"\bхерсонськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
    ),
    localities={
        "kherson_oblast_kherson": LocalityPreset(
            id="kherson_oblast_kherson", patterns=(r"\bхерсон(а|у|ом|і)?\b",)
        ),
    },
)
