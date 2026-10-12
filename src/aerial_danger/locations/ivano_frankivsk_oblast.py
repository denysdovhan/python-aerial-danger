"""Location presets for ivano frankivsk oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

IVANO_FRANKIVSK_OBLAST_REGION: Final = RegionPreset(
    id="ivano_frankivsk_oblast",
    patterns=(
        r"\bфранківщин(а|и|і|у|ою)\b",
        r"\bівано-франківщин(а|и|і|у|ою)\b",
        r"\bівано-франківськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
    ),
    localities={
        "ivano_frankivsk_oblast_ivano_frankivsk": LocalityPreset(
            id="ivano_frankivsk_oblast_ivano_frankivsk",
            patterns=(r"\bівано-франківськ(у|ом|і)?\b",),
        ),
    },
)
