"""Location presets for dnipropetrovsk oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

DNIPROPETROVSK_OBLAST_REGION: Final = RegionPreset(
    id="dnipropetrovsk_oblast",
    patterns=(
        r"\bдніпропетровщин(а|и|і|у|ою)\b",
        r"\bдніпропетровськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
    ),
    localities={
        "dnipropetrovsk_oblast_apostolove": LocalityPreset(
            id="dnipropetrovsk_oblast_apostolove",
            patterns=(r"\bапостолов(е|ого|ому|им|ім)\b",),
        ),
        "dnipropetrovsk_oblast_dnipro": LocalityPreset(
            id="dnipropetrovsk_oblast_dnipro", patterns=(r"\bдніпр(о|а|у|і|ом)\b",)
        ),
        "dnipropetrovsk_oblast_hirnytske": LocalityPreset(
            id="dnipropetrovsk_oblast_hirnytske", patterns=(r"\bгірницьке\b",)
        ),
        "dnipropetrovsk_oblast_kamianske": LocalityPreset(
            id="dnipropetrovsk_oblast_kamianske",
            patterns=(r"\bкам['’ʼ]?янськ(е|ого|ому|им|ім)\b",),
        ),
        "dnipropetrovsk_oblast_kryvyi_rih": LocalityPreset(
            id="dnipropetrovsk_oblast_kryvyi_rih",
            patterns=(r"\bкрив(ий|ого|ому|им) р(іг|огу|озі|огом)\b",),
        ),
        "dnipropetrovsk_oblast_nikopol": LocalityPreset(
            id="dnipropetrovsk_oblast_nikopol",
            patterns=(r"\bнікопол(ь|я|ем)\b",),
        ),
        "dnipropetrovsk_oblast_pavlohrad": LocalityPreset(
            id="dnipropetrovsk_oblast_pavlohrad",
            patterns=(r"\bпавлоград(а|у|і|ом)?\b",),
        ),
        "dnipropetrovsk_oblast_pereshchepyne": LocalityPreset(
            id="dnipropetrovsk_oblast_pereshchepyne",
            patterns=(r"\bперещепин(е|ого|ому|им|ім)\b",),
        ),
        "dnipropetrovsk_oblast_samar": LocalityPreset(
            id="dnipropetrovsk_oblast_samar", patterns=(r"\bсамар(а|у|ом|і)?\b",)
        ),
        "dnipropetrovsk_oblast_shakhtarske": LocalityPreset(
            id="dnipropetrovsk_oblast_shakhtarske",
            patterns=(r"\bшахтарське\b",),
        ),
        "dnipropetrovsk_oblast_solone": LocalityPreset(
            id="dnipropetrovsk_oblast_solone", patterns=(r"\bсолоне\b",)
        ),
        "dnipropetrovsk_oblast_synelnykove": LocalityPreset(
            id="dnipropetrovsk_oblast_synelnykove",
            patterns=(r"\bсинельник(ове|ового|ова)\b",),
        ),
        "dnipropetrovsk_oblast_vasylkivka": LocalityPreset(
            id="dnipropetrovsk_oblast_vasylkivka",
            patterns=(r"\bвасильківк(а|и|у|ою|і)\b",),
        ),
    },
)
