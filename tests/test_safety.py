"""Tests for safety messages."""

# ruff: noqa: S101

import pytest

from aerial_danger import DangerDetector, DetectionStatus

from .common import REGION_PATTERNS

IGNORED_CASES: list[str] = [
    (
        "Маємо підготовку до пусків балістики. Планується залучення близько "
        '10 ОТРК "Іскандер" з Брянська по Київщині.'
    ),
    "Планується залучення ОТРК «Іскандер» по Київщині.",
    "По Києву було застосовано балістичні ракети. Атака завершена.",
    "💥 Одещина вибухи, дорозвідка.",
    (
        "Уточнена інформація щодо ракетного удару по Києву: "
        "зафіксовано влучання балістичної ракети."
    ),
    (
        "У ніч на 28 липня противник атакував Київ та Київщину "
        "балістичними і крилатими ракетами та ударними БпЛА. "
        "Збито/подавлено більшість повітряних цілей. "
        "Зафіксовано влучання."
    ),
    (
        "Чисто на околицях, Київ трішки на перекур. "
        "Присутні цілі в області, але не так близько, очікуємо підліт."
    ),
]

SAFETY_CASES: list[str] = [
    "Мінус",
    "🚀 Ракета на Київ.\n\nРакета припинила своє існування.",
    "☄ Балістика на Київ.\n\nРакети припинили своє існування.",
    "По Києву все, цілей більше немає.",
    "КИЇВ УВАГА!\n\nЦІЛІ ЗНИКЛИ.",
    "КИЇВ УВАГА!\nЦІЛІ ЗНИКЛИ",
    "Все тихо",
    "балістика відбій",
    "⚪️ Відбій загрози балістики.",
    "🟢 ВІДБІЙ ТРИВОГИ | Київ10:00",
    "🟡Чисто на цю мить.",
    "Цілей поки немає.",
    "По балістичних цілях — чисто.",
    "По «реактивних » також чисто.",
    "Область візуально чисто",
    "❕ Локаційно область чиста",
    "❕Припинила існування.",
]


@pytest.mark.parametrize(
    "text",
    SAFETY_CASES,
)
def test_safety_does_not_match(text: str) -> None:
    """Explicit clear posts should not raise danger flags."""
    detector = DangerDetector(REGION_PATTERNS, [])

    detection = detector.danger(text)

    assert detection.danger is False, text
    assert detection.status is DetectionStatus.SAFE, text
    assert detection.type is None, text
    assert detector.is_safe(text) is True, text


@pytest.mark.parametrize("text", IGNORED_CASES)
def test_ignored_messages_do_not_clear_danger(text: str) -> None:
    """Reports and forecasts veto danger wording without signalling all-clear."""
    detector = DangerDetector(REGION_PATTERNS, [])

    assert detector.is_ignored(text) is True
    for checker in (
        detector.danger,
        detector.irbm_danger,
        detector.mlrs_danger,
        detector.guided_bomb_danger,
        detector.ballistic_danger,
        detector.cruise_missile_danger,
        detector.drone_danger,
        detector.generic_danger,
    ):
        detection = checker(text)
        assert detection.status is DetectionStatus.IGNORED
        assert detection.danger is False
        assert detection.type is None


@pytest.mark.parametrize(
    "text",
    [
        "Буде відбій згодом.",
        "Цей мінус, ще один через Димер у бік Вишгорода/Гостомеля.",
        (
            "По ракетам чисто наразі, відбулись масовані пуски реактивних "
            "дронів. Близько 10 реактивних летять на Київщину."
        ),
    ],
)
def test_future_or_partial_clear_is_not_safe(text: str) -> None:
    """Future or weapon-specific clear wording should not veto current danger."""
    detector = DangerDetector(REGION_PATTERNS, [])

    assert detector.is_safe(text) is False, text


def test_safety_wording_and_exclusions_are_independent() -> None:
    """A report can contain all-clear wording without clearing active danger."""
    detector = DangerDetector(REGION_PATTERNS, [])
    text = "По Києву було застосовано балістичні ракети. Атака завершена."

    assert detector.is_safe(text) is True
    assert detector.is_ignored(text) is True
    assert detector.danger(text).status is DetectionStatus.IGNORED
