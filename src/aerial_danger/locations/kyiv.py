"""Location presets for kyiv."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

KYIV_REGION: Final = RegionPreset(
    id="kyiv",
    patterns=(
        r"\bки(їв|єва|єві|єву|євом)\b",
        r"\bстолиц(я|і|ю|ею)\b",
    ),
    localities={
        "kyiv_akademmistechko": LocalityPreset(
            id="kyiv_akademmistechko",
            patterns=(r"\bакадем\b", r"\bакадеммістечк(о|а|у|ом)\b"),
        ),
        "kyiv_antonov": LocalityPreset(
            id="kyiv_antonov", patterns=(r"\bантонов(а)?\b",)
        ),
        "kyiv_berezniaky": LocalityPreset(
            id="kyiv_berezniaky", patterns=(r"\bберезняк(и|ів|ах|ами)\b",)
        ),
        "kyiv_berkovets": LocalityPreset(
            id="kyiv_berkovets", patterns=(r"\bберков(ець|ця|ці|цем)\b",)
        ),
        "kyiv_bilychi": LocalityPreset(
            id="kyiv_bilychi", patterns=(r"\bбілич(і|ів|ах|ами)\b",)
        ),
        "kyiv_borshchahivka": LocalityPreset(
            id="kyiv_borshchahivka",
            patterns=(r"\bборщаг(а|и|у|ою|івк(а|и|у|ою|ці)|івок)\b",),
        ),
        "kyiv_bortnychi": LocalityPreset(
            id="kyiv_bortnychi", patterns=(r"\bбортнич(і|ів|ах|ами)\b",)
        ),
        "kyiv_bykivnia": LocalityPreset(
            id="kyiv_bykivnia", patterns=(r"\bбиківн(я|і|ю|ею)\b",)
        ),
        "kyiv_center": LocalityPreset(
            id="kyiv_center", patterns=(r"\bцентр(у|і|ом|а)?\b",)
        ),
        "kyiv_chokolivka": LocalityPreset(
            id="kyiv_chokolivka", patterns=(r"\bчоколівк(а|и|у|ою|ці)\b",)
        ),
        "kyiv_comfort_town": LocalityPreset(
            id="kyiv_comfort_town", patterns=(r"\bкомфорт[\s-]?таун(а|у|ом|і)?\b",)
        ),
        "kyiv_darnytsia": LocalityPreset(
            id="kyiv_darnytsia",
            patterns=(
                r"\bдарниц(я|і|ю|ею)\b",
                r"\bдарницьк(ий|ого|ому|им)(?: масив(у|і|ом|а)?)?\b",
            ),
        ),
        "kyiv_demiivka": LocalityPreset(
            id="kyiv_demiivka", patterns=(r"\bдеміївк(а|и|у|ою|ці)\b",)
        ),
        "kyiv_desnianskyi_district": LocalityPreset(
            id="kyiv_desnianskyi_district",
            patterns=(r"\bдеснянськ(ий|ого|ому|им|ім) район(у|і|ом|а)?\b",),
        ),
        "kyiv_dniprovskyi_district": LocalityPreset(
            id="kyiv_dniprovskyi_district",
            patterns=(r"\bдніпровськ(ий|ого|ому|им|ім) район(у|і|ом|а)?\b",),
        ),
        "kyiv_dorohzhychi": LocalityPreset(
            id="kyiv_dorohzhychi", patterns=(r"\bдорогожич(і|ів|ам|ами|ах)\b",)
        ),
        "kyiv_dvrz": LocalityPreset(id="kyiv_dvrz", patterns=(r"\bдврз\b",)),
        "kyiv_faina_town": LocalityPreset(
            id="kyiv_faina_town",
            patterns=(
                r"\bфайна[\s-]?таун(а|у|ом|і)?\b",
                r"\bfa(i|y)na[\s-]?town\b",
            ),
        ),
        "kyiv_feofaniia": LocalityPreset(
            id="kyiv_feofaniia", patterns=(r"\bфеофан(ія|ії|ію|ією)\b",)
        ),
        "kyiv_halahany": LocalityPreset(
            id="kyiv_halahany", patterns=(r"\bгалаган(и|ів|ам|ами|ах)?\b",)
        ),
        "kyiv_hidropark": LocalityPreset(
            id="kyiv_hidropark", patterns=(r"\bгідропарк(у|і|ом|а)?\b",)
        ),
        "kyiv_holosiiv": LocalityPreset(
            id="kyiv_holosiiv",
            patterns=(
                r"\bголосі(їв|єва|єві|єву|євом)\b",
                r"\bголосіївськ(ий|ого|ому|им)\b",
                r"\bголос\b",
            ),
        ),
        "kyiv_ipodrom": LocalityPreset(
            id="kyiv_ipodrom", patterns=(r"\bіподром(у|і|ом|а)?\b",)
        ),
        "kyiv_karavaievi_dachi": LocalityPreset(
            id="kyiv_karavaievi_dachi",
            patterns=(
                r"\bкараваєв(і дачі|их дач|им дачам|ими дачами|их дачах)\b",
                r"\bкардач(і|ів|ам|ами|ах)\b",
            ),
        ),
        "kyiv_kharkivskyi_masyv": LocalityPreset(
            id="kyiv_kharkivskyi_masyv",
            patterns=(r"\bхарківськ(ий|ого|ому|им)(?: масив(у|і|ом|а)?)?\b",),
        ),
        "kyiv_khutir": LocalityPreset(
            id="kyiv_khutir",
            patterns=(
                r"\bчервон(ий|ого|ому|им) хут(ір|ор(а|у|і|ом|е))\b",
                r"\bхутір\b",
            ),
        ),
        "kyiv_klov": LocalityPreset(
            id="kyiv_klov",
            patterns=(r"\bклов(у|і|ом|а)?\b", r"\bкловськ(а|ої|ій|у|ою)\b"),
        ),
        "kyiv_koncha_zaspa": LocalityPreset(
            id="kyiv_koncha_zaspa",
            patterns=(
                r"\bконч(а|і)[ -]засп(а|и|і|у|ою)\b",
                r"\bзасп(а|и|і|у|ою)\b",
            ),
        ),
        "kyiv_korchuvate": LocalityPreset(
            id="kyiv_korchuvate", patterns=(r"\bкорчуват(е|ого|ому|им|ім)\b",)
        ),
        "kyiv_kpi": LocalityPreset(id="kyiv_kpi", patterns=(r"\bкпі\b",)),
        "kyiv_kurenivka": LocalityPreset(
            id="kyiv_kurenivka", patterns=(r"\bкуренівк(а|и|у|ою|ці)\b",)
        ),
        "kyiv_left_bank": LocalityPreset(
            id="kyiv_left_bank",
            patterns=(
                r"\bлів(ий|ого|ому|им) берег(а|у|ом|і)?\b",
                r"\bлівобережж(я|і|ю|ям)\b",
            ),
        ),
        "kyiv_lisovyi_masyv": LocalityPreset(
            id="kyiv_lisovyi_masyv",
            patterns=(r"\bлісов(ий|ого|ому|им)(?: масив(у|і|ом|а)?)?\b",),
        ),
        "kyiv_livoberezhnyi_masyv": LocalityPreset(
            id="kyiv_livoberezhnyi_masyv",
            patterns=(r"\bлівобережн(ий|ого|ому|им)(?: масив(у|і|ом|а)?)?\b",),
        ),
        "kyiv_lukianivka": LocalityPreset(
            id="kyiv_lukianivka",
            patterns=(r"\bлук['’ʼ]?янів(ка|ки|ці|ку|кою)\b",),
        ),
        "kyiv_lypky": LocalityPreset(
            id="kyiv_lypky", patterns=(r"\bлип(ки|ок|ках|ками)\b",)
        ),
        "kyiv_minskyi_masyv": LocalityPreset(
            id="kyiv_minskyi_masyv",
            patterns=(r"\bмінськ(ий|ого|ому|им)(?: масив(у|і|ом|а)?)?\b",),
        ),
        "kyiv_muromets": LocalityPreset(
            id="kyiv_muromets",
            patterns=(r"\b(острів )?муром(ець|ця|ці|цем)\b",),
        ),
        "kyiv_mysholovka": LocalityPreset(
            id="kyiv_mysholovka", patterns=(r"\bмишоловк(а|и|у|ою|ці)\b",)
        ),
        "kyiv_nova_zabudova": LocalityPreset(
            id="kyiv_nova_zabudova",
            patterns=(r"\bнов(а|ої|ій|у|ою) забудов(а|и|і|у|ою)\b",),
        ),
        "kyiv_nyvky": LocalityPreset(
            id="kyiv_nyvky", patterns=(r"\bнив(ки|ках|ками|ок)\b",)
        ),
        "kyiv_nyzhni_sady": LocalityPreset(
            id="kyiv_nyzhni_sady",
            patterns=(r"\bнижн(і|іх|ім|ими) сад(и|ів|ах|ами)\b",),
        ),
        "kyiv_obolon": LocalityPreset(
            id="kyiv_obolon",
            patterns=(
                r"\bоболон(ь|і|ню)\b",
                r"\bоболонськ(ий|ого|ому|им)\b",
            ),
        ),
        "kyiv_osokorky": LocalityPreset(
            id="kyiv_osokorky", patterns=(r"\bосокорк(и|ів|ах|ами)\b",)
        ),
        "kyiv_pechersk": LocalityPreset(
            id="kyiv_pechersk", patterns=(r"\bпечерськ(ий|ого|ому|им)?\b",)
        ),
        "kyiv_pochaiana": LocalityPreset(
            id="kyiv_pochaiana", patterns=(r"\bпочайн(а|и|і|у|ою|ої)\b",)
        ),
        "kyiv_podil": LocalityPreset(
            id="kyiv_podil",
            patterns=(
                r"\bпод(іл|олу|олі|олом)\b",
                r"\bподільськ(ий|ого|ому|им)\b",
            ),
        ),
        "kyiv_pozniaky": LocalityPreset(
            id="kyiv_pozniaky",
            patterns=(r"\bпозняк(и|ів|ах|ами)\b",),
        ),
        "kyiv_priorka": LocalityPreset(
            id="kyiv_priorka", patterns=(r"\bпріорк(а|и|у|ою|ці)\b",)
        ),
        "kyiv_pushcha_vodytsia": LocalityPreset(
            id="kyiv_pushcha_vodytsia",
            # Short forms are corpus-backed Kyiv locality names.
            patterns=(
                r"\bпущ(а|і)\b",
                r"(?<=на )пущу\b",
                r"(?<=в )пущу\b",
                r"(?<=у )пущу\b",
                r"(?<=до )пущу\b",
                r"\bпущ(а|і|у|ею)[ -]водиц(я|і|ю|ею)\b",
            ),
        ),
        "kyiv_pyrohiv": LocalityPreset(
            id="kyiv_pyrohiv", patterns=(r"\bпирог(ів|ова|ову|овом|ові)\b",)
        ),
        "kyiv_rembaza": LocalityPreset(
            id="kyiv_rembaza", patterns=(r"\bрембаз(а|и|і|у|ою)\b",)
        ),
        "kyiv_respublika": LocalityPreset(
            id="kyiv_respublika",
            patterns=(r"\bреспублік(а|и|і|у|ою)\b", r"\brespublika\b"),
        ),
        "kyiv_retroville": LocalityPreset(
            id="kyiv_retroville",
            patterns=(
                r"\bретровіл(ь|я|ю|ем|і)\b",
                r"\bretroville\b",
            ),
        ),
        "kyiv_right_bank": LocalityPreset(
            id="kyiv_right_bank",
            patterns=(
                r"\bправ(ий|ого|ому|им) берег(а|у|ом|і)?\b",
                r"\bправобережж(я|і|ю|ям)\b",
            ),
        ),
        "kyiv_rusanivka": LocalityPreset(
            id="kyiv_rusanivka", patterns=(r"\bрусанів(ка|ки|ці|ку|кою)\b",)
        ),
        "kyiv_rusanivski_sady": LocalityPreset(
            id="kyiv_rusanivski_sady",
            patterns=(r"\bрусанівськ(і|их|им|ими) сад(и|ів|ах|ами)\b",),
        ),
        "kyiv_shevchenkivskyi_district": LocalityPreset(
            id="kyiv_shevchenkivskyi_district",
            patterns=(r"\bшевченківськ(ий|ого|ому|им|ім) район(у|і|ом|а)?\b",),
        ),
        "kyiv_shuliavka": LocalityPreset(
            id="kyiv_shuliavka", patterns=(r"\bшулявк(а|и|у|ою|ці)\b",)
        ),
        "kyiv_solomianka": LocalityPreset(
            id="kyiv_solomianka",
            patterns=(
                r"\bсолом(а|['’ʼ]?янк(а|и|у|ою|ці))\b",
                r"\bсолом(у|и|і|ою)\b",
                r"\bсолом['’ʼ]?янськ(ий|ого|ому|им)\b",
            ),
        ),
        "kyiv_sotsmisto": LocalityPreset(
            id="kyiv_sotsmisto", patterns=(r"\bсоцміст(о|ом|т)\b",)
        ),
        "kyiv_sovky": LocalityPreset(
            id="kyiv_sovky", patterns=(r"\bсов(ки|ок|кам|ками|ках)\b",)
        ),
        "kyiv_sviatoshyn": LocalityPreset(
            id="kyiv_sviatoshyn",
            patterns=(
                r"\bсвятошин(о|а|і)?\b",
                r"\bсвятошинськ(ий|ого|ому|им)\b",
            ),
        ),
        "kyiv_syrets": LocalityPreset(
            id="kyiv_syrets", patterns=(r"\bсир(ець|ця|ці|цем)\b",)
        ),
        "kyiv_telychka": LocalityPreset(
            id="kyiv_telychka", patterns=(r"\bтеличк(а|и|у|ою|ці)\b",)
        ),
        "kyiv_teremky": LocalityPreset(
            id="kyiv_teremky", patterns=(r"\bтеремк(и|ів|ах|ами)\b",)
        ),
        "kyiv_troieshchyna": LocalityPreset(
            id="kyiv_troieshchyna",
            patterns=(
                r"\bтроєщин(а|и|і|у|ою)\b",
                r"\bтро(я|ї|ю)\b",
            ),
        ),
        "kyiv_trukhaniv_island": LocalityPreset(
            id="kyiv_trukhaniv_island",
            patterns=(
                r"\bтрухан(ів|ова|ову|овом|ові)\b",
                r"\bтруханів\s+остр(ів|ова|ову|овом|ові)\b",
            ),
        ),
        "kyiv_varshavskyi": LocalityPreset(
            id="kyiv_varshavskyi",
            patterns=(
                r"\bваршавськ(ий|ого|ому|им|ім) масив(у|а|ом|і)?\b",
                r"\bжк\s*[«\"„“]?\s*варшавськ(ий|ого|ому|им|ім)(\s+плюс)?\b",
            ),
        ),
        "kyiv_vidradnyi": LocalityPreset(
            id="kyiv_vidradnyi", patterns=(r"\bвідра(д|нд)н(ий|ого|ому|им)\b",)
        ),
        "kyiv_vita_lytovska": LocalityPreset(
            id="kyiv_vita_lytovska",
            patterns=(r"\bвіта[ -]литовськ(а|ої|ій|у|ою)\b",),
        ),
        "kyiv_voskresenka": LocalityPreset(
            id="kyiv_voskresenka", patterns=(r"\bвос(к)?ресенк(а|и|у|ою|ці)\b",)
        ),
        "kyiv_vydubychi": LocalityPreset(
            id="kyiv_vydubychi", patterns=(r"\bвидубич(і|ів|ах|ами)\b",)
        ),
        "kyiv_vynohradar": LocalityPreset(
            id="kyiv_vynohradar", patterns=(r"\bвиноградар(а|і|ем)?\b",)
        ),
        "kyiv_zhuliany": LocalityPreset(
            id="kyiv_zhuliany", patterns=(r"\bжулян(и|ах|ами)?\b",)
        ),
        "kyiv_zvirynets": LocalityPreset(
            id="kyiv_zvirynets", patterns=(r"\bзвірин(ець|ця|ці|цем)\b",)
        ),
    },
)
