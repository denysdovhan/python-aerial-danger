"""Check the installed package without importing from the source tree."""

# ruff: noqa: S101

from aerial_danger import DangerDetector, DangerType, Detection, PatternMatch
from aerial_danger.location_presets import LOCATION_PRESETS

detector = DangerDetector(regions=[r"\bкиїв\b"], localities=[])
result = detector.danger("КИЇВ ШВИДКІСНА!")
assert isinstance(result, Detection)
assert result.danger
assert result.type == DangerType.BALLISTIC
assert result.matched_area == "КИЇВ"
assert PatternMatch("КИЇВ", r"\bкиїв\b").text == result.matched_area
assert LOCATION_PRESETS["kyiv"].patterns
assert not detector.danger("Привіт").danger
