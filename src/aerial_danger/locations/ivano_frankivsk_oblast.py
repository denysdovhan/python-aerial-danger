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
        "ivano_frankivsk_oblast_burshtyn": LocalityPreset(
            id="ivano_frankivsk_oblast_burshtyn",
            patterns=(r"\bбурштин(а|у|ом|і)?\b",),
        ),
        "ivano_frankivsk_oblast_ivano_frankivsk": LocalityPreset(
            id="ivano_frankivsk_oblast_ivano_frankivsk",
            patterns=(r"\bівано-франківськ(у|ом|і)?\b",),
        ),
        "ivano_frankivsk_oblast_kalush": LocalityPreset(
            id="ivano_frankivsk_oblast_kalush",
            patterns=(r"\bкалуш(а|у|ем|і)?\b",),
        ),
        "ivano_frankivsk_oblast_kolomyia": LocalityPreset(
            id="ivano_frankivsk_oblast_kolomyia",
            patterns=(r"\bколоми(я|ї|ю|єю)\b",),
        ),
        "ivano_frankivsk_oblast_rohatyn": LocalityPreset(
            id="ivano_frankivsk_oblast_rohatyn",
            patterns=(r"\bрогатин(а|у|ом|і)?\b",),
        ),
    },
)
