"""Location presets for luhansk oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

LUHANSK_OBLAST_REGION: Final = RegionPreset(
    id="luhansk_oblast",
    patterns=(
        r"\bлуганщин(а|и|і|у|ою)\b",
        r"\bлуганськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
    ),
    localities={
        "luhansk_oblast_luhansk": LocalityPreset(
            id="luhansk_oblast_luhansk",
            patterns=(r"\bлуганськ(у|ом|і)?\b",),
        ),
    },
)
