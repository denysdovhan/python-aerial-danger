"""Location presets for zhytomyr oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

ZHYTOMYR_OBLAST_REGION: Final = RegionPreset(
    id="zhytomyr_oblast",
    patterns=(
        r"\bжитомирщин(а|и|і|у|ою)\b",
        r"\bжитомирськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
    ),
    localities={
        "zhytomyr_oblast_berdychiv": LocalityPreset(
            id="zhytomyr_oblast_berdychiv",
            patterns=(r"\bбердич(ів|ева|еву|евом|еві)\b",),
        ),
        "zhytomyr_oblast_korosten": LocalityPreset(
            id="zhytomyr_oblast_korosten",
            patterns=(r"\bкоростен(ь|я|ем|і)\b",),
        ),
        "zhytomyr_oblast_ovruch": LocalityPreset(
            id="zhytomyr_oblast_ovruch", patterns=(r"\bовруч(а|у|ем|і)?\b",)
        ),
        "zhytomyr_oblast_zhytomyr": LocalityPreset(
            id="zhytomyr_oblast_zhytomyr", patterns=(r"\bжитомир(а|у|ом|і)?\b",)
        ),
    },
)
