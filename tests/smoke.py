"""Check the installed package without importing from the source tree."""

# ruff: noqa: S101

from aerial_danger import (
    DangerDetector,
    DangerType,
    Detection,
    DetectionStatus,
    PatternMatch,
)
from aerial_danger.location_presets import LOCATION_PRESETS
from aerial_danger.pattern_utils import (
    resolve_locality_patterns,
    resolve_region_patterns,
)

detector = DangerDetector(regions=[r"\bкиїв\b"], localities=[])
result = detector.danger("КИЇВ ШВИДКІСНА!")
assert isinstance(result, Detection)
assert result.danger
assert result.status is DetectionStatus.DANGER
assert result.type == DangerType.BALLISTIC
assert result.matched_area == "КИЇВ"
assert PatternMatch("КИЇВ", r"\bкиїв\b").text == result.matched_area
assert LOCATION_PRESETS["kyiv"].patterns
assert LOCATION_PRESETS["kyiv"].localities["kyiv_nyvky"].names == {
    "uk": "Нивки",
    "en": "Nyvky",
}
assert not detector.danger("Привіт").danger

preset_detector = DangerDetector(
    regions=resolve_region_patterns([], ["kyiv"]),
    localities=resolve_locality_patterns([], ["kyiv"], ["kyiv_nyvky"]),
)
assert preset_detector.drone_danger("Шахед на Нивки!").danger
assert detector.danger("Привіт").status is DetectionStatus.IGNORED
assert detector.danger("Все тихо").status is DetectionStatus.SAFE
