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
        "kirovohrad_oblast_adzhamka": LocalityPreset(
            id="kirovohrad_oblast_adzhamka",
            patterns=(r"\bаджам(ка|ки|ці|ку|кою)\b",),
        ),
        "kirovohrad_oblast_blahovishchenske": LocalityPreset(
            id="kirovohrad_oblast_blahovishchenske",
            patterns=(r"\bблаговіщенськ(е|ого|ому|им|ім)\b",),
        ),
        "kirovohrad_oblast_bobrynets": LocalityPreset(
            id="kirovohrad_oblast_bobrynets",
            patterns=(r"\bбобрин(ець|ця|цю|цем|ці)\b",),
        ),
        "kirovohrad_oblast_dolynska": LocalityPreset(
            id="kirovohrad_oblast_dolynska",
            patterns=(r"\bдолинськ(а|ої|ій|у|ою)\b",),
        ),
        "kirovohrad_oblast_haivoron": LocalityPreset(
            id="kirovohrad_oblast_haivoron",
            patterns=(r"\bгайворон(а|у|ом|і)?\b",),
        ),
        "kirovohrad_oblast_holovanivsk": LocalityPreset(
            id="kirovohrad_oblast_holovanivsk",
            patterns=(r"\bголованівськ(а|у|ом|і)?\b",),
        ),
        "kirovohrad_oblast_kamianets": LocalityPreset(
            id="kirovohrad_oblast_kamianets",
            patterns=(r"\bкам['’ʼ]ян(ець|ця|цю|цем|ці)\b",),
        ),
        "kirovohrad_oblast_khmelove": LocalityPreset(
            id="kirovohrad_oblast_khmelove",
            patterns=(r"\bхмельов(е|ого|ому|им|ім)\b",),
        ),
        "kirovohrad_oblast_kompaniivka": LocalityPreset(
            id="kirovohrad_oblast_kompaniivka",
            patterns=(r"\bкомпаніїв(ка|ки|ці|ку|кою)\b",),
        ),
        "kirovohrad_oblast_kropyvnytskyi": LocalityPreset(
            id="kirovohrad_oblast_kropyvnytskyi",
            patterns=(r"\bкропивницьк(ий|ого|ому|им|ім)\b", r"\bкроп\b"),
        ),
        "kirovohrad_oblast_lisove": LocalityPreset(
            id="kirovohrad_oblast_lisove",
            patterns=(r"\bлісов(е|ого|ому|им|ім)\b",),
        ),
        "kirovohrad_oblast_mala_vyska": LocalityPreset(
            id="kirovohrad_oblast_mala_vyska",
            patterns=(r"\bмал(а|ої|ій|у|ою)\s+вис(ка|ки|ці|ку|кою)\b",),
        ),
        "kirovohrad_oblast_nova_praha": LocalityPreset(
            id="kirovohrad_oblast_nova_praha",
            patterns=(r"\bнов(а|ої|ій|у|ою)\s+пра(га|ги|зі|гу|гою)\b",),
        ),
        "kirovohrad_oblast_novoarkhanhelsk": LocalityPreset(
            id="kirovohrad_oblast_novoarkhanhelsk",
            patterns=(r"\bновоархангельськ(а|у|ом|і)?\b",),
        ),
        "kirovohrad_oblast_novomyrhorod": LocalityPreset(
            id="kirovohrad_oblast_novomyrhorod",
            patterns=(r"\bновомиргород(а|у|ом|і)?\b",),
        ),
        "kirovohrad_oblast_novoukrainka": LocalityPreset(
            id="kirovohrad_oblast_novoukrainka",
            patterns=(r"\bновоукраїн(ка|ки|ці|ку|кою)\b",),
        ),
        "kirovohrad_oblast_oleksandriia": LocalityPreset(
            id="kirovohrad_oblast_oleksandriia",
            patterns=(r"\bолександрі(я|ї|ю|єю)\b",),
        ),
        "kirovohrad_oblast_oleksandriiske": LocalityPreset(
            id="kirovohrad_oblast_oleksandriiske",
            patterns=(r"\bолександрійськ(е|ого|ому|им|ім)\b",),
        ),
        "kirovohrad_oblast_onufriivka": LocalityPreset(
            id="kirovohrad_oblast_onufriivka",
            patterns=(r"\bонуфріїв(ка|ки|ці|ку|кою)\b",),
        ),
        "kirovohrad_oblast_pantaivka": LocalityPreset(
            id="kirovohrad_oblast_pantaivka",
            patterns=(r"\bпантаїв(ка|ки|ці|ку|кою)\b",),
        ),
        "kirovohrad_oblast_pavlysh": LocalityPreset(
            id="kirovohrad_oblast_pavlysh",
            patterns=(r"\bпавлиш(а|у|ем|і)?\b",),
        ),
        "kirovohrad_oblast_petrove": LocalityPreset(
            id="kirovohrad_oblast_petrove",
            patterns=(r"\bпетров(е|ого|ому|им|ім)\b",),
        ),
        "kirovohrad_oblast_pomichna": LocalityPreset(
            id="kirovohrad_oblast_pomichna",
            patterns=(r"\bпомічн(а|ої|ій|у|ою)\b",),
        ),
        "kirovohrad_oblast_smoline": LocalityPreset(
            id="kirovohrad_oblast_smoline",
            patterns=(r"\bсмолін(е|ого|ому|им|ім)\b",),
        ),
        "kirovohrad_oblast_sozonivka": LocalityPreset(
            id="kirovohrad_oblast_sozonivka",
            patterns=(r"\bсозонів(ка|ки|ці|ку|кою)\b",),
        ),
        "kirovohrad_oblast_svitlovodsk": LocalityPreset(
            id="kirovohrad_oblast_svitlovodsk",
            patterns=(r"\bсвітловодськ(а|у|ом|і)?\b",),
        ),
        "kirovohrad_oblast_tsybuleve": LocalityPreset(
            id="kirovohrad_oblast_tsybuleve",
            patterns=(r"\bцибулев(е|ого|ому|им|ім)\b",),
        ),
        "kirovohrad_oblast_ustynivka": LocalityPreset(
            id="kirovohrad_oblast_ustynivka",
            patterns=(r"\bустинів(ка|ки|ці|ку|кою)\b",),
        ),
        "kirovohrad_oblast_velyka_vyska": LocalityPreset(
            id="kirovohrad_oblast_velyka_vyska",
            patterns=(r"\bвелик(а|ої|ій|у|ою)\s+вис(ка|ки|ці|ку|кою)\b",),
        ),
        "kirovohrad_oblast_vilshanka": LocalityPreset(
            id="kirovohrad_oblast_vilshanka",
            patterns=(r"\bвільшан(ка|ки|ці|ку|кою)\b",),
        ),
    },
)
