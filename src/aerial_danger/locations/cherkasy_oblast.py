"""Location presets for cherkasy oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

CHERKASY_OBLAST_REGION: Final = RegionPreset(
    id="cherkasy_oblast",
    patterns=(
        r"\bчеркащин(а|и|і|у|ою)\b",
        r"\bчеркаськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
    ),
    localities={
        "cherkasy_oblast_cherkasy": LocalityPreset(
            id="cherkasy_oblast_cherkasy", patterns=(r"\bчеркас(и|ам|ами|ах)?\b",)
        ),
        "cherkasy_oblast_drabiv": LocalityPreset(
            id="cherkasy_oblast_drabiv",
            patterns=(r"\bдраб(ів|ова|ову|овом|ові)\b",),
        ),
        "cherkasy_oblast_kaniv": LocalityPreset(
            id="cherkasy_oblast_kaniv", patterns=(r"\bкан(ів|ева|еву|евом|еві)\b",)
        ),
        "cherkasy_oblast_smila": LocalityPreset(
            id="cherkasy_oblast_smila", patterns=(r"\bсміл(а|и|у|ою)\b",)
        ),
        "cherkasy_oblast_uman": LocalityPreset(
            id="cherkasy_oblast_uman", patterns=(r"\bуман(ь|і|ню|нею)\b",)
        ),
        "cherkasy_oblast_zolotonosha": LocalityPreset(
            id="cherkasy_oblast_zolotonosha", patterns=(r"\bзолотонош(а|і|у|ею)\b",)
        ),
    },
)
