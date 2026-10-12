"""Location presets for dnipropetrovsk oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

DNIPROPETROVSK_OBLAST_REGION: Final = RegionPreset(
    id="dnipropetrovsk_oblast",
    patterns=(
        r"\bдніпропетровщин(а|и|і|у|ою)\b",
        r"\bдніпропетровськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
    ),
    localities={
        "dnipropetrovsk_oblast_apostolove": LocalityPreset(
            id="dnipropetrovsk_oblast_apostolove",
            patterns=(r"\bапостолов(е|ого|ому|им|ім)\b",),
        ),
        "dnipropetrovsk_oblast_aviatorske": LocalityPreset(
            id="dnipropetrovsk_oblast_aviatorske",
            patterns=(r"\bавіаторськ(е|ого|ому|им|ім)\b",),
        ),
        "dnipropetrovsk_oblast_bozhedarivka": LocalityPreset(
            id="dnipropetrovsk_oblast_bozhedarivka",
            patterns=(r"\bбожедарів(ка|ки|ці|ку|кою)\b",),
        ),
        "dnipropetrovsk_oblast_chaplyne": LocalityPreset(
            id="dnipropetrovsk_oblast_chaplyne",
            patterns=(r"\bчаплин(е|ого|ому|им|ім)\b",),
        ),
        "dnipropetrovsk_oblast_cherkaske": LocalityPreset(
            id="dnipropetrovsk_oblast_cherkaske",
            patterns=(r"\bчеркаськ(е|ого|ому|им|ім)\b",),
        ),
        "dnipropetrovsk_oblast_dnipro": LocalityPreset(
            id="dnipropetrovsk_oblast_dnipro", patterns=(r"\bдніпр(о|а|у|і|ом)\b",)
        ),
        "dnipropetrovsk_oblast_dorohe": LocalityPreset(
            id="dnipropetrovsk_oblast_dorohe",
            patterns=(r"\bдорог(е|ого|ому|им|ім)\b",),
        ),
        "dnipropetrovsk_oblast_doslidne": LocalityPreset(
            id="dnipropetrovsk_oblast_doslidne",
            patterns=(r"\bдослідн(е|ого|ому|им|ім)\b",),
        ),
        "dnipropetrovsk_oblast_hirnytske": LocalityPreset(
            id="dnipropetrovsk_oblast_hirnytske", patterns=(r"\bгірницьке\b",)
        ),
        "dnipropetrovsk_oblast_hubynykha": LocalityPreset(
            id="dnipropetrovsk_oblast_hubynykha",
            patterns=(r"\bгубини(ха|хи|сі|ху|хою)\b",),
        ),
        "dnipropetrovsk_oblast_kamianske": LocalityPreset(
            id="dnipropetrovsk_oblast_kamianske",
            patterns=(r"\bкам['’ʼ]?янськ(е|ого|ому|им|ім)\b",),
        ),
        "dnipropetrovsk_oblast_karnaukhivka": LocalityPreset(
            id="dnipropetrovsk_oblast_karnaukhivka",
            patterns=(r"\bкарнаухів(ка|ки|ці|ку|кою)\b",),
        ),
        "dnipropetrovsk_oblast_krynychky": LocalityPreset(
            id="dnipropetrovsk_oblast_krynychky",
            patterns=(r"\bкринич(ки|ок|кам|ками|ках)\b",),
        ),
        "dnipropetrovsk_oblast_kryvyi_rih": LocalityPreset(
            id="dnipropetrovsk_oblast_kryvyi_rih",
            patterns=(r"\bкрив(ий|ого|ому|им) р(іг|огу|озі|огом)\b",),
        ),
        "dnipropetrovsk_oblast_kurylivka": LocalityPreset(
            id="dnipropetrovsk_oblast_kurylivka",
            patterns=(r"\bкурилів(ка|ки|ці|ку|кою)\b",),
        ),
        "dnipropetrovsk_oblast_lykhivka": LocalityPreset(
            id="dnipropetrovsk_oblast_lykhivka",
            patterns=(r"\bлихів(ка|ки|ці|ку|кою)\b",),
        ),
        "dnipropetrovsk_oblast_marhanets": LocalityPreset(
            id="dnipropetrovsk_oblast_marhanets",
            patterns=(r"\bмарган(ець|ця|цю|цем|ці)\b",),
        ),
        "dnipropetrovsk_oblast_mezhova": LocalityPreset(
            id="dnipropetrovsk_oblast_mezhova",
            patterns=(r"\bмежов(а|ої|ій|у|ою)\b",),
        ),
        "dnipropetrovsk_oblast_nikopol": LocalityPreset(
            id="dnipropetrovsk_oblast_nikopol",
            patterns=(r"\bнікопол(ь|я|ем)\b",),
        ),
        "dnipropetrovsk_oblast_obukhivka": LocalityPreset(
            id="dnipropetrovsk_oblast_obukhivka",
            patterns=(r"\bобухів(ка|ки|ці|ку|кою)\b",),
        ),
        "dnipropetrovsk_oblast_pavlohrad": LocalityPreset(
            id="dnipropetrovsk_oblast_pavlohrad",
            patterns=(r"\bпавлоград(а|у|і|ом)?\b",),
        ),
        "dnipropetrovsk_oblast_pereshchepyne": LocalityPreset(
            id="dnipropetrovsk_oblast_pereshchepyne",
            patterns=(r"\bперещепин(е|ого|ому|им|ім)\b",),
        ),
        "dnipropetrovsk_oblast_petropavlivka": LocalityPreset(
            id="dnipropetrovsk_oblast_petropavlivka",
            patterns=(r"\bпетропавлів(ка|ки|ці|ку|кою)\b",),
        ),
        "dnipropetrovsk_oblast_petrykivka": LocalityPreset(
            id="dnipropetrovsk_oblast_petrykivka",
            patterns=(r"\bпетриків(ка|ки|ці|ку|кою)\b",),
        ),
        "dnipropetrovsk_oblast_pokrov": LocalityPreset(
            id="dnipropetrovsk_oblast_pokrov",
            patterns=(r"\bпокров(а|у|ом|і)?\b",),
        ),
        "dnipropetrovsk_oblast_pokrovske": LocalityPreset(
            id="dnipropetrovsk_oblast_pokrovske",
            patterns=(r"\bпокровськ(е|ого|ому|им|ім)\b",),
        ),
        "dnipropetrovsk_oblast_prosiana": LocalityPreset(
            id="dnipropetrovsk_oblast_prosiana",
            patterns=(r"\bпросян(а|ої|ій|у|ою)\b",),
        ),
        "dnipropetrovsk_oblast_pysmenne": LocalityPreset(
            id="dnipropetrovsk_oblast_pysmenne",
            patterns=(r"\bписьменн(е|ого|ому|им|ім)\b",),
        ),
        "dnipropetrovsk_oblast_radushne": LocalityPreset(
            id="dnipropetrovsk_oblast_radushne",
            patterns=(r"\bрадушн(е|ого|ому|им|ім)\b",),
        ),
        "dnipropetrovsk_oblast_samar": LocalityPreset(
            id="dnipropetrovsk_oblast_samar", patterns=(r"\bсамар(а|у|ом|і)?\b",)
        ),
        "dnipropetrovsk_oblast_shakhtarske": LocalityPreset(
            id="dnipropetrovsk_oblast_shakhtarske",
            patterns=(r"\bшахтарське\b",),
        ),
        "dnipropetrovsk_oblast_shyroke": LocalityPreset(
            id="dnipropetrovsk_oblast_shyroke",
            patterns=(r"\bширок(е|ого|ому|им|ім)\b",),
        ),
        "dnipropetrovsk_oblast_slavhorod": LocalityPreset(
            id="dnipropetrovsk_oblast_slavhorod",
            patterns=(r"\bславгород(а|у|ом|і)?\b",),
        ),
        "dnipropetrovsk_oblast_solone": LocalityPreset(
            id="dnipropetrovsk_oblast_solone", patterns=(r"\bсолоне\b",)
        ),
        "dnipropetrovsk_oblast_synelnykove": LocalityPreset(
            id="dnipropetrovsk_oblast_synelnykove",
            patterns=(r"\bсинельник(ове|ового|ова)\b",),
        ),
        "dnipropetrovsk_oblast_ternivka": LocalityPreset(
            id="dnipropetrovsk_oblast_ternivka",
            patterns=(r"\bтернів(ка|ки|ці|ку|кою)\b",),
        ),
        "dnipropetrovsk_oblast_tsarychanka": LocalityPreset(
            id="dnipropetrovsk_oblast_tsarychanka",
            patterns=(r"\bцаричан(ка|ки|ці|ку|кою)\b",),
        ),
        "dnipropetrovsk_oblast_vasylkivka": LocalityPreset(
            id="dnipropetrovsk_oblast_vasylkivka",
            patterns=(r"\bвасильківк(а|и|у|ою|і)\b",),
        ),
        "dnipropetrovsk_oblast_verkhivtseve": LocalityPreset(
            id="dnipropetrovsk_oblast_verkhivtseve",
            patterns=(r"\bверхівцев(е|ого|ому|им|ім)\b",),
        ),
        "dnipropetrovsk_oblast_verkhnodniprovsk": LocalityPreset(
            id="dnipropetrovsk_oblast_verkhnodniprovsk",
            patterns=(r"\bверхньодніпровськ(а|у|ом|і)?\b",),
        ),
        "dnipropetrovsk_oblast_vilnohirsk": LocalityPreset(
            id="dnipropetrovsk_oblast_vilnohirsk",
            patterns=(r"\bвільногірськ(а|у|ом|і)?\b",),
        ),
        "dnipropetrovsk_oblast_yurivka": LocalityPreset(
            id="dnipropetrovsk_oblast_yurivka",
            patterns=(r"\bюр['’ʼ]їв(ка|ки|ці|ку|кою)\b",),
        ),
        "dnipropetrovsk_oblast_zelenodolsk": LocalityPreset(
            id="dnipropetrovsk_oblast_zelenodolsk",
            patterns=(r"\bзеленодольськ(а|у|ом|і)?\b",),
        ),
        "dnipropetrovsk_oblast_zhovti_vody": LocalityPreset(
            id="dnipropetrovsk_oblast_zhovti_vody",
            patterns=(r"\bжовт(і|их|им|ими)\s+вод(и|ам|ами|ах)?\b",),
        ),
    },
)
