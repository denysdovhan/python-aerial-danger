"""Location presets for poltava oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

POLTAVA_OBLAST_REGION: Final = RegionPreset(
    id="poltava_oblast",
    patterns=(
        r"\bполтавщин(а|и|і|у|ою)\b",
        r"\bполтавськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
    ),
    localities={
        "poltava_oblast_bilyky": LocalityPreset(
            id="poltava_oblast_bilyky",
            patterns=(r"\bбілик(и|ів|ам|ами|ах)\b",),
        ),
        "poltava_oblast_chornukhy": LocalityPreset(
            id="poltava_oblast_chornukhy",
            patterns=(r"\bчорну(хи|х|хам|хами|хах)\b",),
        ),
        "poltava_oblast_chutove": LocalityPreset(
            id="poltava_oblast_chutove",
            patterns=(r"\bчутов(е|ого|ому|им|ім)\b",),
        ),
        "poltava_oblast_dykanka": LocalityPreset(
            id="poltava_oblast_dykanka", patterns=(r"\bдиканьк(а|и|у|ою|і)\b",)
        ),
        "poltava_oblast_hadiach": LocalityPreset(
            id="poltava_oblast_hadiach", patterns=(r"\bгадяч(а)?\b",)
        ),
        "poltava_oblast_hlobyne": LocalityPreset(
            id="poltava_oblast_hlobyne", patterns=(r"\bглобин(е|ого|ому|им|ім)\b",)
        ),
        "poltava_oblast_hoholeve": LocalityPreset(
            id="poltava_oblast_hoholeve",
            patterns=(r"\bгоголев(е|ого|ому|им|ім)\b",),
        ),
        "poltava_oblast_horishni_plavni": LocalityPreset(
            id="poltava_oblast_horishni_plavni",
            patterns=(r"\bгорішн(і|іх|ім|іми)\s+плавн(і|ів|ям|ями|ях)\b",),
        ),
        "poltava_oblast_hradyzk": LocalityPreset(
            id="poltava_oblast_hradyzk",
            patterns=(r"\bградизьк(а|у|ом|і)?\b",),
        ),
        "poltava_oblast_hrebinka": LocalityPreset(
            id="poltava_oblast_hrebinka", patterns=(r"\bгребінк(а|и|у|ою|і)\b",)
        ),
        "poltava_oblast_karlivka": LocalityPreset(
            id="poltava_oblast_karlivka",
            patterns=(r"\bкарлів(ка|ки|ці|ку|кою)\b",),
        ),
        "poltava_oblast_khorol": LocalityPreset(
            id="poltava_oblast_khorol",
            patterns=(r"\bхорол(а|у|ом|і)?\b",),
        ),
        "poltava_oblast_kobeliaky": LocalityPreset(
            id="poltava_oblast_kobeliaky",
            patterns=(r"\bкобеляк(и|ів|ам|ами|ах)\b",),
        ),
        "poltava_oblast_komyshnia": LocalityPreset(
            id="poltava_oblast_komyshnia",
            patterns=(r"\bкомишн(я|і|ю|ею)\b",),
        ),
        "poltava_oblast_kotelva": LocalityPreset(
            id="poltava_oblast_kotelva", patterns=(r"\bкотельв(а|и|у|ою|і)\b",)
        ),
        "poltava_oblast_kozelshchyna": LocalityPreset(
            id="poltava_oblast_kozelshchyna",
            patterns=(r"\bкозельщин(а|и|і|у|ою)\b",),
        ),
        "poltava_oblast_kremenchuk": LocalityPreset(
            id="poltava_oblast_kremenchuk",
            patterns=(r"\bкременч(ук|ука|уку|уком|уці)\b",),
        ),
        "poltava_oblast_lokhvytsia": LocalityPreset(
            id="poltava_oblast_lokhvytsia",
            patterns=(r"\bлохвиц(я|і|ю|ею)\b",),
        ),
        "poltava_oblast_lubny": LocalityPreset(
            id="poltava_oblast_lubny", patterns=(r"\bлуб(ни|ен|нів|ням|нями|нях)\b",)
        ),
        "poltava_oblast_mashivka": LocalityPreset(
            id="poltava_oblast_mashivka",
            patterns=(r"\bмашів(ка|ки|ці|ку|кою)\b",),
        ),
        "poltava_oblast_myrhorod": LocalityPreset(
            id="poltava_oblast_myrhorod", patterns=(r"\bмиргород(а|у|ом|і)?\b",)
        ),
        "poltava_oblast_novi_sanzhary": LocalityPreset(
            id="poltava_oblast_novi_sanzhary",
            patterns=(r"\bнов(і|их|им|ими) санжар(и|ів|ам|ами|ах)\b",),
        ),
        "poltava_oblast_novoorzhytske": LocalityPreset(
            id="poltava_oblast_novoorzhytske",
            patterns=(r"\bновооржицьк(е|ого|ому|им|ім)\b",),
        ),
        "poltava_oblast_opishnia": LocalityPreset(
            id="poltava_oblast_opishnia",
            patterns=(r"\bопішн(я|і|ю|ею)\b",),
        ),
        "poltava_oblast_poltava": LocalityPreset(
            id="poltava_oblast_poltava", patterns=(r"\bполтав(а|и|і|у|ою)\b",)
        ),
        "poltava_oblast_pyriatyn": LocalityPreset(
            id="poltava_oblast_pyriatyn", patterns=(r"\bпирятин(а)?\b",)
        ),
        "poltava_oblast_reshetylivka": LocalityPreset(
            id="poltava_oblast_reshetylivka",
            patterns=(r"\bрешетилівк(а|и|у|ою|і)\b",),
        ),
        "poltava_oblast_romodan": LocalityPreset(
            id="poltava_oblast_romodan",
            patterns=(r"\bромодан(а|у|ом|і)?\b",),
        ),
        "poltava_oblast_shyshaky": LocalityPreset(
            id="poltava_oblast_shyshaky", patterns=(r"\bшишак(и|ів|ам|ами|ах)\b",)
        ),
        "poltava_oblast_skorokhodove": LocalityPreset(
            id="poltava_oblast_skorokhodove",
            patterns=(r"\bскороходов(е|ого|ому|им|ім)\b",),
        ),
        "poltava_oblast_velyka_bahachka": LocalityPreset(
            id="poltava_oblast_velyka_bahachka",
            patterns=(r"\bвелик(а|ої|ій|у|ою)\s+багач(ка|ки|ці|ку|кою)\b",),
        ),
        "poltava_oblast_velyki_sorochyntsi": LocalityPreset(
            id="poltava_oblast_velyki_sorochyntsi",
            patterns=(r"\bвелик(і|их|им|ими) сорочинц(і|ів|ям|ями|ях)\b",),
        ),
        "poltava_oblast_vyrishalne": LocalityPreset(
            id="poltava_oblast_vyrishalne",
            patterns=(r"\bвирішальн(е|ого|ому|им|ім)\b",),
        ),
        "poltava_oblast_zavodske": LocalityPreset(
            id="poltava_oblast_zavodske",
            patterns=(r"\bзаводськ(е|ого|ому|им|ім)\b",),
        ),
        "poltava_oblast_zinkiv": LocalityPreset(
            id="poltava_oblast_zinkiv", patterns=(r"\bзіньків\b",)
        ),
    },
)
