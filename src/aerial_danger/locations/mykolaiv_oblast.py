"""Location presets for mykolaiv oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

MYKOLAIV_OBLAST_REGION: Final = RegionPreset(
    id="mykolaiv_oblast",
    patterns=(
        r"\bмиколаївщин(а|и|і|у|ою)\b",
        r"\bмиколаївськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
    ),
    localities={
        "mykolaiv_oblast_bashtanka": LocalityPreset(
            id="mykolaiv_oblast_bashtanka", patterns=(r"\bбаштанк(а|и|у|ою|і)\b",)
        ),
        "mykolaiv_oblast_mykolaiv": LocalityPreset(
            id="mykolaiv_oblast_mykolaiv",
            patterns=(r"\bмикола(їв|єва|єві|єву|євом)\b",),
        ),
        "mykolaiv_oblast_novyi_buh": LocalityPreset(
            id="mykolaiv_oblast_novyi_buh",
            patterns=(r"\bнов(ий|ого|ому|им|ім) буг(а|у|ом|і)?\b",),
        ),
        "mykolaiv_oblast_ochakiv": LocalityPreset(
            id="mykolaiv_oblast_ochakiv",
            patterns=(r"\bочак(ів|ова|ову|овом|ові)\b",),
        ),
        "mykolaiv_oblast_snigurivka": LocalityPreset(
            id="mykolaiv_oblast_snigurivka",
            patterns=(r"\bснігурівк(у|и|а)\b",),
        ),
        "mykolaiv_oblast_voznesensk": LocalityPreset(
            id="mykolaiv_oblast_voznesensk",
            patterns=(r"\bвознесенськ(а|у|ом|і)?\b",),
        ),
    },
)
