"""Location presets for chernivtsi oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

CHERNIVTSI_OBLAST_REGION: Final = RegionPreset(
    id="chernivtsi_oblast",
    patterns=(
        r"\bбуковин(а|и|і|у|ою)\b",
        r"\bчернівеччин(а|и|і|у|ою)\b",
        r"\bчернівецьк(а|ої|ій|у|ою) област(ь|і|ю)\b",
    ),
    localities={
        "chernivtsi_oblast_chernivtsi": LocalityPreset(
            id="chernivtsi_oblast_chernivtsi",
            patterns=(r"\bчернівц(і|ів|ям|ями|ях)\b",),
        ),
        "chernivtsi_oblast_khotyn": LocalityPreset(
            id="chernivtsi_oblast_khotyn",
            patterns=(r"\bхотин(а|у|ом|і)?\b",),
        ),
        "chernivtsi_oblast_kitsman": LocalityPreset(
            id="chernivtsi_oblast_kitsman",
            patterns=(r"\bкіцман(ь|я|ю|ем|і)\b",),
        ),
        "chernivtsi_oblast_novodnistrovsk": LocalityPreset(
            id="chernivtsi_oblast_novodnistrovsk",
            patterns=(r"\bноводністровськ(а|у|ом|і)?\b",),
        ),
    },
)
