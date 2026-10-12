"""Location presets for zakarpattia oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

ZAKARPATTIA_OBLAST_REGION: Final = RegionPreset(
    id="zakarpattia_oblast",
    patterns=(r"\bзакарпатськ(а|ої|ій|у|ою) област(ь|і|ю)\b",),
    localities={
        "zakarpattia_oblast_uzhhorod": LocalityPreset(
            id="zakarpattia_oblast_uzhhorod", patterns=(r"\bужгород(а|у|ом|і)?\b",)
        ),
    },
)
