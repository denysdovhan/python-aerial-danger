"""Location presets for volyn oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

VOLYN_OBLAST_REGION: Final = RegionPreset(
    id="volyn_oblast",
    patterns=(
        r"\bволин(ь|і|ню)\b",
        r"\bволинськ(а|ої|ій|у|ою) област(ь|і|ю)\b",
    ),
    localities={
        "volyn_oblast_kolky": LocalityPreset(
            id="volyn_oblast_kolky",
            patterns=(r"\bкол(ки|ок|кам|ками|ках)\b",),
        ),
        "volyn_oblast_kovel": LocalityPreset(
            id="volyn_oblast_kovel",
            patterns=(r"\bковел(ь|я|ю|ем|і)\b",),
        ),
        "volyn_oblast_liubeshiv": LocalityPreset(
            id="volyn_oblast_liubeshiv",
            patterns=(r"\bлюбеш(ів|ова|ову|овом|ові)\b",),
        ),
        "volyn_oblast_lutsk": LocalityPreset(
            id="volyn_oblast_lutsk", patterns=(r"\bлуцьк(а|у|ом|ові)?\b",)
        ),
        "volyn_oblast_tsuman": LocalityPreset(
            id="volyn_oblast_tsuman",
            patterns=(r"\bцуман(ь|і|ню)\b",),
        ),
        "volyn_oblast_volodymyr": LocalityPreset(
            id="volyn_oblast_volodymyr",
            patterns=(r"\b(на|від|повз|через|до|біля)\s+володимир(а|у|ом|і)?\b",),
        ),
    },
)
