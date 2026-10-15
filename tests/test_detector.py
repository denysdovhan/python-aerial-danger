"""Tests for common danger detector behavior."""

# ruff: noqa: S101

import re

import pytest

from aerial_danger import (
    DangerDetector,
    DangerType,
    Detection,
    DetectionStatus,
    PatternMatch,
)
from aerial_danger.location_presets import LOCATION_PRESETS

from .common import LOCALITY_PATTERNS, REGION_PATTERNS

NO_MATCH_CASES: list[str] = [
    "🛵Шахед на Мену.",
    "🛵7 Шахедів з моря на Татарбунари.",
    "🛵Залишився 1 Шахед на півночі Київщині, летить в напрямку Чорнобиля!",
    "🚀Візуалізації напрямку польоту крилатої ракети.",
    "🟡 Дорозвідка по Кинджалах, локаційно чисто.",
    "🔴🚛 Загроза балістики з Воронезької області!",
    "БпЛА невстановленого типу над Обухівським р-ном Київщини.",
    "💥Удар балістикою по Дніпру.",
    "⚠️ 2х БпЛА сектор Павлоград, дніпропетровської області.",
    "‼️Одеса — спуск балістики!",
    "По Києву били Іскандер-М та Циркони.",
    "Під час нічної атаки по Києву росія випустила дві ракети «Циркон»/«Онікс».",
    "На жаль, цієї ночі над Києвом не вдалося збити жодної ракети «Циркон».",
    "Удар Цирконами по Києву відбувся вночі.",
    "Вночі було зафіксовано пуск ракети «Циркон» по Києву.",
]


def test_validate_patterns() -> None:
    """Configured patterns compile independently from the detector."""
    DangerDetector.validate_patterns(REGION_PATTERNS, LOCALITY_PATTERNS)

    with pytest.raises(re.error):
        DangerDetector.validate_patterns(["("])


def test_detection_includes_exact_matches_and_patterns() -> None:
    """A detection should preserve exact text and matching regex patterns."""
    area_pattern = r"\bкиїв\b"
    detector = DangerDetector([area_pattern], [])

    detection = detector.danger("КИЇВ ШВИДКІСНА!")

    assert detection.matched_area == "КИЇВ"
    assert detection.status is DetectionStatus.DANGER
    assert detection.matched_danger == "КИЇВ ШВИДКІСНА"
    assert detection.area_pattern == area_pattern
    assert detection.danger_pattern == rf"{area_pattern} швидкісна"


def test_match_helpers_return_pattern_matches() -> None:
    """Match helpers should return named text and pattern fields."""
    area_pattern = r"\bкиїв\b"
    danger_pattern = rf"{area_pattern} швидкісна"
    message = "КИЇВ ШВИДКІСНА!"
    detector = DangerDetector([area_pattern], [])

    assert detector.find_area(message, [area_pattern]) == PatternMatch(
        text="КИЇВ", pattern=area_pattern
    )
    assert detector.match_first(
        detector.compile_patterns([danger_pattern]), message
    ) == PatternMatch(text="КИЇВ ШВИДКІСНА", pattern=danger_pattern)


def test_named_area_patterns_compose_with_movement() -> None:
    """Custom named captures remain valid in region and locality templates."""
    pattern = r"\b(?P<place>Нивки)\b"
    for regions, localities, expected_type in (
        ([], [pattern], DangerType.DRONE),
        ([pattern], [], DangerType.GENERIC),
    ):
        detection = DangerDetector(regions, localities).danger("На Нивки йде")

        assert detection.type is expected_type
        assert detection.matched_area == "Нивки"
        assert detection.matched_danger == "На Нивки йде"


def test_non_matches() -> None:
    """Negative samples should not raise danger flags."""
    detector = DangerDetector(REGION_PATTERNS, LOCALITY_PATTERNS)
    for text in NO_MATCH_CASES:
        detection = detector.danger(text)
        assert detection.danger is False, text
        assert detection.type is None, text


def test_preset_prose_is_ignored() -> None:
    """Common-word locality collisions require actual alert wording."""
    cases = [
        (
            "kyiv_oblast_khotiv",
            "О той що на Житомирщину хотів йде в бік Фастова",
            None,
        ),
        ("kyiv_oblast_mriia", "мрії мрії", "мрії"),
    ]
    region = LOCATION_PRESETS["kyiv_oblast"]
    for locality_id, text, matched_area in cases:
        localities = region.localities[locality_id].patterns
        detector = DangerDetector([], localities)
        detection = detector.danger(text)
        area = detector.find_area(text, localities)

        assert (area.text if area else None) == matched_area, text
        assert detection.status is DetectionStatus.IGNORED, text
        assert detection.danger is False, text
        assert detection.type is None, text
        assert detector.is_safe(text) is False, text


def test_unrelated_message_is_ignored() -> None:
    """A non-match must not become an all-clear."""
    detector = DangerDetector(REGION_PATTERNS, LOCALITY_PATTERNS)

    assert detector.danger("Привіт").status is DetectionStatus.IGNORED


@pytest.mark.parametrize("danger", [True, False])
def test_detection_preserves_danger_constructor(*, danger: bool) -> None:
    """Existing keyword and positional construction retain the primary flag."""
    detection = Detection(danger=danger, message="КИЇВ ШВИДКІСНА!")
    assert detection.danger is danger
    assert detection == Detection(danger, "КИЇВ ШВИДКІСНА!")


def test_explicit_safe_status_preserves_negative_danger_flag() -> None:
    """Callers can distinguish an all-clear without a separate safe flag."""
    detection = Detection(danger=False, message="Все тихо", status=DetectionStatus.SAFE)
    assert detection.danger is False
    assert detection.status is DetectionStatus.SAFE
