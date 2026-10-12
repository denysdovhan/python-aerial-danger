"""Location presets for vinnytsia oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

VINNYTSIA_OBLAST_REGION: Final = RegionPreset(
    id="vinnytsia_oblast",
    patterns=(
        r"\bвінниччин(а|и|і|у|ою)\b",
        r"\bвінницьк(а|ої|ій|у|ою) област(ь|і|ю)\b",
    ),
    localities={
        "vinnytsia_oblast_bar": LocalityPreset(
            id="vinnytsia_oblast_bar",
            patterns=(r"\bбар(а|у|ом|і)?\b",),
        ),
        "vinnytsia_oblast_bershad": LocalityPreset(
            id="vinnytsia_oblast_bershad",
            patterns=(r"\bбершад(ь|і|дю)\b",),
        ),
        "vinnytsia_oblast_bratslav": LocalityPreset(
            id="vinnytsia_oblast_bratslav",
            patterns=(r"\bбрацлав(а|у|ом|і)?\b",),
        ),
        "vinnytsia_oblast_chechelnyk": LocalityPreset(
            id="vinnytsia_oblast_chechelnyk",
            patterns=(r"\bчечельник(а|у|ом|і)?\b",),
        ),
        "vinnytsia_oblast_dashiv": LocalityPreset(
            id="vinnytsia_oblast_dashiv",
            patterns=(r"\bдаш(ів|ова|ову|овом|ові)\b",),
        ),
        "vinnytsia_oblast_haisyn": LocalityPreset(
            id="vinnytsia_oblast_haisyn",
            patterns=(r"\bгайсин(а|у|ом|і)?\b",),
        ),
        "vinnytsia_oblast_hlukhivtsi": LocalityPreset(
            id="vinnytsia_oblast_hlukhivtsi",
            patterns=(r"\bглухівц(і|ів|ям|ями|ях)\b",),
        ),
        "vinnytsia_oblast_hnivan": LocalityPreset(
            id="vinnytsia_oblast_hnivan",
            patterns=(r"\bгніван(ь|і|ню)\b",),
        ),
        "vinnytsia_oblast_illintsi": LocalityPreset(
            id="vinnytsia_oblast_illintsi",
            patterns=(r"\bіллін(ці|ців|цям|цями|цях)\b",),
        ),
        "vinnytsia_oblast_khmilnyk": LocalityPreset(
            id="vinnytsia_oblast_khmilnyk",
            patterns=(r"\bхмільник(а|у|ом|і)?\b",),
        ),
        "vinnytsia_oblast_kopaihorod": LocalityPreset(
            id="vinnytsia_oblast_kopaihorod",
            patterns=(r"\bкопайгород(а|у|ом|і)?\b",),
        ),
        "vinnytsia_oblast_koziatyn": LocalityPreset(
            id="vinnytsia_oblast_koziatyn",
            patterns=(r"\bкозятин(а|у|ом|і)?\b",),
        ),
        "vinnytsia_oblast_kryzhopil": LocalityPreset(
            id="vinnytsia_oblast_kryzhopil",
            patterns=(r"\bкрижоп(іль|оля|олю|олем|олі)\b",),
        ),
        "vinnytsia_oblast_ladyzhyn": LocalityPreset(
            id="vinnytsia_oblast_ladyzhyn",
            patterns=(r"\bладижин(а|у|ом|і)?\b",),
        ),
        "vinnytsia_oblast_lypovets": LocalityPreset(
            id="vinnytsia_oblast_lypovets",
            patterns=(r"\bлипов(ець|ця|цю|цем|ці)\b",),
        ),
        "vinnytsia_oblast_murovani_kurylivtsi": LocalityPreset(
            id="vinnytsia_oblast_murovani_kurylivtsi",
            patterns=(r"\bмурован(і|их|им|ими)\s+курилівц(і|ів|ям|ями|ях)\b",),
        ),
        "vinnytsia_oblast_nemyriv": LocalityPreset(
            id="vinnytsia_oblast_nemyriv",
            patterns=(r"\bнемир(ів|ова|ову|овом|ові)\b",),
        ),
        "vinnytsia_oblast_orativ": LocalityPreset(
            id="vinnytsia_oblast_orativ",
            patterns=(r"\bорат(ів|ова|ову|овом|ові)\b",),
        ),
        "vinnytsia_oblast_pohrebyshche": LocalityPreset(
            id="vinnytsia_oblast_pohrebyshche",
            patterns=(r"\bпогребищ(е|а|у|ем|і)\b",),
        ),
        "vinnytsia_oblast_rakhny_lisovi": LocalityPreset(
            id="vinnytsia_oblast_rakhny_lisovi",
            patterns=(r"\bрахн(и|ів|ам|ами|ах)[ -]лісов(і|их|им|ими)\b",),
        ),
        "vinnytsia_oblast_sharhorod": LocalityPreset(
            id="vinnytsia_oblast_sharhorod",
            patterns=(r"\bшаргород(а|у|ом|і)?\b",),
        ),
        "vinnytsia_oblast_shpykiv": LocalityPreset(
            id="vinnytsia_oblast_shpykiv",
            patterns=(r"\bшпик(ів|ова|ову|овом|ові)\b",),
        ),
        "vinnytsia_oblast_sytkivtsi": LocalityPreset(
            id="vinnytsia_oblast_sytkivtsi",
            patterns=(r"\bситківц(і|ів|ям|ями|ях)\b",),
        ),
        "vinnytsia_oblast_teplyk": LocalityPreset(
            id="vinnytsia_oblast_teplyk",
            patterns=(r"\bтеплик(а|у|ом|і)?\b",),
        ),
        "vinnytsia_oblast_tomashpil": LocalityPreset(
            id="vinnytsia_oblast_tomashpil",
            patterns=(r"\bтомашп(іль|оля|олю|олем|олі)\b",),
        ),
        "vinnytsia_oblast_trostianets": LocalityPreset(
            id="vinnytsia_oblast_trostianets", patterns=(r"\bтростянець\b",)
        ),
        "vinnytsia_oblast_tulchyn": LocalityPreset(
            id="vinnytsia_oblast_tulchyn",
            patterns=(r"\bтульчин(а|у|ом|і)?\b",),
        ),
        "vinnytsia_oblast_turbiv": LocalityPreset(
            id="vinnytsia_oblast_turbiv",
            patterns=(r"\bтурб(ів|ова|ову|овом|ові)\b",),
        ),
        "vinnytsia_oblast_tyvriv": LocalityPreset(
            id="vinnytsia_oblast_tyvriv",
            patterns=(r"\bтивр(ів|ова|ову|овом|ові)\b",),
        ),
        "vinnytsia_oblast_ulaniv": LocalityPreset(
            id="vinnytsia_oblast_ulaniv",
            patterns=(r"\bулан(ів|ова|ову|овом|ові)\b",),
        ),
        "vinnytsia_oblast_vapniarka": LocalityPreset(
            id="vinnytsia_oblast_vapniarka", patterns=(r"\bвапнярку\b",)
        ),
        "vinnytsia_oblast_vinnytsia": LocalityPreset(
            id="vinnytsia_oblast_vinnytsia", patterns=(r"\bвінниц(я|і|ю|ею)\b",)
        ),
        "vinnytsia_oblast_voronovytsia": LocalityPreset(
            id="vinnytsia_oblast_voronovytsia",
            patterns=(r"\bвороновиц(я|і|ю|ею)\b",),
        ),
        "vinnytsia_oblast_zhmerynka": LocalityPreset(
            id="vinnytsia_oblast_zhmerynka", patterns=(r"\bжмеринк(а|и|у)\b",)
        ),
    },
)
