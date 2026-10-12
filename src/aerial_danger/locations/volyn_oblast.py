"""Location presets for volyn oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

VOLYN_OBLAST_REGION: Final = RegionPreset(
    id="volyn_oblast",
    patterns=(
        r"\bволин(ь|і|ню)\b",
        r"\bволинськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
    ),
    localities={
        "volyn_oblast_lutsk": LocalityPreset(
            id="volyn_oblast_lutsk", patterns=(r"\bлуцьк(а|у|ом|ові)?\b",)
        ),
    },
)
