"""Location presets for lviv oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

LVIV_OBLAST_REGION: Final = RegionPreset(
    id="lviv_oblast",
    patterns=(
        r"\bльвівщин(а|и|і|у|ою)\b",
        r"\bльвівськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
    ),
    localities={
        "lviv_oblast_bibrka": LocalityPreset(
            id="lviv_oblast_bibrka",
            patterns=(r"\bбібр(ка|ки|ці|ку|кою)\b",),
        ),
        "lviv_oblast_lviv": LocalityPreset(
            id="lviv_oblast_lviv", patterns=(r"\bльв(ів|ова|ову|овом|ові)\b",)
        ),
        "lviv_oblast_stryi": LocalityPreset(
            id="lviv_oblast_stryi",
            patterns=(r"\bстри(й|я|ю|єм|ї)\b",),
        ),
        "lviv_oblast_zhovkva": LocalityPreset(
            id="lviv_oblast_zhovkva",
            patterns=(r"\bжовкв(а|и|і|у|ою)\b",),
        ),
        "lviv_oblast_zhydachiv": LocalityPreset(
            id="lviv_oblast_zhydachiv",
            patterns=(r"\bжидач(ів|ова|ову|овом|ові)\b",),
        ),
    },
)
