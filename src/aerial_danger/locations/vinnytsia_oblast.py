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
        "vinnytsia_oblast_trostianets": LocalityPreset(
            id="vinnytsia_oblast_trostianets", patterns=(r"\bтростянець\b",)
        ),
        "vinnytsia_oblast_vapniarka": LocalityPreset(
            id="vinnytsia_oblast_vapniarka", patterns=(r"\bвапнярку\b",)
        ),
        "vinnytsia_oblast_vinnytsia": LocalityPreset(
            id="vinnytsia_oblast_vinnytsia", patterns=(r"\bвінниц(я|і|ю|ею)\b",)
        ),
        "vinnytsia_oblast_zhmerynka": LocalityPreset(
            id="vinnytsia_oblast_zhmerynka", patterns=(r"\bжмеринк(а|и|у)\b",)
        ),
    },
)
