"""Location presets for donetsk oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

DONETSK_OBLAST_REGION: Final = RegionPreset(
    id="donetsk_oblast",
    patterns=(
        r"\bдонеччин(а|и|і|у|ою)\b",
        r"\bдонецьк(а|ої|ій|у|ою) област(ь|і|ю)\b",
    ),
    localities={
        "donetsk_oblast_dobropillia": LocalityPreset(
            id="donetsk_oblast_dobropillia",
            patterns=(r"\bдобропілл(я|ю|ям|і)\b",),
        ),
        "donetsk_oblast_donetsk": LocalityPreset(
            id="donetsk_oblast_donetsk",
            patterns=(r"\bдонецьк(у|ом|і)?\b",),
        ),
        "donetsk_oblast_kramatorsk": LocalityPreset(
            id="donetsk_oblast_kramatorsk",
            patterns=(r"\bкраматорськ(а|у|ом|і)?\b",),
        ),
        "donetsk_oblast_novodonetske": LocalityPreset(
            id="donetsk_oblast_novodonetske",
            patterns=(r"\bноводонецьк(е|ого|ому|им|ім)\b",),
        ),
        "donetsk_oblast_sloviansk": LocalityPreset(
            id="donetsk_oblast_sloviansk",
            patterns=(r"\bслов['’ʼ]янськ(а|у|ом|і)?\b",),
        ),
    },
)
