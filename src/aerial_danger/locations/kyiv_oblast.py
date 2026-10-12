"""Location presets for kyiv oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

KYIV_OBLAST_REGION: Final = RegionPreset(
    id="kyiv_oblast",
    patterns=(
        r"\bкиївщин(а|и|і|у|ою)\b",
        r"\bкиївськ(а|ої|ій|у|ою|і|их|им|ими) област(ь|і|ю|ей|ям|ями|ях)\b",
    ),
    localities={
        "kyiv_oblast_baryshivka": LocalityPreset(
            id="kyiv_oblast_baryshivka", patterns=(r"\bбаришівк(а|и|у|ою|і)\b",)
        ),
        "kyiv_oblast_berezan": LocalityPreset(
            id="kyiv_oblast_berezan", patterns=(r"\bберезан(ь|і)\b",)
        ),
        "kyiv_oblast_bila_tserkva": LocalityPreset(
            id="kyiv_oblast_bila_tserkva",
            patterns=(
                r"\bбіл(а|ої|ій|у|ою) церкв(а|и|і|у|ою)\b",
                r"\bбц\b",
            ),
        ),
        "kyiv_oblast_bilohorodka": LocalityPreset(
            id="kyiv_oblast_bilohorodka", patterns=(r"\bбілогородк(а|и|у|ою|і)\b",)
        ),
        "kyiv_oblast_bohuslav": LocalityPreset(
            id="kyiv_oblast_bohuslav", patterns=(r"\bбогуслав(а|ом)?\b",)
        ),
        "kyiv_oblast_borodianka": LocalityPreset(
            id="kyiv_oblast_borodianka", patterns=(r"\bбородянк(а|и|у|ою|і)\b",)
        ),
        "kyiv_oblast_boryspil": LocalityPreset(
            id="kyiv_oblast_boryspil",
            patterns=(
                r"\bборисп(іль|оля|олю|олем|олі)\b",
                r"\bборік\b",
            ),
        ),
        "kyiv_oblast_boyarka": LocalityPreset(
            id="kyiv_oblast_boyarka", patterns=(r"\bбоярк(у|а|и|ою)\b",)
        ),
        "kyiv_oblast_brovary": LocalityPreset(
            id="kyiv_oblast_brovary",
            patterns=(r"\bбровар(и|ів|ам|ами|ах)\b",),
        ),
        "kyiv_oblast_bucha": LocalityPreset(
            id="kyiv_oblast_bucha", patterns=(r"\bбуч(а|і|у|ею)\b",)
        ),
        "kyiv_oblast_buzova": LocalityPreset(
            id="kyiv_oblast_buzova", patterns=(r"\bбузов(а|ої|у|ою|і)\b",)
        ),
        "kyiv_oblast_byshiv": LocalityPreset(
            id="kyiv_oblast_byshiv", patterns=(r"\bбишів\b",)
        ),
        "kyiv_oblast_chabany": LocalityPreset(
            id="kyiv_oblast_chabany", patterns=(r"\bчабан(и|ів)\b",)
        ),
        "kyiv_oblast_chaiky": LocalityPreset(
            id="kyiv_oblast_chaiky", patterns=(r"\bчайк(и|ів|ам|ами|ах)\b",)
        ),
        "kyiv_oblast_chornobyl": LocalityPreset(
            id="kyiv_oblast_chornobyl", patterns=(r"\bчорнобил(ь|я|ю|ем|і)\b",)
        ),
        "kyiv_oblast_dudarkiv": LocalityPreset(
            id="kyiv_oblast_dudarkiv",
            patterns=(r"\bдудар(ків|кова|кову|ковом|кові)\b",),
        ),
        "kyiv_oblast_dymer": LocalityPreset(
            id="kyiv_oblast_dymer", patterns=(r"\bдимер(а|у|ом|і)?\b",)
        ),
        "kyiv_oblast_fastiv": LocalityPreset(
            id="kyiv_oblast_fastiv", patterns=(r"\bфаст(ів|ова|ову|овом|ові)\b",)
        ),
        "kyiv_oblast_fenevychi": LocalityPreset(
            id="kyiv_oblast_fenevychi", patterns=(r"\bфеневич(і|ів|ам|ами|ах)\b",)
        ),
        "kyiv_oblast_gatne": LocalityPreset(
            id="kyiv_oblast_gatne", patterns=(r"\bгатн(е|ого|ому|им|ім)\b",)
        ),
        "kyiv_oblast_hlevakha": LocalityPreset(
            id="kyiv_oblast_hlevakha", patterns=(r"\bглевах(а|и|у|ою|і)\b",)
        ),
        "kyiv_oblast_hnidyn": LocalityPreset(
            id="kyiv_oblast_hnidyn", patterns=(r"\bгнідин(а|у|ом|і)?\b",)
        ),
        "kyiv_oblast_hoholiv": LocalityPreset(
            id="kyiv_oblast_hoholiv", patterns=(r"\bгогол(ів|ева|еву|евом|еві)\b",)
        ),
        "kyiv_oblast_horenka": LocalityPreset(
            id="kyiv_oblast_horenka", patterns=(r"\bгоренк(а|и|у|ою|і)\b",)
        ),
        "kyiv_oblast_horenychi": LocalityPreset(
            id="kyiv_oblast_horenychi", patterns=(r"\bгоренич(і|ів|ам|ами|ах)\b",)
        ),
        "kyiv_oblast_hostomel": LocalityPreset(
            id="kyiv_oblast_hostomel", patterns=(r"\bгостомел(ь|я|ю|ем|і)\b",)
        ),
        "kyiv_oblast_hotianivka": LocalityPreset(
            id="kyiv_oblast_hotianivka", patterns=(r"\bхотянівк(а|и|у|ою|ці)\b",)
        ),
        "kyiv_oblast_hrebinky": LocalityPreset(
            id="kyiv_oblast_hrebinky", patterns=(r"\bгребінк(и|ів|ам|ами|ах)\b",)
        ),
        "kyiv_oblast_irpin": LocalityPreset(
            id="kyiv_oblast_irpin", patterns=(r"\bірп(інь|еня|еню|енем|ені)\b",)
        ),
        "kyiv_oblast_ivankiv": LocalityPreset(
            id="kyiv_oblast_ivankiv", patterns=(r"\bіван(ків|кова|кову|ковом|кові)\b",)
        ),
        "kyiv_oblast_ivankovychi": LocalityPreset(
            id="kyiv_oblast_ivankovychi",
            patterns=(r"\bіванкович(і|ів|ам|ами|ах)\b",),
        ),
        "kyiv_oblast_kaharlyk": LocalityPreset(
            id="kyiv_oblast_kaharlyk", patterns=(r"\bкагарлик(а)?\b",)
        ),
        "kyiv_oblast_kalita": LocalityPreset(
            id="kyiv_oblast_kalita", patterns=(r"\bкалит(а|и|у|ою|і)\b",)
        ),
        "kyiv_oblast_katiuzhanka": LocalityPreset(
            id="kyiv_oblast_katiuzhanka", patterns=(r"\bкатюжанк(а|и|у|ою|і)\b",)
        ),
        "kyiv_oblast_khodosivka": LocalityPreset(
            id="kyiv_oblast_khodosivka", patterns=(r"\bходосівк(а|и|у|ою|і)\b",)
        ),
        "kyiv_oblast_khotiv": LocalityPreset(
            id="kyiv_oblast_khotiv",
            patterns=(
                r"\b(на|до|у|в|через|повз|поблизу|районі|курс|курсом)\s+хотів\b",
                r"\bхотів(?=\s*(?:[-/!?.:,]|сектор|увага|бпла|ще|на|та|поки))",
                r"(?m)^[ \t]*хотів[.!]*[ \t]*$",
            ),
        ),
        "kyiv_oblast_khotsky": LocalityPreset(
            id="kyiv_oblast_khotsky", patterns=(r"\bхоцьк(и|ів|ам|ами|ах)\b",)
        ),
        "kyiv_oblast_kniazhychi": LocalityPreset(
            id="kyiv_oblast_kniazhychi",
            patterns=(r"\bкняжич(і|ів)\b",),
        ),
        "kyiv_oblast_kotsiubynske": LocalityPreset(
            id="kyiv_oblast_kotsiubynske",
            patterns=(r"\bкоцюбинськ(е|ого|ому|им|ім)\b",),
        ),
        "kyiv_oblast_kozyn": LocalityPreset(
            id="kyiv_oblast_kozyn", patterns=(r"\bкозин(а|у|ом|і)?\b",)
        ),
        "kyiv_oblast_krasiatychi": LocalityPreset(
            id="kyiv_oblast_krasiatychi",
            patterns=(r"\bкрасятич(і|ів|ам|ами|ах)\b",),
        ),
        "kyiv_oblast_kriukivshchyna": LocalityPreset(
            id="kyiv_oblast_kriukivshchyna",
            patterns=(r"\bкрюківщин(а|и|у|ою|і)\b",),
        ),
        "kyiv_oblast_kruhlyk": LocalityPreset(
            id="kyiv_oblast_kruhlyk", patterns=(r"\bкруглик(а|у|ом|і)?\b",)
        ),
        "kyiv_oblast_krushynka": LocalityPreset(
            id="kyiv_oblast_krushynka", patterns=(r"\bкрушинк(а|и|у|ою|і)\b",)
        ),
        "kyiv_oblast_kryachky": LocalityPreset(
            id="kyiv_oblast_kryachky", patterns=(r"\bкрячк(и|ів|ам|ами|ах)\b",)
        ),
        "kyiv_oblast_lebedivka": LocalityPreset(
            id="kyiv_oblast_lebedivka",
            patterns=(r"\bлебедівк(а|у|и)\b",),
        ),
        "kyiv_oblast_lisnyky": LocalityPreset(
            id="kyiv_oblast_lisnyky", patterns=(r"\bлісники\b",)
        ),
        "kyiv_oblast_liubartsi": LocalityPreset(
            id="kyiv_oblast_liubartsi", patterns=(r"\bлюбарц(і|ів|ям|ями|ях)\b",)
        ),
        "kyiv_oblast_liutizh": LocalityPreset(
            id="kyiv_oblast_liutizh", patterns=(r"\bлютіж\b",)
        ),
        "kyiv_oblast_makariv": LocalityPreset(
            id="kyiv_oblast_makariv", patterns=(r"\bмакар(ів|ова|ову|овом|ові)\b",)
        ),
        "kyiv_oblast_maliutianka": LocalityPreset(
            id="kyiv_oblast_maliutianka", patterns=(r"\bмалютянк(а|и|у|ою|і)\b",)
        ),
        "kyiv_oblast_markhalivka": LocalityPreset(
            id="kyiv_oblast_markhalivka", patterns=(r"\bмархалівк(а|и|у|ою|і)\b",)
        ),
        "kyiv_oblast_moshchun": LocalityPreset(
            id="kyiv_oblast_moshchun", patterns=(r"\bмощун(а|у|ом|і)?\b",)
        ),
        "kyiv_oblast_myronivka": LocalityPreset(
            id="kyiv_oblast_myronivka", patterns=(r"\bмиронівк(у|и|а)\b",)
        ),
        "kyiv_oblast_nemishaieve": LocalityPreset(
            id="kyiv_oblast_nemishaieve",
            patterns=(r"\bнемішаєв(е|о|ого|ому|им|ім)\b",),
        ),
        "kyiv_oblast_novosilky": LocalityPreset(
            id="kyiv_oblast_novosilky",
            patterns=(r"\bновосілк(и|ів|ам|ами|ах)\b",),
        ),
        "kyiv_oblast_obukhiv": LocalityPreset(
            id="kyiv_oblast_obukhiv", patterns=(r"\bобух(ів|ова|ову|овом|ові)\b",)
        ),
        "kyiv_oblast_oseshchyna": LocalityPreset(
            id="kyiv_oblast_oseshchyna", patterns=(r"\bосещин(а|и|у|ою|і)\b",)
        ),
        "kyiv_oblast_pereiaslav": LocalityPreset(
            id="kyiv_oblast_pereiaslav", patterns=(r"\bпереяслав(а|у|ом|і)?\b",)
        ),
        "kyiv_oblast_petrivtsi": LocalityPreset(
            id="kyiv_oblast_petrivtsi", patterns=(r"\bпетрівц(і|ів|ям|ями|ях)\b",)
        ),
        "kyiv_oblast_petropavlivska_borshchahivka": LocalityPreset(
            id="kyiv_oblast_petropavlivska_borshchahivka",
            patterns=(r"\bпетропавлівськ(а|ої|ій|у|ою) борщагівк(а|и|і|у|ою|ці)\b",),
        ),
        "kyiv_oblast_pidhirtsi": LocalityPreset(
            id="kyiv_oblast_pidhirtsi", patterns=(r"\bпідгірці\b",)
        ),
        "kyiv_oblast_piskivka": LocalityPreset(
            id="kyiv_oblast_piskivka", patterns=(r"\bпісківк(а|и|у|ою|і)\b",)
        ),
        "kyiv_oblast_plyuty": LocalityPreset(
            id="kyiv_oblast_plyuty", patterns=(r"\bплют(и|ів|ям|ями|ях)\b",)
        ),
        "kyiv_oblast_pohreby": LocalityPreset(
            id="kyiv_oblast_pohreby", patterns=(r"\bпогреб(и|ів|ам|ами|ах)\b",)
        ),
        "kyiv_oblast_prolisky": LocalityPreset(
            id="kyiv_oblast_prolisky",
            patterns=(r"\bпроліс(ки|ків|кам|ками|ках)\b",),
        ),
        "kyiv_oblast_protsiv": LocalityPreset(
            id="kyiv_oblast_protsiv", patterns=(r"\bпроц(ів|ева|еву|евом|еві)\b",)
        ),
        "kyiv_oblast_pukhivka": LocalityPreset(
            id="kyiv_oblast_pukhivka", patterns=(r"\bпухівк(а|и|у|ою|і)\b",)
        ),
        "kyiv_oblast_rohoziv": LocalityPreset(
            id="kyiv_oblast_rohoziv", patterns=(r"\bрогоз(ів|ова|ову|овом|ові)\b",)
        ),
        "kyiv_oblast_rozhivka": LocalityPreset(
            id="kyiv_oblast_rozhivka", patterns=(r"\bрожівк(а|и|у|ою|і)\b",)
        ),
        "kyiv_oblast_rozhny": LocalityPreset(
            id="kyiv_oblast_rozhny", patterns=(r"\bрожни\b",)
        ),
        "kyiv_oblast_rusaniv": LocalityPreset(
            id="kyiv_oblast_rusaniv", patterns=(r"\bрусанів\b",)
        ),
        "kyiv_oblast_rzhyshchiv": LocalityPreset(
            id="kyiv_oblast_rzhyshchiv", patterns=(r"\bржищ(ів|ева|еву|евом|еві)\b",)
        ),
        "kyiv_oblast_semypolky": LocalityPreset(
            id="kyiv_oblast_semypolky",
            patterns=(r"\bсемипол(ки|ок|кам|ками|ках)\b",),
        ),
        "kyiv_oblast_shchaslyve": LocalityPreset(
            id="kyiv_oblast_shchaslyve", patterns=(r"\bщасливе\b",)
        ),
        "kyiv_oblast_skibyn": LocalityPreset(
            id="kyiv_oblast_skibyn", patterns=(r"\bскибин(а|у|ом|і)?\b",)
        ),
        "kyiv_oblast_skvyra": LocalityPreset(
            id="kyiv_oblast_skvyra", patterns=(r"\bсквир(а|и|у|ою|і)\b",)
        ),
        "kyiv_oblast_slavutych": LocalityPreset(
            id="kyiv_oblast_slavutych", patterns=(r"\bславутич(а|у|ем|і)?\b",)
        ),
        "kyiv_oblast_sofiivska_borshchahivka": LocalityPreset(
            id="kyiv_oblast_sofiivska_borshchahivka",
            patterns=(
                r"\bсофіївськ(а|ої|ій|у|ою) борщагівк(а|и|і|у|ою|ці)\b",
                r"\bсоф\s+борщаг(?:а|у|и|ою)\b",
                r"\bсоф\b",
            ),
        ),
        "kyiv_oblast_stavyshche": LocalityPreset(
            id="kyiv_oblast_stavyshche", patterns=(r"\bставищ(е|а|ем)\b",)
        ),
        "kyiv_oblast_stoianka": LocalityPreset(
            id="kyiv_oblast_stoianka", patterns=(r"\bстоянк(а|и|у|ою|і)\b",)
        ),
        "kyiv_oblast_strakholissia": LocalityPreset(
            id="kyiv_oblast_strakholissia", patterns=(r"\bстрахолісс(я|і|ям)\b",)
        ),
        "kyiv_oblast_sukholuchchia": LocalityPreset(
            id="kyiv_oblast_sukholuchchia", patterns=(r"\bсухолучч(я|і|ям)\b",)
        ),
        "kyiv_oblast_suvid": LocalityPreset(
            id="kyiv_oblast_suvid", patterns=(r"\bсувид(а|у|ом|і)?\b",)
        ),
        "kyiv_oblast_sviatopetrivske": LocalityPreset(
            id="kyiv_oblast_sviatopetrivske",
            patterns=(r"\bсвятопетрівськ(е|ого|ому|им|ім)\b",),
        ),
        "kyiv_oblast_svitilnia": LocalityPreset(
            id="kyiv_oblast_svitilnia", patterns=(r"\bсвітильн(я|і|ю|ею)\b",)
        ),
        "kyiv_oblast_tarashcha": LocalityPreset(
            id="kyiv_oblast_tarashcha",
            patterns=(r"\bтаращ(у|і|а|ею)\b",),
        ),
        "kyiv_oblast_tatsenky": LocalityPreset(
            id="kyiv_oblast_tatsenky", patterns=(r"\bтаценк(и|ів|ам|ами|ах)\b",)
        ),
        "kyiv_oblast_tetiiv": LocalityPreset(
            id="kyiv_oblast_tetiiv",
            patterns=(r"\bтет(іїв|ієва|ієву|ієвом|ієві)\b",),
        ),
        "kyiv_oblast_trebukhiv": LocalityPreset(
            id="kyiv_oblast_trebukhiv",
            patterns=(r"\bтребух(ів|ова|ову|овом|ові)\b",),
        ),
        "kyiv_oblast_trypillia": LocalityPreset(
            id="kyiv_oblast_trypillia", patterns=(r"\bтрипілл(я|і|ям)\b",)
        ),
        "kyiv_oblast_ukrainka": LocalityPreset(
            id="kyiv_oblast_ukrainka", patterns=(r"\bукраїнк(а|и|у|ою|ці)\b",)
        ),
        "kyiv_oblast_uzyn": LocalityPreset(
            id="kyiv_oblast_uzyn", patterns=(r"\bузин(а|ом)?\b",)
        ),
        "kyiv_oblast_vasylkiv": LocalityPreset(
            id="kyiv_oblast_vasylkiv",
            patterns=(
                r"\bвасильков(а|у|ом|і)?\b",
                r"\bвасильків(а|у|ом|і)?\b",
                r"\bвасі\b",
                r"\bвасік(а|у|ом|і)?\b",
            ),
        ),
        "kyiv_oblast_velyka_dymerka": LocalityPreset(
            id="kyiv_oblast_velyka_dymerka",
            patterns=(r"\bвелик(а|ої|ій|у|ою) димерк(а|и|у|ою|і)\b",),
        ),
        "kyiv_oblast_vita_poshtova": LocalityPreset(
            id="kyiv_oblast_vita_poshtova",
            patterns=(r"\bвіт(а|и|і|у|ою)[ -]пошт(ова|ової|овій|ову|овою)\b",),
        ),
        "kyiv_oblast_voronkiv": LocalityPreset(
            id="kyiv_oblast_voronkiv",
            patterns=(r"\bвороньк(ів|ова|ову|овом|ові)\b",),
        ),
        "kyiv_oblast_vorzel": LocalityPreset(
            id="kyiv_oblast_vorzel", patterns=(r"\bворзел(ь|я|ю|ем|і)\b",)
        ),
        "kyiv_oblast_vyshenky": LocalityPreset(
            id="kyiv_oblast_vyshenky", patterns=(r"\bвишеньк(и|ок|ам|ами|ах)\b",)
        ),
        "kyiv_oblast_vyshhorod": LocalityPreset(
            id="kyiv_oblast_vyshhorod", patterns=(r"\bвишгород(у|і|ом|а)?\b",)
        ),
        "kyiv_oblast_vyshneve": LocalityPreset(
            id="kyiv_oblast_vyshneve", patterns=(r"\bвишнев(е|ого|ому|им|ім)\b",)
        ),
        "kyiv_oblast_yahotyn": LocalityPreset(
            id="kyiv_oblast_yahotyn", patterns=(r"\bяготин(а|у|ом|і)?\b",)
        ),
        "kyiv_oblast_yurivka": LocalityPreset(
            id="kyiv_oblast_yurivka", patterns=(r"\bюрівк(а|и|у|ою|і)\b",)
        ),
        "kyiv_oblast_zavorychi": LocalityPreset(
            id="kyiv_oblast_zavorychi", patterns=(r"\bзаворич(і|ів|ам|ами|ах)\b",)
        ),
        "kyiv_oblast_zazyma": LocalityPreset(
            id="kyiv_oblast_zazyma", patterns=(r"\bзазим['’ʼ]?(я|ї|ям)\b",)
        ),
        "kyiv_oblast_zghurivka": LocalityPreset(
            id="kyiv_oblast_zghurivka", patterns=(r"\bзгурівк(а|и|у|ою|і)\b",)
        ),
        "kyiv_oblast_zhk_sofiia": LocalityPreset(
            id="kyiv_oblast_zhk_sofiia",
            patterns=(r"\bжк[. ]+[«\"]?софі(я|ї|ю|єю)\b",),
        ),
        "kyiv_oblast_zhukyn": LocalityPreset(
            id="kyiv_oblast_zhukyn", patterns=(r"\bжукин(а|у|им|і)?\b",)
        ),
    },
)
