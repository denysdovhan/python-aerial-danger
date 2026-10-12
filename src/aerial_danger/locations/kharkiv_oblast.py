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
        "kharkiv_oblast_andriivka": LocalityPreset(
            id="kharkiv_oblast_andriivka",
            patterns=(r"\bандріїв(ка|ки|ці|ку|кою)\b",),
        ),
        "kharkiv_oblast_balakliia": LocalityPreset(
            id="kharkiv_oblast_balakliia", patterns=(r"\bбалаклі(я|ї|ю|єю)\b",)
        ),
        "kharkiv_oblast_barvinkove": LocalityPreset(
            id="kharkiv_oblast_barvinkove", patterns=(r"\bбарвінкове\b",)
        ),
        "kharkiv_oblast_berestyn": LocalityPreset(
            id="kharkiv_oblast_berestyn", patterns=(r"\bберестин(а|у|ом|і)?\b",)
        ),
        "kharkiv_oblast_bezliudivka": LocalityPreset(
            id="kharkiv_oblast_bezliudivka",
            patterns=(r"\bбезлюдів(ка|ки|ці|ку|кою)\b",),
        ),
        "kharkiv_oblast_blyzniuky": LocalityPreset(
            id="kharkiv_oblast_blyzniuky",
            patterns=(r"\bблизнюк(и|ів|ам|ами|ах)\b",),
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
        "kharkiv_oblast_donets": LocalityPreset(
            id="kharkiv_oblast_donets",
            patterns=(r"\bдон(ець|ця|цю|цем|ці)\b",),
        ),
        "kharkiv_oblast_huty": LocalityPreset(
            id="kharkiv_oblast_huty",
            patterns=(r"\bгут(и|ам|ами|ах)?\b",),
        ),
        "kharkiv_oblast_izium": LocalityPreset(
            id="kharkiv_oblast_izium", patterns=(r"\bізюм(а|у|ом|і)?\b",)
        ),
        "kharkiv_oblast_kehychivka": LocalityPreset(
            id="kharkiv_oblast_kehychivka",
            patterns=(r"\bкегичів(ка|ки|ці|ку|кою)\b",),
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
        "kharkiv_oblast_koviahy": LocalityPreset(
            id="kharkiv_oblast_koviahy",
            patterns=(r"\bков['’ʼ]я(ги|г|гам|гами|гах)\b",),
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
        "kharkiv_oblast_mala_danylivka": LocalityPreset(
            id="kharkiv_oblast_mala_danylivka",
            patterns=(r"\bмал(а|ої|ій|у|ою)\s+данилів(ка|ки|ці|ку|кою)\b",),
        ),
        "kharkiv_oblast_merefa": LocalityPreset(
            id="kharkiv_oblast_merefa",
            patterns=(r"\bмереф(а|и|і|у|ою)\b",),
        ),
        "kharkiv_oblast_nova_vodolaha": LocalityPreset(
            id="kharkiv_oblast_nova_vodolaha",
            patterns=(r"\bнов(а|ої|ій|у|ою)\s+водола(га|ги|зі|гу|гою)\b",),
        ),
        "kharkiv_oblast_pechenihy": LocalityPreset(
            id="kharkiv_oblast_pechenihy",
            patterns=(r"\bпеченіг(и|ів|ам|ами|ах)\b",),
        ),
        "kharkiv_oblast_peresichne": LocalityPreset(
            id="kharkiv_oblast_peresichne",
            patterns=(r"\bпересічн(е|ого|ому|им|ім)\b",),
        ),
        "kharkiv_oblast_piatykhatky": LocalityPreset(
            id="kharkiv_oblast_piatykhatky",
            patterns=(r"\bп['’ʼ]?ятихатк(и|ах|ам|ами)\b",),
        ),
        "kharkiv_oblast_pisochyn": LocalityPreset(
            id="kharkiv_oblast_pisochyn",
            patterns=(r"\bпісочин(а|у|ом|і)?\b",),
        ),
        "kharkiv_oblast_prolisne": LocalityPreset(
            id="kharkiv_oblast_prolisne",
            patterns=(r"\bпролісн(е|ого|ому|им|ім)\b",),
        ),
        "kharkiv_oblast_prykolotne": LocalityPreset(
            id="kharkiv_oblast_prykolotne",
            patterns=(r"\bприколотн(е|ого|ому|им|ім)\b",),
        ),
        "kharkiv_oblast_rohan": LocalityPreset(
            id="kharkiv_oblast_rohan",
            patterns=(r"\bроган(ь|і|ню)\b",),
        ),
        "kharkiv_oblast_sakhnovshchyna": LocalityPreset(
            id="kharkiv_oblast_sakhnovshchyna",
            patterns=(r"\bсахновщин(а|и|і|у|ою)\b",),
        ),
        "kharkiv_oblast_saltivka": LocalityPreset(
            id="kharkiv_oblast_saltivka",
            patterns=(r"\bсалтівк(а|и|і|у|ою|о)\b",),
        ),
        "kharkiv_oblast_savyntsi": LocalityPreset(
            id="kharkiv_oblast_savyntsi",
            patterns=(r"\bсавин(ці|ців|цям|цями|цях)\b",),
        ),
        "kharkiv_oblast_sharivka": LocalityPreset(
            id="kharkiv_oblast_sharivka",
            patterns=(r"\bшарів(ка|ки|ці|ку|кою)\b",),
        ),
        "kharkiv_oblast_shevchenkove": LocalityPreset(
            id="kharkiv_oblast_shevchenkove", patterns=(r"\bшевченкове\b",)
        ),
        "kharkiv_oblast_slatyne": LocalityPreset(
            id="kharkiv_oblast_slatyne", patterns=(r"\bслатин(е|ого|ому|им|ім)\b",)
        ),
        "kharkiv_oblast_slobozhanske": LocalityPreset(
            id="kharkiv_oblast_slobozhanske",
            patterns=(r"\bслобожанськ(е|ого|ому|им|ім)\b",),
        ),
        "kharkiv_oblast_staryi_merchyk": LocalityPreset(
            id="kharkiv_oblast_staryi_merchyk",
            patterns=(r"\bстар(ий|ого|ому|им|ім)\s+мерчик(а|у|ом|і)?\b",),
        ),
        "kharkiv_oblast_staryy_saltiv": LocalityPreset(
            id="kharkiv_oblast_staryy_saltiv",
            patterns=(r"\bстар(ий|ого|ому|им|ім) салт(ів|ова|ову|овом|ові)\b",),
        ),
        "kharkiv_oblast_valky": LocalityPreset(
            id="kharkiv_oblast_valky", patterns=(r"\bвалк(и|ів|ам|ами|ах)\b",)
        ),
        "kharkiv_oblast_vasyshcheve": LocalityPreset(
            id="kharkiv_oblast_vasyshcheve",
            patterns=(r"\bвасищев(е|ого|ому|им|ім)\b",),
        ),
        "kharkiv_oblast_velykyi_burluk": LocalityPreset(
            id="kharkiv_oblast_velykyi_burluk",
            patterns=(r"\bвелик(ий|ого|ому|им|ім)\s+бурлук(а|у|ом|і)?\b",),
        ),
        "kharkiv_oblast_vilshany": LocalityPreset(
            id="kharkiv_oblast_vilshany",
            patterns=(r"\bвільшан(и|ам|ами|ах)?\b",),
        ),
        "kharkiv_oblast_vysokyi": LocalityPreset(
            id="kharkiv_oblast_vysokyi",
            patterns=(r"\bвисок(ий|ого|ому|им|ім)\b(?=\s*([.!?,/—–-]|$))",),
        ),
        "kharkiv_oblast_zlatopil": LocalityPreset(
            id="kharkiv_oblast_zlatopil", patterns=(r"\bзлатопіль\b",)
        ),
        "kharkiv_oblast_zmiiv": LocalityPreset(
            id="kharkiv_oblast_zmiiv",
            patterns=(r"\bзмі(їв|єва|єву|євом|єві)\b",),
        ),
        "kharkiv_oblast_zolochiv": LocalityPreset(
            id="kharkiv_oblast_zolochiv",
            patterns=(r"\bзолоч(ів|ова|ову|овом|ові)\b",),
        ),
    },
)
