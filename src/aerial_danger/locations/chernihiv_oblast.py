"""Location presets for chernihiv oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

CHERNIHIV_OBLAST_REGION: Final = RegionPreset(
    id="chernihiv_oblast",
    patterns=(
        r"\bчернігівщин(а|и|і|у|ою)\b",
        r"\bчернігівськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
    ),
    localities={
        "chernihiv_oblast_bakhmach": LocalityPreset(
            id="chernihiv_oblast_bakhmach", patterns=(r"\bбахмач(а|у|ем|і)?\b",)
        ),
        "chernihiv_oblast_baturyn": LocalityPreset(
            id="chernihiv_oblast_baturyn", patterns=(r"\bбатурин(а|у|ом|і)?\b",)
        ),
        "chernihiv_oblast_bobrovytsia": LocalityPreset(
            id="chernihiv_oblast_bobrovytsia", patterns=(r"\bбобровиц(я|і|ю|ею)\b",)
        ),
        "chernihiv_oblast_borzna": LocalityPreset(
            id="chernihiv_oblast_borzna", patterns=(r"\bборзн(а|и|ої|у|ою|і)\b",)
        ),
        "chernihiv_oblast_chernihiv": LocalityPreset(
            id="chernihiv_oblast_chernihiv",
            patterns=(r"\bчерніг(ів|ова|ову|овом|ові)\b",),
        ),
        "chernihiv_oblast_desna": LocalityPreset(
            id="chernihiv_oblast_desna", patterns=(r"\bдесн(у|и|і)\b",)
        ),
        "chernihiv_oblast_honcharivske": LocalityPreset(
            id="chernihiv_oblast_honcharivske",
            patterns=(r"\bгончарівськ(е|ого|ому|им|ім)\b",),
        ),
        "chernihiv_oblast_horodnia": LocalityPreset(
            id="chernihiv_oblast_horodnia", patterns=(r"\bгородн(я|і|ю|ею)\b",)
        ),
        "chernihiv_oblast_ichnia": LocalityPreset(
            id="chernihiv_oblast_ichnia", patterns=(r"\bічн(я|і|ю|ею)\b",)
        ),
        "chernihiv_oblast_kholmy": LocalityPreset(
            id="chernihiv_oblast_kholmy", patterns=(r"\bхолм(и|ів|ам|ами|ах)\b",)
        ),
        "chernihiv_oblast_kipti": LocalityPreset(
            id="chernihiv_oblast_kipti", patterns=(r"\bкіпт(і|ів|ями)\b",)
        ),
        "chernihiv_oblast_koriukivka": LocalityPreset(
            id="chernihiv_oblast_koriukivka",
            patterns=(r"\bкорюківк(а|и|у|ою|і)\b",),
        ),
        "chernihiv_oblast_kozelets": LocalityPreset(
            id="chernihiv_oblast_kozelets",
            patterns=(r"\b(козелець|козельц(я|ю|ем|і))\b",),
        ),
        "chernihiv_oblast_lebedyn": LocalityPreset(
            id="chernihiv_oblast_lebedyn", patterns=(r"\bлебедин\b",)
        ),
        "chernihiv_oblast_liubech": LocalityPreset(
            id="chernihiv_oblast_liubech", patterns=(r"\bлюбеч(а|у|ем|і)?\b",)
        ),
        "chernihiv_oblast_mena": LocalityPreset(
            id="chernihiv_oblast_mena", patterns=(r"\bмен(а|и|у|і|ою)\b",)
        ),
        "chernihiv_oblast_nizhyn": LocalityPreset(
            id="chernihiv_oblast_nizhyn", patterns=(r"\bніжин(а|у|ом|і)?\b",)
        ),
        "chernihiv_oblast_novhorod_siverskyy": LocalityPreset(
            id="chernihiv_oblast_novhorod_siverskyy",
            patterns=(r"\bновгород-сіверськ(ий|ого|ому|им|ім)\b",),
        ),
        "chernihiv_oblast_olyshivka": LocalityPreset(
            id="chernihiv_oblast_olyshivka", patterns=(r"\bолишівк(а|и|у|ою|і)\b",)
        ),
        "chernihiv_oblast_oster": LocalityPreset(
            id="chernihiv_oblast_oster", patterns=(r"\bостер(а|у|ом|і)?\b",)
        ),
        "chernihiv_oblast_peremoha": LocalityPreset(
            id="chernihiv_oblast_peremoha", patterns=(r"\bперемог(у|и)\b",)
        ),
        "chernihiv_oblast_pryluky": LocalityPreset(
            id="chernihiv_oblast_pryluky",
            patterns=(r"\bприлук(и|ів|ами)?\b",),
        ),
        "chernihiv_oblast_ripky": LocalityPreset(
            id="chernihiv_oblast_ripky", patterns=(r"\bріп(ки|ок|кам|ками|ках)\b",)
        ),
        "chernihiv_oblast_snovsk": LocalityPreset(
            id="chernihiv_oblast_snovsk", patterns=(r"\bсновськ(а|у|ом|і)?\b",)
        ),
        "chernihiv_oblast_sosnytsia": LocalityPreset(
            id="chernihiv_oblast_sosnytsia", patterns=(r"\bсосниц(я|і|ю|ею)\b",)
        ),
    },
)
