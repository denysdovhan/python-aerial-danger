"""Location presets for ternopil oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

TERNOPIL_OBLAST_REGION: Final = RegionPreset(
    id="ternopil_oblast",
    patterns=(
        r"\bтернопільщин(а|и|і|у|ою)\b",
        r"\bтернопільськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
    ),
    localities={
        "ternopil_oblast_chortkiv": LocalityPreset(
            id="ternopil_oblast_chortkiv",
            patterns=(r"\bчортк(ів|ова|ову|овом|ові)\b",),
        ),
        "ternopil_oblast_hrymailiv": LocalityPreset(
            id="ternopil_oblast_hrymailiv",
            patterns=(r"\bгримайл(ів|ова|ову|овом|ові)\b",),
        ),
        "ternopil_oblast_khorostkiv": LocalityPreset(
            id="ternopil_oblast_khorostkiv",
            patterns=(r"\bхоростк(ів|ова|ову|овом|ові)\b",),
        ),
        "ternopil_oblast_kozova": LocalityPreset(
            id="ternopil_oblast_kozova",
            patterns=(r"\bкозов(а|и|і|у|ою)\b",),
        ),
        "ternopil_oblast_kremenets": LocalityPreset(
            id="ternopil_oblast_kremenets",
            patterns=(r"\bкремен(ець|ця|цю|цем|ці)\b",),
        ),
        "ternopil_oblast_lanivtsi": LocalityPreset(
            id="ternopil_oblast_lanivtsi",
            patterns=(r"\bланівц(і|ів|ям|ями|ях)\b",),
        ),
        "ternopil_oblast_terebovlia": LocalityPreset(
            id="ternopil_oblast_terebovlia",
            patterns=(r"\bтеребовл(я|і|ю|ею)\b",),
        ),
        "ternopil_oblast_ternopil": LocalityPreset(
            id="ternopil_oblast_ternopil",
            patterns=(r"\bтерноп(іль|оля|олю|олем|олі)\b",),
        ),
        "ternopil_oblast_velyki_birky": LocalityPreset(
            id="ternopil_oblast_velyki_birky",
            patterns=(r"\bвелик(і|их|им|ими)\s+бір(ки|ок|кам|ками|ках)\b",),
        ),
        "ternopil_oblast_vyshnivets": LocalityPreset(
            id="ternopil_oblast_vyshnivets",
            patterns=(r"\bвишнів(ець|ця|цю|цем|ці)\b",),
        ),
    },
)
