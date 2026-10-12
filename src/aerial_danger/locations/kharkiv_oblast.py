"""Location presets for kharkiv oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

KHARKIV_OBLAST_REGION: Final = RegionPreset(
    id="kharkiv_oblast",
    patterns=(
        r"\bхарківщин(а|и|і|у|ою)\b",
        r"\bхарківськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
    ),
    localities={
        "kharkiv_oblast_balakliia": LocalityPreset(
            id="kharkiv_oblast_balakliia", patterns=(r"\bбалаклі(я|ї|ю|єю)\b",)
        ),
        "kharkiv_oblast_barvinkove": LocalityPreset(
            id="kharkiv_oblast_barvinkove", patterns=(r"\bбарвінкове\b",)
        ),
        "kharkiv_oblast_berestyn": LocalityPreset(
            id="kharkiv_oblast_berestyn", patterns=(r"\bберестин(а|у|ом|і)?\b",)
        ),
        "kharkiv_oblast_bohodukhiv": LocalityPreset(
            id="kharkiv_oblast_bohodukhiv",
            patterns=(r"\bбогодух(ів|ова|ову|овом|ові)\b",),
        ),
        "kharkiv_oblast_chuhuiv": LocalityPreset(
            id="kharkiv_oblast_chuhuiv",
            patterns=(r"\bчуг(уїв|уєва|уєву|уєвом|уєві)\b",),
        ),
        "kharkiv_oblast_derhachi": LocalityPreset(
            id="kharkiv_oblast_derhachi", patterns=(r"\bдергач(і|ів|ам|ами|ах)\b",)
        ),
        "kharkiv_oblast_derzhprom": LocalityPreset(
            id="kharkiv_oblast_derzhprom", patterns=(r"\bдержпром(у|і|ом|а)?\b",)
        ),
        "kharkiv_oblast_izium": LocalityPreset(
            id="kharkiv_oblast_izium", patterns=(r"\bізюм(а|у|ом|і)?\b",)
        ),
        "kharkiv_oblast_kharkiv": LocalityPreset(
            id="kharkiv_oblast_kharkiv",
            patterns=(r"\bхарк(ів|ова|ову|овом|ові)\b",),
        ),
        "kharkiv_oblast_khtz": LocalityPreset(
            id="kharkiv_oblast_khtz", patterns=(r"\bхтз\b",)
        ),
        "kharkiv_oblast_kolomak": LocalityPreset(
            id="kharkiv_oblast_kolomak", patterns=(r"\bколомак(а|у|ом|і)?\b",)
        ),
        "kharkiv_oblast_kozacha_lopan": LocalityPreset(
            id="kharkiv_oblast_kozacha_lopan",
            patterns=(r"\bкозач(а|у|ою) лопан(ь|і|ню|ью)\b",),
        ),
        "kharkiv_oblast_krasnokutsk": LocalityPreset(
            id="kharkiv_oblast_krasnokutsk",
            patterns=(r"\bкраснокутськ(а|у|ом|і)?\b",),
        ),
        "kharkiv_oblast_krasnopavlivka": LocalityPreset(
            id="kharkiv_oblast_krasnopavlivka",
            patterns=(r"\bкраснопавлівк(а|и|у|ою|і)\b",),
        ),
        "kharkiv_oblast_kulynychi": LocalityPreset(
            id="kharkiv_oblast_kulynychi",
            patterns=(r"\bкулинич(і|ів|ам|ами|ах)\b",),
        ),
        "kharkiv_oblast_kupiansk": LocalityPreset(
            id="kharkiv_oblast_kupiansk",
            patterns=(r"\bкуп['’ʼ]?янськ(а|у|ом|і)?\b",),
        ),
        "kharkiv_oblast_liubotyn": LocalityPreset(
            id="kharkiv_oblast_liubotyn", patterns=(r"\bлюботин(а|у|ом|і)?\b",)
        ),
        "kharkiv_oblast_lozova": LocalityPreset(
            id="kharkiv_oblast_lozova",
            patterns=(r"\bлозов(у|ої|а|ою)\b",),
        ),
        "kharkiv_oblast_pechenihy": LocalityPreset(
            id="kharkiv_oblast_pechenihy",
            patterns=(r"\bпеченіг(и|ів|ам|ами|ах)\b",),
        ),
        "kharkiv_oblast_piatykhatky": LocalityPreset(
            id="kharkiv_oblast_piatykhatky",
            patterns=(r"\bп['’ʼ]?ятихатк(и|ах|ам|ами)\b",),
        ),
        "kharkiv_oblast_saltivka": LocalityPreset(
            id="kharkiv_oblast_saltivka",
            patterns=(r"\bсалтівк(а|и|і|у|ою|о)\b",),
        ),
        "kharkiv_oblast_shevchenkove": LocalityPreset(
            id="kharkiv_oblast_shevchenkove", patterns=(r"\bшевченкове\b",)
        ),
        "kharkiv_oblast_slatyne": LocalityPreset(
            id="kharkiv_oblast_slatyne", patterns=(r"\bслатин(е|ого|ому|им|ім)\b",)
        ),
        "kharkiv_oblast_staryy_saltiv": LocalityPreset(
            id="kharkiv_oblast_staryy_saltiv",
            patterns=(r"\bстар(ий|ого|ому|им|ім) салт(ів|ова|ову|овом|ові)\b",),
        ),
        "kharkiv_oblast_valky": LocalityPreset(
            id="kharkiv_oblast_valky", patterns=(r"\bвалк(и|ів|ам|ами|ах)\b",)
        ),
        "kharkiv_oblast_zlatopil": LocalityPreset(
            id="kharkiv_oblast_zlatopil", patterns=(r"\bзлатопіль\b",)
        ),
    },
)
