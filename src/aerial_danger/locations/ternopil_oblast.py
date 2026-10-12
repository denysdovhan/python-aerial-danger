"""Location presets for ternopil oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

TERNOPIL_OBLAST_REGION: Final = RegionPreset(
    id="ternopil_oblast",
    patterns=(
        r"\bтернопільщин(а|и|і|у|ою)\b",
        r"\bтернопільськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
    ),
    localities={
        "ternopil_oblast_ternopil": LocalityPreset(
            id="ternopil_oblast_ternopil",
            patterns=(r"\bтерноп(іль|оля|олю|олем|олі)\b",),
        ),
    },
)
