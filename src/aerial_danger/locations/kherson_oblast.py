"""Location presets for kherson oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

KHERSON_OBLAST_REGION: Final = RegionPreset(
    id="kherson_oblast",
    patterns=(
        r"\bхерсонщин(а|и|і|у|ою)\b",
        r"\bхерсонськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
    ),
    localities={
        "kherson_oblast_arkhanhelske": LocalityPreset(
            id="kherson_oblast_arkhanhelske",
            patterns=(r"\bархангельськ(е|ого|ому|им|ім)\b",),
        ),
        "kherson_oblast_beryslav": LocalityPreset(
            id="kherson_oblast_beryslav",
            patterns=(r"\bберислав(а|у|ом|і)?\b",),
        ),
        "kherson_oblast_kherson": LocalityPreset(
            id="kherson_oblast_kherson", patterns=(r"\bхерсон(а|у|ом|і)?\b",)
        ),
        "kherson_oblast_stanislav": LocalityPreset(
            id="kherson_oblast_stanislav",
            patterns=(r"\bстаніслав(а|у|ом|і)?\b",),
        ),
        "kherson_oblast_vysokopillia": LocalityPreset(
            id="kherson_oblast_vysokopillia",
            patterns=(r"\bвисокопілл(я|ю|ям|і)\b",),
        ),
    },
)
