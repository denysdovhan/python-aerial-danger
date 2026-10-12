"""Location presets for zhytomyr oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

ZHYTOMYR_OBLAST_REGION: Final = RegionPreset(
    id="zhytomyr_oblast",
    patterns=(
        r"\bжитомирщин(а|и|і|у|ою)\b",
        r"\bжитомирськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
    ),
    localities={
        "zhytomyr_oblast_andrushivka": LocalityPreset(
            id="zhytomyr_oblast_andrushivka",
            patterns=(r"\bандрушів(ка|ки|ці|ку|кою)\b",),
        ),
        "zhytomyr_oblast_berdychiv": LocalityPreset(
            id="zhytomyr_oblast_berdychiv",
            patterns=(r"\bбердич(ів|ева|еву|евом|еві)\b",),
        ),
        "zhytomyr_oblast_brusyliv": LocalityPreset(
            id="zhytomyr_oblast_brusyliv",
            patterns=(r"\bбрусил(ів|ова|ову|овом|ові)\b",),
        ),
        "zhytomyr_oblast_cherniakhiv": LocalityPreset(
            id="zhytomyr_oblast_cherniakhiv",
            patterns=(r"\bчернях(ів|ова|ову|овом|ові)\b",),
        ),
        "zhytomyr_oblast_chopovychi": LocalityPreset(
            id="zhytomyr_oblast_chopovychi",
            patterns=(r"\bчопович(і|ів|ам|ами|ах)\b",),
        ),
        "zhytomyr_oblast_chudniv": LocalityPreset(
            id="zhytomyr_oblast_chudniv",
            patterns=(r"\bчудн(ів|ова|ову|овом|ові)\b",),
        ),
        "zhytomyr_oblast_dovbysh": LocalityPreset(
            id="zhytomyr_oblast_dovbysh",
            patterns=(r"\bдовбиш(а|у|ем|і)?\b",),
        ),
        "zhytomyr_oblast_irshansk": LocalityPreset(
            id="zhytomyr_oblast_irshansk",
            patterns=(r"\bіршанськ(а|у|ом|і)?\b",),
        ),
        "zhytomyr_oblast_khoroshiv": LocalityPreset(
            id="zhytomyr_oblast_khoroshiv",
            patterns=(r"\bхорош(ів|ова|ову|овом|ові)\b",),
        ),
        "zhytomyr_oblast_kornyn": LocalityPreset(
            id="zhytomyr_oblast_kornyn",
            patterns=(r"\bкорнин(а|у|ом|і)?\b",),
        ),
        "zhytomyr_oblast_korosten": LocalityPreset(
            id="zhytomyr_oblast_korosten",
            patterns=(r"\bкоростен(ь|я|ем|і)\b",),
        ),
        "zhytomyr_oblast_korostyshiv": LocalityPreset(
            id="zhytomyr_oblast_korostyshiv",
            patterns=(r"\bкоростиш(ів|ова|ову|овом|ові)\b",),
        ),
        "zhytomyr_oblast_liubar": LocalityPreset(
            id="zhytomyr_oblast_liubar",
            patterns=(r"\bлюбар(а|у|ом|і)?\b",),
        ),
        "zhytomyr_oblast_luhyny": LocalityPreset(
            id="zhytomyr_oblast_luhyny",
            patterns=(r"\bлугин(и|ів|ам|ами|ах)\b",),
        ),
        "zhytomyr_oblast_malyn": LocalityPreset(
            id="zhytomyr_oblast_malyn",
            patterns=(r"\bмалин(а|у|ом|і)?\b",),
        ),
        "zhytomyr_oblast_narodychi": LocalityPreset(
            id="zhytomyr_oblast_narodychi",
            patterns=(r"\bнародич(і|ів|ам|ами|ах)\b",),
        ),
        "zhytomyr_oblast_nova_borova": LocalityPreset(
            id="zhytomyr_oblast_nova_borova",
            patterns=(r"\bнов(а|ої|ій|у|ою)\s+боров(а|ої|ій|у|ою)\b",),
        ),
        "zhytomyr_oblast_novohuivynske": LocalityPreset(
            id="zhytomyr_oblast_novohuivynske",
            patterns=(r"\bновогуйвинськ(е|ого|ому|им|ім)\b",),
        ),
        "zhytomyr_oblast_olevsk": LocalityPreset(
            id="zhytomyr_oblast_olevsk",
            patterns=(r"\bолевськ(а|у|ом|і)?\b",),
        ),
        "zhytomyr_oblast_ovruch": LocalityPreset(
            id="zhytomyr_oblast_ovruch", patterns=(r"\bовруч(а|у|ем|і)?\b",)
        ),
        "zhytomyr_oblast_ozerne": LocalityPreset(
            id="zhytomyr_oblast_ozerne",
            patterns=(r"\bозерн(е|ого|ому|им|ім)\b",),
        ),
        "zhytomyr_oblast_pulyny": LocalityPreset(
            id="zhytomyr_oblast_pulyny",
            patterns=(r"\bпулин(и|ів|ам|ами|ах)\b",),
        ),
        "zhytomyr_oblast_radomyshl": LocalityPreset(
            id="zhytomyr_oblast_radomyshl",
            patterns=(r"\bрадомишл(ь|я|ю|ем|і)\b",),
        ),
        "zhytomyr_oblast_ruzhyn": LocalityPreset(
            id="zhytomyr_oblast_ruzhyn",
            patterns=(r"\bружин(а|у|ом|і)?\b",),
        ),
        "zhytomyr_oblast_zarichany": LocalityPreset(
            id="zhytomyr_oblast_zarichany",
            patterns=(r"\bзарічан(и|ам|ами|ах)?\b",),
        ),
        "zhytomyr_oblast_zhytomyr": LocalityPreset(
            id="zhytomyr_oblast_zhytomyr", patterns=(r"\bжитомир(а|у|ом|і)?\b",)
        ),
        "zhytomyr_oblast_zviahel": LocalityPreset(
            id="zhytomyr_oblast_zviahel",
            patterns=(r"\bзвягел(ь|я|ю|ем|і)\b",),
        ),
    },
)
