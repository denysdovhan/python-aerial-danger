"""Area pattern presets for Aerial Danger."""

from dataclasses import dataclass
from typing import Final


@dataclass(frozen=True)
class LocalityPreset:
    """Locality preset definition."""

    id: str
    patterns: tuple[str, ...]


@dataclass(frozen=True)
class RegionPreset:
    """Region preset definition and its localities."""

    id: str
    patterns: tuple[str, ...]
    localities: dict[str, LocalityPreset]


LOCATION_PRESETS: Final = {
    "cherkasy_oblast": RegionPreset(
        id="cherkasy_oblast",
        patterns=(
            r"\bчеркащин(а|и|і|у|ою)\b",
            r"\bчеркаськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
        ),
        localities={
            "cherkasy_oblast_cherkasy": LocalityPreset(
                id="cherkasy_oblast_cherkasy", patterns=(r"\bчеркас(и|ам|ами|ах)?\b",)
            ),
        },
    ),
    "chernihiv_oblast": RegionPreset(
        id="chernihiv_oblast",
        patterns=(
            r"\bчернігівщин(а|и|і|у|ою)\b",
            r"\bчернігівськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
        ),
        localities={
            "chernihiv_oblast_chernihiv": LocalityPreset(
                id="chernihiv_oblast_chernihiv",
                patterns=(r"\bчерніг(ів|ова|ову|овом|ові)\b",),
            ),
        },
    ),
    "chernivtsi_oblast": RegionPreset(
        id="chernivtsi_oblast",
        patterns=(
            r"\bбуковин(а|и|і|у|ою)\b",
            r"\bчернівеччин(а|и|і|у|ою)\b",
            r"\bчернівецьк(а|ої|ій|у|ою) област(ь|і|ю)\b",
        ),
        localities={
            "chernivtsi_oblast_chernivtsi": LocalityPreset(
                id="chernivtsi_oblast_chernivtsi",
                patterns=(r"\bчернівц(і|ів|ям|ями|ях)\b",),
            ),
        },
    ),
    "dnipropetrovsk_oblast": RegionPreset(
        id="dnipropetrovsk_oblast",
        patterns=(
            r"\bдніпропетровщин(а|и|і|у|ою)\b",
            r"\bдніпропетровськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
        ),
        localities={
            "dnipropetrovsk_oblast_dnipro": LocalityPreset(
                id="dnipropetrovsk_oblast_dnipro", patterns=(r"\bдніпр(о|а|у|і|ом)\b",)
            ),
            "dnipropetrovsk_oblast_kamianske": LocalityPreset(
                id="dnipropetrovsk_oblast_kamianske",
                patterns=(r"\bкам['’ʼ]?янськ(е|ого|ому|им|ім)\b",),
            ),
            "dnipropetrovsk_oblast_kryvyi_rih": LocalityPreset(
                id="dnipropetrovsk_oblast_kryvyi_rih",
                patterns=(r"\bкрив(ий|ого|ому|им) р(іг|огу|озі|огом)\b",),
            ),
            "dnipropetrovsk_oblast_pavlohrad": LocalityPreset(
                id="dnipropetrovsk_oblast_pavlohrad",
                patterns=(r"\bпавлоград(а|у|і|ом)?\b",),
            ),
        },
    ),
    "donetsk_oblast": RegionPreset(
        id="donetsk_oblast",
        patterns=(
            r"\bдонеччин(а|и|і|у|ою)\b",
            r"\bдонецьк(а|ої|ій|у|ою) област(ь|і|ю)\b",
        ),
        localities={
            "donetsk_oblast_donetsk": LocalityPreset(
                id="donetsk_oblast_donetsk",
                patterns=(r"\bдонецьк(у|ом|і)?\b",),
            ),
        },
    ),
    "ivano_frankivsk_oblast": RegionPreset(
        id="ivano_frankivsk_oblast",
        patterns=(
            r"\bфранківщин(а|и|і|у|ою)\b",
            r"\bівано-франківщин(а|и|і|у|ою)\b",
            r"\bівано-франківськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
        ),
        localities={
            "ivano_frankivsk_oblast_ivano_frankivsk": LocalityPreset(
                id="ivano_frankivsk_oblast_ivano_frankivsk",
                patterns=(r"\bівано-франківськ(у|ом|і)?\b",),
            ),
        },
    ),
    "kharkiv_oblast": RegionPreset(
        id="kharkiv_oblast",
        patterns=(
            r"\bхарківщин(а|и|і|у|ою)\b",
            r"\bхарківськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
        ),
        localities={
            "kharkiv_oblast_balakliia": LocalityPreset(
                id="kharkiv_oblast_balakliia", patterns=(r"\bбалаклі(я|ї|ю|єю)\b",)
            ),
            "kharkiv_oblast_bohodukhiv": LocalityPreset(
                id="kharkiv_oblast_bohodukhiv",
                patterns=(r"\bбогодух(ів|ова|ову|овом|ові)\b",),
            ),
            "kharkiv_oblast_derzhprom": LocalityPreset(
                id="kharkiv_oblast_derzhprom", patterns=(r"\bдержпром(у|і|ом|а)?\b",)
            ),
            "kharkiv_oblast_kharkiv": LocalityPreset(
                id="kharkiv_oblast_kharkiv",
                patterns=(r"\bхарк(ів|ова|ову|овом|ові)\b",),
            ),
            "kharkiv_oblast_khtz": LocalityPreset(
                id="kharkiv_oblast_khtz", patterns=(r"\bхтз\b",)
            ),
            "kharkiv_oblast_kozacha_lopan": LocalityPreset(
                id="kharkiv_oblast_kozacha_lopan",
                patterns=(r"\bкозач(а|у|ою) лопан(ь|і|ню|ью)\b",),
            ),
            "kharkiv_oblast_kulynychi": LocalityPreset(
                id="kharkiv_oblast_kulynychi",
                patterns=(r"\bкулинич(і|ів|ам|ами|ах)\b",),
            ),
            "kharkiv_oblast_kupiansk": LocalityPreset(
                id="kharkiv_oblast_kupiansk",
                patterns=(r"\bкуп['’ʼ]?янськ(а|у|ом|і)?\b",),
            ),
            "kharkiv_oblast_piatykhatky": LocalityPreset(
                id="kharkiv_oblast_piatykhatky",
                patterns=(r"\bп['’ʼ]?ятихатк(и|ах|ам|ами)\b",),
            ),
            "kharkiv_oblast_saltivka": LocalityPreset(
                id="kharkiv_oblast_saltivka",
                patterns=(r"\bсалтівк(а|и|і|у|ою|о)\b",),
            ),
        },
    ),
    "kherson_oblast": RegionPreset(
        id="kherson_oblast",
        patterns=(
            r"\bхерсонщин(а|и|і|у|ою)\b",
            r"\bхерсонськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
        ),
        localities={
            "kherson_oblast_kherson": LocalityPreset(
                id="kherson_oblast_kherson", patterns=(r"\bхерсон(а|у|ом|і)?\b",)
            ),
        },
    ),
    "khmelnytskyi_oblast": RegionPreset(
        id="khmelnytskyi_oblast",
        patterns=(
            r"\bхмельниччин(а|и|і|у|ою)\b",
            r"\bхмельницьк(а|ої|ій|у|ою) област(ь|і|ю)\b",
        ),
        localities={
            "khmelnytskyi_oblast_khmelnytskyi": LocalityPreset(
                id="khmelnytskyi_oblast_khmelnytskyi",
                patterns=(r"\bхмельницьк(ий|ого|ому|им|ім)\b",),
            ),
        },
    ),
    "kirovohrad_oblast": RegionPreset(
        id="kirovohrad_oblast",
        patterns=(
            r"\bкіровоградщин(а|и|і|у|ою)\b",
            r"\bкіровоградськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
        ),
        localities={
            "kirovohrad_oblast_kropyvnytskyi": LocalityPreset(
                id="kirovohrad_oblast_kropyvnytskyi",
                patterns=(r"\bкропивницьк(ий|ого|ому|им|ім)\b",),
            ),
        },
    ),
    "kyiv": RegionPreset(
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
            "kyiv_dorohzhychi": LocalityPreset(
                id="kyiv_dorohzhychi", patterns=(r"\bдорогожич(і|ів|ам|ами|ах)\b",)
            ),
            "kyiv_dvrz": LocalityPreset(id="kyiv_dvrz", patterns=(r"\bдврз\b",)),
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
                id="kyiv_klov", patterns=(r"\bклов(у|і|ом|а)?\b",)
            ),
            "kyiv_koncha_zaspa": LocalityPreset(
                id="kyiv_koncha_zaspa",
                patterns=(
                    r"\bконч(а|і)[ -]засп(а|и|і|у|ою)\b",
                    r"\bзасп(а|и|і|у|ою)\b",
                ),
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
                # TODO: пуща  # noqa: TD002
                patterns=(r"\bпущ(а|і|у|ею)[ -]водиц(я|і|ю|ею)\b",),
            ),
            "kyiv_rembaza": LocalityPreset(
                id="kyiv_rembaza", patterns=(r"\bрембаз(а|и|і|у|ою)\b",)
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
            "kyiv_shuliavka": LocalityPreset(
                id="kyiv_shuliavka", patterns=(r"\bшулявк(а|и|у|ою|ці)\b",)
            ),
            "kyiv_solomianka": LocalityPreset(
                id="kyiv_solomianka",
                patterns=(
                    r"\bсолом(а|['’ʼ]?янк(а|и|у|ою|ці))\b",
                    r"\bсолом['’ʼ]?янськ(ий|ого|ому|им)\b",
                ),
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
    ),
    "kyiv_oblast": RegionPreset(
        id="kyiv_oblast",
        patterns=(
            r"\bкиївщин(а|и|і|у|ою)\b",
            r"\bкиївськ(а|ої|ій|у|ою|і|их|им|ими) област(ь|і|ю|ей|ям|ями|ях)\b",
        ),
        localities={
            "kyiv_oblast_bila_tserkva": LocalityPreset(
                id="kyiv_oblast_bila_tserkva",
                patterns=(
                    r"\bбіл(а|ої|ій|у|ою) церкв(а|и|і|у|ою)\b",
                    r"\bбц\b",
                ),
            ),
            "kyiv_oblast_boryspil": LocalityPreset(
                id="kyiv_oblast_boryspil",
                patterns=(
                    r"\bборисп(іль|оля|олю|олем|олі)\b",
                    r"\bборік\b",
                ),
            ),
            "kyiv_oblast_brovary": LocalityPreset(
                id="kyiv_oblast_brovary",
                patterns=(r"\bбровар(и|ів|ам|ами|ах)\b",),
            ),
            "kyiv_oblast_bucha": LocalityPreset(
                id="kyiv_oblast_bucha", patterns=(r"\bбуч(а|і|у|ею)\b",)
            ),
            "kyiv_oblast_chaiky": LocalityPreset(
                id="kyiv_oblast_chaiky", patterns=(r"\bчайк(и|ів|ам|ами|ах)\b",)
            ),
            "kyiv_oblast_dymer": LocalityPreset(
                id="kyiv_oblast_dymer", patterns=(r"\bдимер(а|у|ом|і)?\b",)
            ),
            "kyiv_oblast_hnidyn": LocalityPreset(
                id="kyiv_oblast_hnidyn", patterns=(r"\bгнідин(а|у|ом|і)?\b",)
            ),
            "kyiv_oblast_hostomel": LocalityPreset(
                id="kyiv_oblast_hostomel", patterns=(r"\bгостомел(ь|я|ю|ем|і)\b",)
            ),
            "kyiv_oblast_hotianivka": LocalityPreset(
                id="kyiv_oblast_hotianivka", patterns=(r"\bхотянівк(а|и|у|ою|ці)\b",)
            ),
            "kyiv_oblast_irpin": LocalityPreset(
                id="kyiv_oblast_irpin", patterns=(r"\bірп(інь|еня|еню|енем|ені)\b",)
            ),
            "kyiv_oblast_kotsiubynske": LocalityPreset(
                id="kyiv_oblast_kotsiubynske",
                patterns=(r"\bкоцюбинськ(е|ого|ому|им|ім)\b",),
            ),
            "kyiv_oblast_kozyn": LocalityPreset(
                id="kyiv_oblast_kozyn", patterns=(r"\bкозин(а|у|ом|і)?\b",)
            ),
            "kyiv_oblast_obukhiv": LocalityPreset(
                id="kyiv_oblast_obukhiv", patterns=(r"\bобух(ів|ова|ову|овом|ові)\b",)
            ),
            "kyiv_oblast_petrivtsi": LocalityPreset(
                id="kyiv_oblast_petrivtsi", patterns=(r"\bпетрівц(і|ів|ям|ями|ях)\b",)
            ),
            "kyiv_oblast_petropavlivska_borshchahivka": LocalityPreset(
                id="kyiv_oblast_petropavlivska_borshchahivka",
                patterns=(
                    r"\bпетропавлівськ(а|ої|ій|у|ою) борщагівк(а|и|і|у|ою|ці)\b",
                ),
            ),
            "kyiv_oblast_pohreby": LocalityPreset(
                id="kyiv_oblast_pohreby", patterns=(r"\bпогреб(и|ів|ам|ами|ах)\b",)
            ),
            "kyiv_oblast_prolisky": LocalityPreset(
                id="kyiv_oblast_prolisky",
                patterns=(r"\bпроліс(ки|ків|кам|ками|ках)\b",),
            ),
            "kyiv_oblast_sofiivska_borshchahivka": LocalityPreset(
                id="kyiv_oblast_sofiivska_borshchahivka",
                patterns=(r"\bсофіївськ(а|ої|ій|у|ою) борщагівк(а|и|і|у|ою|ці)\b",),
            ),
            "kyiv_oblast_ukrainka": LocalityPreset(
                id="kyiv_oblast_ukrainka", patterns=(r"\bукраїнк(а|и|у|ою|ці)\b",)
            ),
            "kyiv_oblast_vasylkiv": LocalityPreset(
                id="kyiv_oblast_vasylkiv", patterns=(r"\bвасильков(а|у|ом|і)?\b",)
            ),
            "kyiv_oblast_vorzel": LocalityPreset(
                id="kyiv_oblast_vorzel", patterns=(r"\bворзел(ь|я|ю|ем|і)\b",)
            ),
            "kyiv_oblast_vyshhorod": LocalityPreset(
                id="kyiv_oblast_vyshhorod", patterns=(r"\bвишгород(у|і|ом|а)?\b",)
            ),
            "kyiv_oblast_vyshneve": LocalityPreset(
                id="kyiv_oblast_vyshneve", patterns=(r"\bвишнев(е|ого|ому|им|ім)\b",)
            ),
            "kyiv_oblast_zazyma": LocalityPreset(
                id="kyiv_oblast_zazyma", patterns=(r"\bзазим['’ʼ]?(я|ї|ям)\b",)
            ),
            "kyiv_oblast_zhk_sofiia": LocalityPreset(
                id="kyiv_oblast_zhk_sofiia",
                patterns=(r"\bжк[. ]+[«\"]?софі(я|ї|ю|єю)\b",),
            ),
        },
    ),
    "luhansk_oblast": RegionPreset(
        id="luhansk_oblast",
        patterns=(
            r"\bлуганщин(а|и|і|у|ою)\b",
            r"\bлуганськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
        ),
        localities={
            "luhansk_oblast_luhansk": LocalityPreset(
                id="luhansk_oblast_luhansk",
                patterns=(r"\bлуганськ(у|ом|і)?\b",),
            ),
        },
    ),
    "lviv_oblast": RegionPreset(
        id="lviv_oblast",
        patterns=(
            r"\bльвівщин(а|и|і|у|ою)\b",
            r"\bльвівськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
        ),
        localities={
            "lviv_oblast_lviv": LocalityPreset(
                id="lviv_oblast_lviv", patterns=(r"\bльв(ів|ова|ову|овом|ові)\b",)
            ),
        },
    ),
    "mykolaiv_oblast": RegionPreset(
        id="mykolaiv_oblast",
        patterns=(
            r"\bмиколаївщин(а|и|і|у|ою)\b",
            r"\bмиколаївськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
        ),
        localities={
            "mykolaiv_oblast_mykolaiv": LocalityPreset(
                id="mykolaiv_oblast_mykolaiv",
                patterns=(r"\bмикола(їв|єва|єві|єву|євом)\b",),
            ),
        },
    ),
    "odesa_oblast": RegionPreset(
        id="odesa_oblast",
        patterns=(
            r"\bодещин(а|и|і|у|ою)\b",
            r"\bодеськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
        ),
        localities={
            "odesa_oblast_arkadiia": LocalityPreset(
                id="odesa_oblast_arkadiia", patterns=(r"\bаркаді(я|ї|ю|єю)\b",)
            ),
            "odesa_oblast_bilhorod_dnistrovskyi": LocalityPreset(
                id="odesa_oblast_bilhorod_dnistrovskyi",
                patterns=(r"\bбілгород[ -]дністровськ(ий|ого|ому|им|ім)\b",),
            ),
            "odesa_oblast_chornomorsk": LocalityPreset(
                id="odesa_oblast_chornomorsk", patterns=(r"\bчорноморськ(а|у|ом|і)?\b",)
            ),
            "odesa_oblast_karolino_buhaz": LocalityPreset(
                id="odesa_oblast_karolino_buhaz",
                patterns=(r"\bкароліно[ -]бугаз(у|і|ом|а)?\b",),
            ),
            "odesa_oblast_khadzhybeiskyi_raion": LocalityPreset(
                id="odesa_oblast_khadzhybeiskyi_raion",
                patterns=(r"\bхаджибейськ(ий|ого|ому|им|ім) район(у|і|ом)?\b",),
            ),
            "odesa_oblast_odesa": LocalityPreset(
                id="odesa_oblast_odesa", patterns=(r"\bодес(а|и|і|у|ою)\b",)
            ),
            "odesa_oblast_odesa_port": LocalityPreset(
                id="odesa_oblast_odesa_port",
                patterns=(
                    r"\bодеськ(ий|ого|ому|им|ім) порт(у|і|ом|а)?\b",
                    r"\bодес(а|и|і|у|ою)\s*[ /-]\s*порт(у|і|ом|а)?\b",
                ),
            ),
            "odesa_oblast_ovidiopol": LocalityPreset(
                id="odesa_oblast_ovidiopol", patterns=(r"\bовідіопол(ь|я|і|ю|ем)\b",)
            ),
            "odesa_oblast_peresyp": LocalityPreset(
                id="odesa_oblast_peresyp", patterns=(r"\bпересип(у|ом|і)?\b",)
            ),
            "odesa_oblast_zatoka": LocalityPreset(
                id="odesa_oblast_zatoka", patterns=(r"\bзаток(а|и|у|ою|ці)\b",)
            ),
        },
    ),
    "poltava_oblast": RegionPreset(
        id="poltava_oblast",
        patterns=(
            r"\bполтавщин(а|и|і|у|ою)\b",
            r"\bполтавськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
        ),
        localities={
            "poltava_oblast_poltava": LocalityPreset(
                id="poltava_oblast_poltava", patterns=(r"\bполтав(а|и|і|у|ою)\b",)
            ),
        },
    ),
    "rivne_oblast": RegionPreset(
        id="rivne_oblast",
        patterns=(
            r"\bрівненщин(а|и|і|у|ою)\b",
            r"\bрівненськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
        ),
        localities={
            "rivne_oblast_rivne": LocalityPreset(
                id="rivne_oblast_rivne", patterns=(r"\bрівне\b",)
            ),
        },
    ),
    "sumy_oblast": RegionPreset(
        id="sumy_oblast",
        patterns=(
            r"\bсумщин(а|и|і|у|ою)\b",
            r"\bсумськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
        ),
        localities={
            "sumy_oblast_sumy": LocalityPreset(
                id="sumy_oblast_sumy", patterns=(r"\bсум(и|ах|ами)?\b",)
            ),
        },
    ),
    "ternopil_oblast": RegionPreset(
        id="ternopil_oblast",
        patterns=(
            r"\bтернопільщин(а|и|і|у|ою)\b",
            r"\bтернопільськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
        ),
        localities={
            "ternopil_oblast_ternopil": LocalityPreset(
                id="ternopil_oblast_ternopil",
                patterns=(r"\bтерноп(іль|оля|олю|олем|олі)\b",),
            ),
        },
    ),
    "vinnytsia_oblast": RegionPreset(
        id="vinnytsia_oblast",
        patterns=(
            r"\bвінниччин(а|и|і|у|ою)\b",
            r"\bвінницьк(а|ої|ій|у|ою) област(ь|і|ю)\b",
        ),
        localities={
            "vinnytsia_oblast_vinnytsia": LocalityPreset(
                id="vinnytsia_oblast_vinnytsia", patterns=(r"\bвінниц(я|і|ю|ею)\b",)
            ),
        },
    ),
    "volyn_oblast": RegionPreset(
        id="volyn_oblast",
        patterns=(
            r"\bволин(ь|і|ню)\b",
            r"\bволинськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
        ),
        localities={
            "volyn_oblast_lutsk": LocalityPreset(
                id="volyn_oblast_lutsk", patterns=(r"\bлуцьк(а|у|ом|ові)?\b",)
            ),
        },
    ),
    "zakarpattia_oblast": RegionPreset(
        id="zakarpattia_oblast",
        patterns=(r"\bзакарпатськ(а|ої|ій|у|ою) област(ь|і|ю)\b",),
        localities={
            "zakarpattia_oblast_uzhhorod": LocalityPreset(
                id="zakarpattia_oblast_uzhhorod", patterns=(r"\bужгород(а|у|ом|і)?\b",)
            ),
        },
    ),
    "zaporizhzhia_oblast": RegionPreset(
        id="zaporizhzhia_oblast",
        patterns=(r"\bзапорізьк(а|ої|ій|у|ою) област(ь|і|ю)\b",),
        localities={
            "zaporizhzhia_oblast_komyshuvakha": LocalityPreset(
                id="zaporizhzhia_oblast_komyshuvakha",
                patterns=(r"\bкомишувах(а|и|і|у|ою)\b",),
            ),
            "zaporizhzhia_oblast_orikhiv": LocalityPreset(
                id="zaporizhzhia_oblast_orikhiv",
                patterns=(r"\bоріх(ів|ова|ову|ові|овом)\b",),
            ),
            "zaporizhzhia_oblast_vilniansk": LocalityPreset(
                id="zaporizhzhia_oblast_vilniansk",
                patterns=(r"\bвільнянськ(а|у|і|ом)?\b",),
            ),
            "zaporizhzhia_oblast_zaporizhzhia": LocalityPreset(
                id="zaporizhzhia_oblast_zaporizhzhia",
                patterns=(
                    r"\bзапоріжж(я|і|ю|ям)\b",
                    r"\bзп\b",
                ),
            ),
        },
    ),
    "zhytomyr_oblast": RegionPreset(
        id="zhytomyr_oblast",
        patterns=(
            r"\bжитомирщин(а|и|і|у|ою)\b",
            r"\bжитомирськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
        ),
        localities={
            "zhytomyr_oblast_zhytomyr": LocalityPreset(
                id="zhytomyr_oblast_zhytomyr", patterns=(r"\bжитомир(а|у|ом|і)?\b",)
            ),
        },
    ),
}
