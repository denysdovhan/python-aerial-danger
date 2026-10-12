"""Location presets for rivne oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

RIVNE_OBLAST_REGION: Final = RegionPreset(
    id="rivne_oblast",
    patterns=(
        r"\bрівненщин(а|и|і|у|ою)\b",
        r"\bрівненськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
    ),
    localities={
        "rivne_oblast_rivne": LocalityPreset(
            id="rivne_oblast_rivne", patterns=(r"\bрівне\b",)
        ),
    },
)
