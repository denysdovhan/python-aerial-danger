"""Location presets for khmelnytskyi oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

KHMELNYTSKYI_OBLAST_REGION: Final = RegionPreset(
    id="khmelnytskyi_oblast",
    patterns=(
        r"\bхмельниччин(а|и|і|у|ою)\b",
        r"\bхмельницьк(а|ої|ій|у|ою) област(ь|і|ю)\b",
    ),
    localities={
        "khmelnytskyi_oblast_khmelnytskyi": LocalityPreset(
            id="khmelnytskyi_oblast_khmelnytskyi",
            patterns=(r"\bхмельницьк(ий|ого|ому|им|ім)\b",),
        ),
        "khmelnytskyi_oblast_starokostiantyniv": LocalityPreset(
            id="khmelnytskyi_oblast_starokostiantyniv",
            patterns=(
                r"\bстарокостянтин(ів|ова|ову|овом|ові)\b",
                r"\bстаркон(у|а)?\b",
            ),
        ),
    },
)
