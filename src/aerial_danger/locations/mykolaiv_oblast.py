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
        "mykolaiv_oblast_arbuzynka": LocalityPreset(
            id="mykolaiv_oblast_arbuzynka",
            patterns=(r"\bарбузин(ка|ки|ці|ку|кою)\b",),
        ),
        "mykolaiv_oblast_bashtanka": LocalityPreset(
            id="mykolaiv_oblast_bashtanka", patterns=(r"\bбаштанк(а|и|у|ою|і)\b",)
        ),
        "mykolaiv_oblast_bereznehuvate": LocalityPreset(
            id="mykolaiv_oblast_bereznehuvate",
            patterns=(r"\bберезнегуват(е|ого|ому|им|ім)\b",),
        ),
        "mykolaiv_oblast_bratske": LocalityPreset(
            id="mykolaiv_oblast_bratske",
            patterns=(r"\bбратськ(е|ого|ому|им|ім)\b",),
        ),
        "mykolaiv_oblast_kazanka": LocalityPreset(
            id="mykolaiv_oblast_kazanka",
            patterns=(r"\bказан(ка|ки|ці|ку|кою)\b",),
        ),
        "mykolaiv_oblast_kobleve": LocalityPreset(
            id="mykolaiv_oblast_kobleve",
            patterns=(r"\bкоблев(е|ого|ому|им|ім)\b",),
        ),
        "mykolaiv_oblast_kryve_ozero": LocalityPreset(
            id="mykolaiv_oblast_kryve_ozero",
            patterns=(r"\bкрив(е|ого|ому|им|ім)\s+озер(о|а|у|ом|і)\b",),
        ),
        "mykolaiv_oblast_morske": LocalityPreset(
            id="mykolaiv_oblast_morske",
            patterns=(r"\bморськ(е|ого|ому|им|ім)\b",),
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
        "mykolaiv_oblast_olshanske": LocalityPreset(
            id="mykolaiv_oblast_olshanske",
            patterns=(r"\bольшанськ(е|ого|ому|им|ім)\b",),
        ),
        "mykolaiv_oblast_pervomaisk": LocalityPreset(
            id="mykolaiv_oblast_pervomaisk",
            patterns=(r"\bпервомайськ(а|у|ом|і)?\b",),
        ),
        "mykolaiv_oblast_pivdennoukrainsk": LocalityPreset(
            id="mykolaiv_oblast_pivdennoukrainsk",
            patterns=(r"\bпівденноукраїнськ(а|у|ом|і)?\b",),
        ),
        "mykolaiv_oblast_rybakivka": LocalityPreset(
            id="mykolaiv_oblast_rybakivka",
            patterns=(r"\bрибаків(ка|ки|ці|ку|кою)\b",),
        ),
        "mykolaiv_oblast_snigurivka": LocalityPreset(
            id="mykolaiv_oblast_snigurivka",
            patterns=(r"\bснігурівк(у|и|а)\b",),
        ),
        "mykolaiv_oblast_tokarivka": LocalityPreset(
            id="mykolaiv_oblast_tokarivka",
            patterns=(r"\bтокарів(ка|ки|ці|ку|кою)\b",),
        ),
        "mykolaiv_oblast_trykhaty": LocalityPreset(
            id="mykolaiv_oblast_trykhaty",
            patterns=(r"\bтрихат(и|ам|ами|ах)?\b",),
        ),
        "mykolaiv_oblast_veselynove": LocalityPreset(
            id="mykolaiv_oblast_veselynove",
            patterns=(r"\bвеселинов(е|ого|ому|им|ім)\b",),
        ),
        "mykolaiv_oblast_voskresenske": LocalityPreset(
            id="mykolaiv_oblast_voskresenske",
            patterns=(r"\bвоскресенськ(е|ого|ому|им|ім)\b",),
        ),
        "mykolaiv_oblast_voznesensk": LocalityPreset(
            id="mykolaiv_oblast_voznesensk",
            patterns=(r"\bвознесенськ(а|у|ом|і)?\b",),
        ),
        "mykolaiv_oblast_vozsiiatske": LocalityPreset(
            id="mykolaiv_oblast_vozsiiatske",
            patterns=(r"\bвозсіятськ(е|ого|ому|им|ім)\b",),
        ),
        "mykolaiv_oblast_yelanets": LocalityPreset(
            id="mykolaiv_oblast_yelanets",
            patterns=(r"\bєлан(ець|ця|цю|цем|ці)\b",),
        ),
    },
)
