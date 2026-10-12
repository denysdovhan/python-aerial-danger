"""Location presets for kirovohrad oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

KIROVOHRAD_OBLAST_REGION: Final = RegionPreset(
    id="kirovohrad_oblast",
    patterns=(
        r"\bкіровоградщин(а|и|і|у|ою)\b",
        r"\bкіровоградськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
    ),
    localities={
        "kirovohrad_oblast_kropyvnytskyi": LocalityPreset(
            id="kirovohrad_oblast_kropyvnytskyi",
            patterns=(r"\bкропивницьк(ий|ого|ому|им|ім)\b", r"\bкроп\b"),
        ),
    },
)
