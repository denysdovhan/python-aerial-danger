"""Location presets for poltava oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

POLTAVA_OBLAST_REGION: Final = RegionPreset(
    id="poltava_oblast",
    patterns=(
        r"\bполтавщин(а|и|і|у|ою)\b",
        r"\bполтавськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
    ),
    localities={
        "poltava_oblast_dykanka": LocalityPreset(
            id="poltava_oblast_dykanka", patterns=(r"\bдиканьк(а|и|у|ою|і)\b",)
        ),
        "poltava_oblast_hadiach": LocalityPreset(
            id="poltava_oblast_hadiach", patterns=(r"\bгадяч(а)?\b",)
        ),
        "poltava_oblast_hlobyne": LocalityPreset(
            id="poltava_oblast_hlobyne", patterns=(r"\bглобин(е|ого|ому|им|ім)\b",)
        ),
        "poltava_oblast_hrebinka": LocalityPreset(
            id="poltava_oblast_hrebinka", patterns=(r"\bгребінк(а|и|у|ою|і)\b",)
        ),
        "poltava_oblast_kobeliaky": LocalityPreset(
            id="poltava_oblast_kobeliaky",
            patterns=(r"\bкобеляк(и|ів|ам|ами|ах)\b",),
        ),
        "poltava_oblast_kotelva": LocalityPreset(
            id="poltava_oblast_kotelva", patterns=(r"\bкотельв(а|и|у|ою|і)\b",)
        ),
        "poltava_oblast_kremenchuk": LocalityPreset(
            id="poltava_oblast_kremenchuk",
            patterns=(r"\bкременч(ук|ука|уку|уком|уці)\b",),
        ),
        "poltava_oblast_lubny": LocalityPreset(
            id="poltava_oblast_lubny", patterns=(r"\bлуб(ни|ен|нів|ням|нями|нях)\b",)
        ),
        "poltava_oblast_myrhorod": LocalityPreset(
            id="poltava_oblast_myrhorod", patterns=(r"\bмиргород(а|у|ом|і)?\b",)
        ),
        "poltava_oblast_novi_sanzhary": LocalityPreset(
            id="poltava_oblast_novi_sanzhary",
            patterns=(r"\bнов(і|их|им|ими) санжар(и|ів|ам|ами|ах)\b",),
        ),
        "poltava_oblast_poltava": LocalityPreset(
            id="poltava_oblast_poltava", patterns=(r"\bполтав(а|и|і|у|ою)\b",)
        ),
        "poltava_oblast_pyriatyn": LocalityPreset(
            id="poltava_oblast_pyriatyn", patterns=(r"\bпирятин(а)?\b",)
        ),
        "poltava_oblast_reshetylivka": LocalityPreset(
            id="poltava_oblast_reshetylivka",
            patterns=(r"\bрешетилівк(а|и|у|ою|і)\b",),
        ),
        "poltava_oblast_shyshaky": LocalityPreset(
            id="poltava_oblast_shyshaky", patterns=(r"\bшишак(и|ів|ам|ами|ах)\b",)
        ),
        "poltava_oblast_velyki_sorochyntsi": LocalityPreset(
            id="poltava_oblast_velyki_sorochyntsi",
            patterns=(r"\bвелик(і|их|им|ими) сорочинц(і|ів|ям|ями|ях)\b",),
        ),
        "poltava_oblast_zinkiv": LocalityPreset(
            id="poltava_oblast_zinkiv", patterns=(r"\bзіньків\b",)
        ),
    },
)
