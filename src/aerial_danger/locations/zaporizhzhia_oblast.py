"""Location presets for zaporizhzhia oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

ZAPORIZHZHIA_OBLAST_REGION: Final = RegionPreset(
    id="zaporizhzhia_oblast",
    patterns=(r"\bзапорізьк(а|ої|ій|у|ою) област(ь|і|ю)\b",),
    localities={
        "zaporizhzhia_oblast_komyshuvakha": LocalityPreset(
            id="zaporizhzhia_oblast_komyshuvakha",
            patterns=(r"\bкомишувах(а|и|і|у|ою)\b",),
        ),
        "zaporizhzhia_oblast_orikhiv": LocalityPreset(
            id="zaporizhzhia_oblast_orikhiv",
            patterns=(r"\bоріх(ів|ова|ову|ові|овом)\b",),
        ),
        "zaporizhzhia_oblast_sotsmisto": LocalityPreset(
            id="zaporizhzhia_oblast_sotsmisto",
            patterns=(r"\bсоцміст(о|ом|т)\b",),
        ),
        "zaporizhzhia_oblast_vilniansk": LocalityPreset(
            id="zaporizhzhia_oblast_vilniansk",
            patterns=(r"\bвільнянськ(а|у|і|ом)?\b",),
        ),
        "zaporizhzhia_oblast_zaporizhzhia": LocalityPreset(
            id="zaporizhzhia_oblast_zaporizhzhia",
            patterns=(
                r"\bзапоріжж(я|і|ю|ям)\b",
                r"\bзп\b",
            ),
        ),
    },
)
