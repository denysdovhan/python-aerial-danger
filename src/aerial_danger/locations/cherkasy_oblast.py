"""Location presets for cherkasy oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

CHERKASY_OBLAST_REGION: Final = RegionPreset(
    id="cherkasy_oblast",
    patterns=(
        r"\bчеркащин(а|и|і|у|ою)\b",
        r"\bчеркаськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
    ),
    localities={
        "cherkasy_oblast_buky": LocalityPreset(
            id="cherkasy_oblast_buky",
            patterns=(r"\bбук(и|ів|ам|ами|ах)\b",),
        ),
        "cherkasy_oblast_cherkasy": LocalityPreset(
            id="cherkasy_oblast_cherkasy", patterns=(r"\bчеркас(и|ам|ами|ах)?\b",)
        ),
        "cherkasy_oblast_chornobai": LocalityPreset(
            id="cherkasy_oblast_chornobai", patterns=(r"\bчорноба(й|я|ю|єм|ї)\b",)
        ),
        "cherkasy_oblast_chyhyryn": LocalityPreset(
            id="cherkasy_oblast_chyhyryn",
            patterns=(r"\bчигирин(а|у|ом|і)?\b",),
        ),
        "cherkasy_oblast_drabiv": LocalityPreset(
            id="cherkasy_oblast_drabiv",
            patterns=(r"\bдраб(ів|ова|ову|овом|ові)\b",),
        ),
        "cherkasy_oblast_helmiaziv": LocalityPreset(
            id="cherkasy_oblast_helmiaziv",
            patterns=(r"\bгельмяз(ів|ова|ову|овом|ові)\b",),
        ),
        "cherkasy_oblast_horodyshche": LocalityPreset(
            id="cherkasy_oblast_horodyshche",
            patterns=(r"\bгородищ(е|а|у|ем|і)\b",),
        ),
        "cherkasy_oblast_irdyn": LocalityPreset(
            id="cherkasy_oblast_irdyn",
            patterns=(r"\bірдин(ь|я|ю|ем|і)\b",),
        ),
        "cherkasy_oblast_irkliiv": LocalityPreset(
            id="cherkasy_oblast_irkliiv",
            patterns=(r"\bіркл(іїв|ієва|ієву|ієвом|ієві)\b",),
        ),
        "cherkasy_oblast_kalynopil": LocalityPreset(
            id="cherkasy_oblast_kalynopil",
            patterns=(r"\bкалиноп(іль|оля|олю|олем|олі)\b",),
        ),
        "cherkasy_oblast_kamianka": LocalityPreset(
            id="cherkasy_oblast_kamianka",
            patterns=(r"\bкам['’ʼ]ян(ка|ки|ці|ку|кою)\b",),
        ),
        "cherkasy_oblast_kaniv": LocalityPreset(
            id="cherkasy_oblast_kaniv", patterns=(r"\bкан(ів|ева|еву|евом|еві)\b",)
        ),
        "cherkasy_oblast_korsun_shevchenkivskyi": LocalityPreset(
            id="cherkasy_oblast_korsun_shevchenkivskyi",
            patterns=(r"\bкорсун(ь|я|ю|ем|і)[ -]шевченківськ(ий|ого|ому|им|ім)\b",),
        ),
        "cherkasy_oblast_lysianka": LocalityPreset(
            id="cherkasy_oblast_lysianka",
            patterns=(r"\bлисян(ка|ки|ці|ку|кою)\b",),
        ),
        "cherkasy_oblast_monastyryshche": LocalityPreset(
            id="cherkasy_oblast_monastyryshche",
            patterns=(r"\bмонастирищ(е|а|у|ем|і)\b",),
        ),
        "cherkasy_oblast_moshny": LocalityPreset(
            id="cherkasy_oblast_moshny",
            patterns=(r"\bмош(ни|ен|нам|нами|нах)\b",),
        ),
        "cherkasy_oblast_shpola": LocalityPreset(
            id="cherkasy_oblast_shpola", patterns=(r"\bшпол(а|и|і|у|ою)\b",)
        ),
        "cherkasy_oblast_smila": LocalityPreset(
            id="cherkasy_oblast_smila", patterns=(r"\bсміл(а|и|у|ою)\b",)
        ),
        "cherkasy_oblast_talne": LocalityPreset(
            id="cherkasy_oblast_talne", patterns=(r"\bтальн(е|ого|ому|им|ім)\b",)
        ),
        "cherkasy_oblast_trakhtemyriv": LocalityPreset(
            id="cherkasy_oblast_trakhtemyriv",
            patterns=(r"\bтрахтемир(ів|ова|ову|овом|ові)\b",),
        ),
        "cherkasy_oblast_tsvitkove": LocalityPreset(
            id="cherkasy_oblast_tsvitkove",
            patterns=(r"\bцвітков(е|ого|ому|им|ім)\b",),
        ),
        "cherkasy_oblast_tsybuliv": LocalityPreset(
            id="cherkasy_oblast_tsybuliv",
            patterns=(r"\bцибул(ів|ова|ову|овом|ові)\b",),
        ),
        "cherkasy_oblast_uman": LocalityPreset(
            id="cherkasy_oblast_uman", patterns=(r"\bуман(ь|і|ню|нею)\b",)
        ),
        "cherkasy_oblast_vilshana": LocalityPreset(
            id="cherkasy_oblast_vilshana",
            patterns=(r"\bвільшан(а|и|і|у|ою)\b",),
        ),
        "cherkasy_oblast_zhashkiv": LocalityPreset(
            id="cherkasy_oblast_zhashkiv",
            patterns=(r"\bжашк(ів|ова|ову|овом|ові)\b",),
        ),
        "cherkasy_oblast_zolotonosha": LocalityPreset(
            id="cherkasy_oblast_zolotonosha", patterns=(r"\bзолотонош(а|і|у|ею)\b",)
        ),
        "cherkasy_oblast_zvenyhorodka": LocalityPreset(
            id="cherkasy_oblast_zvenyhorodka",
            patterns=(r"\bзвенигород(ка|ки|ці|ку|кою)\b",),
        ),
    },
)
