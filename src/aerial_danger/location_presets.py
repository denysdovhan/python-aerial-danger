"""Area pattern presets for Aerial Danger."""

import json
from importlib.resources import files
from typing import Final

from .models import LocalityPreset, RegionPreset

__all__ = ["LOCATION_PRESETS", "LocalityPreset", "RegionPreset"]


def _load_presets() -> dict[str, RegionPreset]:
    presets = {}
    for resource in sorted(
        files("aerial_danger.locations").iterdir(), key=lambda resource: resource.name
    ):
        if not resource.name.endswith(".json"):
            continue
        data = json.loads(resource.read_text(encoding="utf-8"))
        region = RegionPreset(
            id=data["id"],
            names=data["names"],
            patterns=tuple(data["patterns"]),
            localities={
                locality_id: LocalityPreset(
                    id=locality_id,
                    names=locality["names"],
                    patterns=tuple(locality["patterns"]),
                )
                for locality_id, locality in data["localities"].items()
            },
        )
        presets[region.id] = region
    return presets


LOCATION_PRESETS: Final = _load_presets()
