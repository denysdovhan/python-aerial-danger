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
        "rivne_oblast_berezne": LocalityPreset(
            id="rivne_oblast_berezne",
            patterns=(r"\bберезн(е|ого|ому|им|ім)\b",),
        ),
        "rivne_oblast_dubno": LocalityPreset(
            id="rivne_oblast_dubno",
            patterns=(r"\bдубн(о|а|у|ом|і)\b",),
        ),
        "rivne_oblast_dubrovytsia": LocalityPreset(
            id="rivne_oblast_dubrovytsia",
            patterns=(r"\bдубровиц(я|і|ю|ею)\b",),
        ),
        "rivne_oblast_hoshcha": LocalityPreset(
            id="rivne_oblast_hoshcha",
            patterns=(r"\bгощ(а|і|у|ею)\b",),
        ),
        "rivne_oblast_klevan": LocalityPreset(
            id="rivne_oblast_klevan",
            patterns=(r"\bклеван(ь|я|ю|ем|і)\b",),
        ),
        "rivne_oblast_korets": LocalityPreset(
            id="rivne_oblast_korets",
            patterns=(r"\bкор(ець|ця|цю|цем|ці)\b",),
        ),
        "rivne_oblast_kostopil": LocalityPreset(
            id="rivne_oblast_kostopil",
            patterns=(r"\bкостоп(іль|оля|олю|олем|олі)\b",),
        ),
        "rivne_oblast_mizoch": LocalityPreset(
            id="rivne_oblast_mizoch",
            patterns=(r"\bмізоч(а|у|ем|і)?\b",),
        ),
        "rivne_oblast_rivne": LocalityPreset(
            id="rivne_oblast_rivne", patterns=(r"\bрівне\b",)
        ),
        "rivne_oblast_sarny": LocalityPreset(
            id="rivne_oblast_sarny",
            patterns=(r"\bсарн(и|ам|ами|ах)?\b",),
        ),
        "rivne_oblast_stepan": LocalityPreset(
            id="rivne_oblast_stepan",
            patterns=(r"\bстепан(ь|я|ю|ем|і)\b",),
        ),
        "rivne_oblast_tomashhorod": LocalityPreset(
            id="rivne_oblast_tomashhorod",
            patterns=(r"\bтомашгород(а|у|ом|і)?\b",),
        ),
        "rivne_oblast_varash": LocalityPreset(
            id="rivne_oblast_varash",
            patterns=(r"\bвараш(а|у|ем|і)?\b",),
        ),
        "rivne_oblast_zdolbuniv": LocalityPreset(
            id="rivne_oblast_zdolbuniv",
            patterns=(r"\bздолбун(ів|ова|ову|овом|ові)\b",),
        ),
    },
)
