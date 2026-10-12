"""Location presets for odesa oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

ODESA_OBLAST_REGION: Final = RegionPreset(
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
        "odesa_oblast_chornomorske": LocalityPreset(
            id="odesa_oblast_chornomorske", patterns=(r"\bчорноморське\b",)
        ),
        "odesa_oblast_dobroslav": LocalityPreset(
            id="odesa_oblast_dobroslav", patterns=(r"\bдоброслав(а|у|ом|і)?\b",)
        ),
        "odesa_oblast_izmail": LocalityPreset(
            id="odesa_oblast_izmail", patterns=(r"\bізмаїл(а|у|ом|і)?\b",)
        ),
        "odesa_oblast_karolino_buhaz": LocalityPreset(
            id="odesa_oblast_karolino_buhaz",
            patterns=(r"\bкароліно[ -]бугаз(у|і|ом|а)?\b",),
        ),
        "odesa_oblast_katlabuh": LocalityPreset(
            id="odesa_oblast_katlabuh", patterns=(r"\bкатлабуг(а|у|ом|і)?\b",)
        ),
        "odesa_oblast_khadzhybeiskyi_raion": LocalityPreset(
            id="odesa_oblast_khadzhybeiskyi_raion",
            patterns=(r"\bхаджибейськ(ий|ого|ому|им|ім) район(у|і|ом)?\b",),
        ),
        "odesa_oblast_kosa": LocalityPreset(
            id="odesa_oblast_kosa", patterns=(r"\bкос(у|ою)\b",)
        ),
        "odesa_oblast_kosy": LocalityPreset(
            id="odesa_oblast_kosy", patterns=(r"\bкоси\b",)
        ),
        "odesa_oblast_mayaky": LocalityPreset(
            id="odesa_oblast_mayaky", patterns=(r"\bмаяки\b",)
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
        "odesa_oblast_pivdenne": LocalityPreset(
            id="odesa_oblast_pivdenne", patterns=(r"\bпівденне\b",)
        ),
        "odesa_oblast_reni": LocalityPreset(
            id="odesa_oblast_reni", patterns=(r"\bрен(і|ях|ями)\b",)
        ),
        "odesa_oblast_tatarbunary": LocalityPreset(
            id="odesa_oblast_tatarbunary",
            patterns=(r"\bтатарбунар(и|ів|ам|ами|ах)\b",),
        ),
        "odesa_oblast_tuzly": LocalityPreset(
            id="odesa_oblast_tuzly", patterns=(r"\bтузли\b",)
        ),
        "odesa_oblast_vylkove": LocalityPreset(
            id="odesa_oblast_vylkove", patterns=(r"\bвилков(е|ого|ому|им|ім)\b",)
        ),
        "odesa_oblast_zatoka": LocalityPreset(
            id="odesa_oblast_zatoka", patterns=(r"\bзаток(а|и|у|ою|ці)\b",)
        ),
    },
)
