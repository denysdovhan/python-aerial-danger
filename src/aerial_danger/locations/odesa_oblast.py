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
        "odesa_oblast_altestove": LocalityPreset(
            id="odesa_oblast_altestove",
            patterns=(r"\bалтестов(е|ого|ому|им|ім)\b",),
        ),
        "odesa_oblast_ananiv": LocalityPreset(
            id="odesa_oblast_ananiv",
            patterns=(r"\bанань(їв|єва|єву|євом|єві)\b",),
        ),
        "odesa_oblast_arkadiia": LocalityPreset(
            id="odesa_oblast_arkadiia", patterns=(r"\bаркаді(я|ї|ю|єю)\b",)
        ),
        "odesa_oblast_artsyz": LocalityPreset(
            id="odesa_oblast_artsyz",
            patterns=(r"\bарциз(а|у|ом|і)?\b",),
        ),
        "odesa_oblast_avanhard": LocalityPreset(
            id="odesa_oblast_avanhard",
            patterns=(r"\bавангард(а|у|ом|і)?\b",),
        ),
        "odesa_oblast_balta": LocalityPreset(
            id="odesa_oblast_balta",
            patterns=(r"\bбалт(а|и|і|у|ою)\b",),
        ),
        "odesa_oblast_baraboi": LocalityPreset(
            id="odesa_oblast_baraboi",
            patterns=(r"\bбарабо(й|я|ю|єм|ї)\b",),
        ),
        "odesa_oblast_berezivka": LocalityPreset(
            id="odesa_oblast_berezivka",
            patterns=(r"\bберезів(ка|ки|ці|ку|кою)\b",),
        ),
        "odesa_oblast_bilhorod_dnistrovskyi": LocalityPreset(
            id="odesa_oblast_bilhorod_dnistrovskyi",
            patterns=(r"\bбілгород[ -]дністровськ(ий|ого|ому|им|ім)\b",),
        ),
        "odesa_oblast_biliaivka": LocalityPreset(
            id="odesa_oblast_biliaivka",
            patterns=(r"\bбіляїв(ка|ки|ці|ку|кою)\b",),
        ),
        "odesa_oblast_biliari": LocalityPreset(
            id="odesa_oblast_biliari",
            patterns=(r"\bбіляр(і|ів|ям|ями|ях)\b",),
        ),
        "odesa_oblast_bolhrad": LocalityPreset(
            id="odesa_oblast_bolhrad",
            patterns=(r"\bболград(а|у|ом|і)?\b",),
        ),
        "odesa_oblast_buialyk": LocalityPreset(
            id="odesa_oblast_buialyk",
            patterns=(r"\bбуялик(а|у|ом|і)?\b",),
        ),
        "odesa_oblast_chornomorsk": LocalityPreset(
            id="odesa_oblast_chornomorsk", patterns=(r"\bчорноморськ(а|у|ом|і)?\b",)
        ),
        "odesa_oblast_chornomorske": LocalityPreset(
            id="odesa_oblast_chornomorske", patterns=(r"\bчорноморське\b",)
        ),
        "odesa_oblast_dachne": LocalityPreset(
            id="odesa_oblast_dachne",
            patterns=(r"\bдачн(е|ого|ому|им|ім)\b",),
        ),
        "odesa_oblast_dalnyk": LocalityPreset(
            id="odesa_oblast_dalnyk",
            patterns=(r"\bдальник(а|у|ом|і)?\b",),
        ),
        "odesa_oblast_dobroslav": LocalityPreset(
            id="odesa_oblast_dobroslav", patterns=(r"\bдоброслав(а|у|ом|і)?\b",)
        ),
        "odesa_oblast_fontanka": LocalityPreset(
            id="odesa_oblast_fontanka",
            patterns=(r"\bфонтан(ка|ки|ці|ку|кою)\b",),
        ),
        "odesa_oblast_hrybivka": LocalityPreset(
            id="odesa_oblast_hrybivka",
            patterns=(r"\bгрибів(ка|ки|ці|ку|кою)\b",),
        ),
        "odesa_oblast_hryhorivka": LocalityPreset(
            id="odesa_oblast_hryhorivka",
            patterns=(r"\bгригорів(ка|ки|ці|ку|кою)\b",),
        ),
        "odesa_oblast_ilichanka": LocalityPreset(
            id="odesa_oblast_ilichanka",
            patterns=(r"\bілічан(ка|ки|ці|ку|кою)\b",),
        ),
        "odesa_oblast_ivanivka": LocalityPreset(
            id="odesa_oblast_ivanivka",
            patterns=(r"\bіванів(ка|ки|ці|ку|кою)\b",),
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
        "odesa_oblast_kiliia": LocalityPreset(
            id="odesa_oblast_kiliia",
            patterns=(r"\bкілі(я|ї|ю|єю)\b",),
        ),
        "odesa_oblast_kosa": LocalityPreset(
            id="odesa_oblast_kosa", patterns=(r"\bкос(у|ою)\b",)
        ),
        "odesa_oblast_kosy": LocalityPreset(
            id="odesa_oblast_kosy", patterns=(r"\bкоси\b",)
        ),
        "odesa_oblast_krasnosilka": LocalityPreset(
            id="odesa_oblast_krasnosilka",
            patterns=(r"\bкрасносіл(ка|ки|ці|ку|кою)\b",),
        ),
        "odesa_oblast_kurisove": LocalityPreset(
            id="odesa_oblast_kurisove",
            patterns=(r"\bкурісов(е|ого|ому|им|ім)\b",),
        ),
        "odesa_oblast_kurortne": LocalityPreset(
            id="odesa_oblast_kurortne",
            patterns=(r"\bкурортн(е|ого|ому|им|ім)\b",),
        ),
        "odesa_oblast_liubashivka": LocalityPreset(
            id="odesa_oblast_liubashivka",
            patterns=(r"\bлюбашів(ка|ки|ці|ку|кою)\b",),
        ),
        "odesa_oblast_lyman": LocalityPreset(
            id="odesa_oblast_lyman",
            patterns=(r"\bлиман(а|у|ом|і)?\b",),
        ),
        "odesa_oblast_lymanka": LocalityPreset(
            id="odesa_oblast_lymanka",
            patterns=(r"\bлиман(ка|ки|ці|ку|кою)\b",),
        ),
        "odesa_oblast_malodolynske": LocalityPreset(
            id="odesa_oblast_malodolynske",
            patterns=(r"\bмалодолинськ(е|ого|ому|им|ім)\b",),
        ),
        "odesa_oblast_malyi_fontan": LocalityPreset(
            id="odesa_oblast_malyi_fontan",
            patterns=(r"\bмал(ий|ого|ому|им|ім)\s+фонтан(а|у|ом|і)?\b",),
        ),
        "odesa_oblast_mayaky": LocalityPreset(
            id="odesa_oblast_mayaky", patterns=(r"\bмаяки\b",)
        ),
        "odesa_oblast_moldovanka": LocalityPreset(
            id="odesa_oblast_moldovanka",
            patterns=(r"\bмолдован(ка|ки|ці|ку|кою)\b",),
        ),
        "odesa_oblast_nadlymanske": LocalityPreset(
            id="odesa_oblast_nadlymanske",
            patterns=(r"\bнадлиманськ(е|ого|ому|им|ім)\b",),
        ),
        "odesa_oblast_nova_dolyna": LocalityPreset(
            id="odesa_oblast_nova_dolyna",
            patterns=(r"\bнов(а|ої|ій|у|ою)\s+долин(а|и|і|у|ою)\b",),
        ),
        "odesa_oblast_novi_biliari": LocalityPreset(
            id="odesa_oblast_novi_biliari",
            patterns=(r"\bнов(і|их|им|ими)\s+біляр(і|ів|ям|ями|ях)\b",),
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
        "odesa_oblast_oleksandrivka": LocalityPreset(
            id="odesa_oblast_oleksandrivka",
            patterns=(r"\bолександрів(ка|ки|ці|ку|кою)\b",),
        ),
        "odesa_oblast_orlivka": LocalityPreset(
            id="odesa_oblast_orlivka",
            patterns=(r"\bорлів(ка|ки|ці|ку|кою)\b",),
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
        "odesa_oblast_podilsk": LocalityPreset(
            id="odesa_oblast_podilsk",
            patterns=(r"\bподільськ(а|у|ом|і)?\b",),
        ),
        "odesa_oblast_prylymanske": LocalityPreset(
            id="odesa_oblast_prylymanske",
            patterns=(r"\bприлиманськ(е|ого|ому|им|ім)\b",),
        ),
        "odesa_oblast_prymorske": LocalityPreset(
            id="odesa_oblast_prymorske",
            patterns=(r"\bприморськ(е|ого|ому|им|ім)\b",),
        ),
        "odesa_oblast_reni": LocalityPreset(
            id="odesa_oblast_reni", patterns=(r"\bрен(і|ях|ями)\b",)
        ),
        "odesa_oblast_rozdilna": LocalityPreset(
            id="odesa_oblast_rozdilna",
            patterns=(r"\bроздільн(а|ої|ій|у|ою)\b",),
        ),
        "odesa_oblast_sanzhiika": LocalityPreset(
            id="odesa_oblast_sanzhiika",
            patterns=(r"\bсанжій(ка|ки|ці|ку|кою)\b",),
        ),
        "odesa_oblast_sarata": LocalityPreset(
            id="odesa_oblast_sarata",
            patterns=(r"\bсарат(а|и|і|у|ою)\b",),
        ),
        "odesa_oblast_shabo": LocalityPreset(
            id="odesa_oblast_shabo",
            patterns=(r"\bшабо\b",),
        ),
        "odesa_oblast_shyriaieve": LocalityPreset(
            id="odesa_oblast_shyriaieve",
            patterns=(r"\bширяєв(е|ого|ому|им|ім)\b",),
        ),
        "odesa_oblast_starokozache": LocalityPreset(
            id="odesa_oblast_starokozache",
            patterns=(r"\bстарокозач(е|ого|ому|им|ім)\b",),
        ),
        "odesa_oblast_sukhyi_lyman": LocalityPreset(
            id="odesa_oblast_sukhyi_lyman",
            patterns=(r"\bсух(ий|ого|ому|им|ім)\s+лиман(а|у|ом|і)?\b",),
        ),
        "odesa_oblast_tairove": LocalityPreset(
            id="odesa_oblast_tairove",
            patterns=(r"\bтаїров(е|ого|ому|им|ім)\b",),
        ),
        "odesa_oblast_tatarbunary": LocalityPreset(
            id="odesa_oblast_tatarbunary",
            patterns=(r"\bтатарбунар(и|ів|ам|ами|ах)\b",),
        ),
        "odesa_oblast_teplodar": LocalityPreset(
            id="odesa_oblast_teplodar",
            patterns=(r"\bтеплодар(а|у|ом|і)?\b",),
        ),
        "odesa_oblast_tuzly": LocalityPreset(
            id="odesa_oblast_tuzly", patterns=(r"\bтузли\b",)
        ),
        "odesa_oblast_usatove": LocalityPreset(
            id="odesa_oblast_usatove",
            patterns=(r"\bусатов(е|ого|ому|им|ім)\b",),
        ),
        "odesa_oblast_velykodolynske": LocalityPreset(
            id="odesa_oblast_velykodolynske",
            patterns=(r"\bвеликодолинськ(е|ого|ому|им|ім)\b",),
        ),
        "odesa_oblast_velykyi_dalnyk": LocalityPreset(
            id="odesa_oblast_velykyi_dalnyk",
            patterns=(r"\bвелик(ий|ого|ому|им|ім)\s+дальник(а|у|ом|і)?\b",),
        ),
        "odesa_oblast_vylkove": LocalityPreset(
            id="odesa_oblast_vylkove", patterns=(r"\bвилков(е|ого|ому|им|ім)\b",)
        ),
        "odesa_oblast_zatoka": LocalityPreset(
            id="odesa_oblast_zatoka", patterns=(r"\bзаток(а|и|у|ою|ці)\b",)
        ),
    },
)
