"""Location presets for sumy oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

SUMY_OBLAST_REGION: Final = RegionPreset(
    id="sumy_oblast",
    patterns=(
        r"\bсумщин(а|и|і|у|ою)\b",
        r"\bсумськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
    ),
    localities={
        "sumy_oblast_bilopillia": LocalityPreset(
            id="sumy_oblast_bilopillia", patterns=(r"\bбілопілля\b",)
        ),
        "sumy_oblast_boromlia": LocalityPreset(
            id="sumy_oblast_boromlia", patterns=(r"\bборомл(я|і|ю|ею)\b",)
        ),
        "sumy_oblast_buryn": LocalityPreset(
            id="sumy_oblast_buryn", patterns=(r"\bбурин(ь|і|ню)\b",)
        ),
        "sumy_oblast_duboviazivka": LocalityPreset(
            id="sumy_oblast_duboviazivka",
            patterns=(r"\bдубов'язівк(а|и|у|ою|і)\b",),
        ),
        "sumy_oblast_hlukhiv": LocalityPreset(
            id="sumy_oblast_hlukhiv", patterns=(r"\bглухів\b",)
        ),
        "sumy_oblast_kharkivshchyna": LocalityPreset(
            id="sumy_oblast_kharkivshchyna",
            patterns=(r"\bхарківщин(а|у|і|и|ою)\b",),
        ),
        "sumy_oblast_khotin": LocalityPreset(
            id="sumy_oblast_khotin", patterns=(r"\bхот(інь|іня|іні|іню|інею)\b",)
        ),
        "sumy_oblast_konotop": LocalityPreset(
            id="sumy_oblast_konotop",
            patterns=(r"\bконотоп(а|ом|у)?\b",),
        ),
        "sumy_oblast_krolevets": LocalityPreset(
            id="sumy_oblast_krolevets",
            patterns=(r"\bкрол(евець|евця|евцю|евцем|евці)\b",),
        ),
        "sumy_oblast_kyrykivka": LocalityPreset(
            id="sumy_oblast_kyrykivka", patterns=(r"\bкириківк(а|и|у|ою|і)\b",)
        ),
        "sumy_oblast_lebedyn": LocalityPreset(
            id="sumy_oblast_lebedyn", patterns=(r"\bлебедин\b",)
        ),
        "sumy_oblast_nedryhailiv": LocalityPreset(
            id="sumy_oblast_nedryhailiv", patterns=(r"\bнедригайлів(а|у|ом|і)?\b",)
        ),
        "sumy_oblast_okhtyrka": LocalityPreset(
            id="sumy_oblast_okhtyrka", patterns=(r"\bохтирк(а|и|у|ою|і)\b",)
        ),
        "sumy_oblast_putivl": LocalityPreset(
            id="sumy_oblast_putivl", patterns=(r"\bпутивл(ь|я|ю|ем|і)\b",)
        ),
        "sumy_oblast_romny": LocalityPreset(
            id="sumy_oblast_romny", patterns=(r"\bром(ни|ен|нів|нам|нами|нах)\b",)
        ),
        "sumy_oblast_shostka": LocalityPreset(
            id="sumy_oblast_shostka", patterns=(r"\bшостк(а|и|у|ою|і)\b",)
        ),
        "sumy_oblast_sumy": LocalityPreset(
            id="sumy_oblast_sumy", patterns=(r"\bсум(и|ах|ами)?\b",)
        ),
        "sumy_oblast_terny": LocalityPreset(
            id="sumy_oblast_terny", patterns=(r"\bтерни\b",)
        ),
        "sumy_oblast_trostianets": LocalityPreset(
            id="sumy_oblast_trostianets", patterns=(r"\bтростянець\b",)
        ),
    },
)
