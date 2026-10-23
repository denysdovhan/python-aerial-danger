"""Tests for generic danger detection."""

# ruff: noqa: S101

import pytest

from aerial_danger import DangerDetector, DangerType, DetectionStatus
from aerial_danger.location_presets import LOCATION_PRESETS

from .common import LOCALITY_PATTERNS, REGION_PATTERNS

GENERIC_CASES: list[str] = [
    "У бік Києва!!!!",
    "На Васильків підлітає",
    "Васильків, над містом",
    "Васильків увага",
    "Васік увага",
    "🔴🚀Нивки.",
    "🔴❗️Вектор Київ!",
    "🔴❗️Київ!",
    "🔴🚀 Київ!!",
    "❗️Київ!",
    "🟡Київ!",
    "🚀Нивки!",
    "Далі Нивки.",
    "❗️На Нивки!",
    "БОЯРКА - ВИШНЕВЕ - КИЇВ!!",
    "КИЇВ",
    "КИЇВ!",
    "КИЇВ 2 СТІНИ!",
    "КИЇВ Є ЦІЛІ!",
    "КИЇВ ЦІЛЬ!",
    "Київ є ЦІЛЬ!",
    "КИЇВ УВАГА!",
    "Київ зреагувати!!",
    "‼️Київ!",
    "Київ жахне!!",
    "Київ/Вишгород увага",
    "🔴🚀 Вектор руху на Київ!",
    "🚀 Вектор на столицю!",
    "ЦІЛЬ КИЇВЩИНА!",
    "Київ в укриття!",
    "Київ в укриття",
    "Київ до укриття",
    "Київ — в укриття",
    "Нивки зреагувати!",
    "Київ ваш вектор!",
    "Далі на Київ йде 2 цілі!!",
    "Петропавлівська на Академ/Святошин!",
    "Нивки!!!",
    "Нивки підліт",
    "Святошинський - увага !",
    "КИЇВ 2 ЦІЛІ!",
    "Курс - Київ!",
    "Нивки - Антонов!",
    "Антонов, Коцюба.",
    "Київщина увага ще ЦІЛЬ!",
    "Київ повторно!",
    "Курсом на Київ!",
    "ЦІЛЬ КИЇВ",
    "КИЇВ ДВІ СТІНИ",
    "2 цілі на Київ",
    "КИЇВ УВАГА!!!!!",
    "КИЇВ ХВИЛИНА!!",
    "Київ ще групові, увага!",
    "🚀 Академмістечко",
    "🔴Київ!",
    "НИВКИ УВАГА!!!!!!!!",
    "🚀 Знову ціль на Київ!",
    "🚀Київ в укриття",
    "Київ !!!",
    "КИЇВ СХОВАЛИСЬ В ДВІ СТІНИ",
    "🔴🚀Нивки!",
    "🔴🚀 Святошин!",
    "🚀 Святошино/Нивки!",
    "Пролітає Галагани та Файна таун.",
    "Галагани на Святошин, Антонов. Нивки готовність!",
    "Хвилина до заходу в Київ!",
    "🔴🚀Вишгород/Оболонь!",
    "Бровари підліт. Ви його не почуєте. Від вікон.",
]

REGION_ONLY_INCOMING_WEAPON_CASES: list[tuple[str, str]] = [
    (r"\bчернігівщин\w*\b", "🛵 З Чернігівщини йде один БпЛА."),
    (r"\bкиїв\b", "Шахед на Київ підлітає"),
    (r"\bки(ї|є)в(а|у|ом|е|і)?\b", "🟡💣 Київ!"),
    (r"\bхарків(а|у|ом|і)?\b", "🔴❗️ РСЗВ на Харків!"),
    (
        r"\bдніпропетровщин(а|и|і|у|ою)?\b",
        "🟡💣 КАБи на Дніпропетровщині, вектор Кривий Ріг!",
    ),
    (
        r"\bхарків(а|у|ом|і)?\b",
        "🟡💣 КАБ на Харків, вектор Стара Салтівка!",
    ),
]

GENERIC_WHOLE_MESSAGE_CASES: list[str] = [
    "Нивки\nЖуляни",
    "У бік Києва!!!!",
    "КИЇВ!",
    "НИВКИ!",
    "❗️На Нивки!",
    "🔴❗️Вектор Київ!",
    "Курсом на Київ!",
]

GENERIC_NO_MATCH_CASES: list[str] = [
    "Якщо піде до нас — маємо ще близько ~25 хвилин.",
    (
        "У столиці з 15 вересня на хвилину мовчання світлофори поступово "
        "переходитимуть у режим повної зупинки руху 🔴"
    ),
    "Столиця, маєте ще хвилин ~20 хв перекуру 🚬",
    "Київ-Пасажирський!",
    (
        "🟡 УВАГА! У Києві оголошена дронова небезпека!"
        "Просимо всіх терміново прослідувати в укриття цивільного захисту!"
    ),
    (
        "🟣 **Загроза балістики з Курська. Увага.**\n\n"
        "Імовірний пуск ракет системи  «Іскандер», \n"
        "або робота ворожої ППО С-300/С-400."
    ),
]


def test_generic_only() -> None:
    """Generic helper should flag generic samples."""
    detector = DangerDetector(REGION_PATTERNS, LOCALITY_PATTERNS)
    for text in GENERIC_CASES:
        detection = detector.generic_danger(text)
        assert detection.danger is True, text
        assert detection.type == DangerType.GENERIC, text
        assert detector.danger(text).type == DangerType.GENERIC, text


@pytest.mark.parametrize(
    "localities", [(), LOCATION_PRESETS["kyiv"].localities["kyiv_nyvky"].patterns]
)
def test_weapon_messages_do_not_fall_through_to_generic(
    localities: tuple[str, ...],
) -> None:
    """Typed messages with only a region match should stay neutral."""
    for region_pattern, text in REGION_ONLY_INCOMING_WEAPON_CASES:
        detector = DangerDetector([region_pattern], localities)

        for checker in (detector.generic_danger, detector.danger):
            detection = checker(text)

            assert detection.status is DetectionStatus.IGNORED, text
            assert detection.danger is False, text
            assert detection.type is None, text
            assert detection.message == text


def test_terse_generic_matches_complete_message() -> None:
    """Terse generic warnings should preserve the complete matched text."""
    detector = DangerDetector(REGION_PATTERNS, LOCALITY_PATTERNS)
    for text in GENERIC_WHOLE_MESSAGE_CASES:
        detection = detector.generic_danger(text)

        assert detection.danger is True, text
        assert detection.type == DangerType.GENERIC, text
        assert detection.matched_danger == text, text


def test_area_list_matches_each_selected_locality() -> None:
    """Each selected locality in a bare area list should independently match."""
    cases = [
        ("Нивки\nЖуляни", ("kyiv_nyvky", "kyiv_zhuliany")),
        (
            "Рибальський острів - Поділ - Почайна",
            ("kyiv_rybalskyi_ostriv", "kyiv_podil", "kyiv_pochaiana"),
        ),
    ]
    for text, locality_ids in cases:
        for locality_id in locality_ids:
            patterns = LOCATION_PRESETS["kyiv"].localities[locality_id].patterns
            detection = DangerDetector([], patterns).danger(text)

            assert detection.type == DangerType.GENERIC, locality_id
            assert detection.matched_danger == text, locality_id


def test_direction_reports_match_selected_locality() -> None:
    """Terse direction reports preserve the place name and complete alert."""
    cases = [
        ("kyiv_oblast_khotiv", "На Хотів - Лісники.", "Хотів"),
        ("kyiv_oblast_khotiv", "На Хотів / Чабани", "Хотів"),
        ("kyiv_oblast_khotiv", "На Хотів-Чабани", "Хотів"),
        ("kyiv_oblast_khotiv", "До Хотів", "Хотів"),
        ("kyiv_oblast_khotiv", "Повз Хотів", "Хотів"),
        ("kyiv_oblast_khotiv", "На Хотів - Чабани - Гатне", "Хотів"),
        ("kyiv_oblast_khotiv", "На Хотів - Феофанію", "Хотів"),
    ]
    region = LOCATION_PRESETS["kyiv_oblast"]
    for locality_id, text, matched_area in cases:
        localities = region.localities[locality_id].patterns
        detection = DangerDetector([], localities).danger(text)

        assert detection.type == DangerType.GENERIC, text
        assert detection.message == text
        assert detection.matched_area == matched_area, text
        assert detection.matched_danger == text, text
        assert not DangerDetector(region.patterns, []).danger(text).danger, text
        unrelated = region.localities["kyiv_oblast_mriia"].patterns
        assert not DangerDetector([], unrelated).danger(text).danger, text


def test_station_attention_requires_selected_locality() -> None:
    """A station name must not trigger an attention alert for its city."""
    text = "Київ-Товарний увага!"
    kyiv = LOCATION_PRESETS["kyiv"]
    for locality_id, expected_type in (
        (None, None),
        ("kyiv_nyvky", None),
        ("kyiv_tovarnyi", DangerType.GENERIC),
    ):
        localities = kyiv.localities[locality_id].patterns if locality_id else []
        detector = DangerDetector(kyiv.patterns, localities)

        detection = detector.danger(text)

        assert detection.danger is (expected_type is not None), locality_id
        assert detection.type == expected_type, locality_id
        assert detection.message == text
        assert detector.is_safe(text) is False
        if expected_type is not None:
            assert detection.matched_danger == text
            assert detection.danger_pattern is not None
            assert any(pattern in detection.danger_pattern for pattern in localities)


def test_generic_does_not_match() -> None:
    """Non-alert explanations should not raise danger flags."""
    detector = DangerDetector([*REGION_PATTERNS, r"\bкурськ\w*\b"], LOCALITY_PATTERNS)
    for text in GENERIC_NO_MATCH_CASES:
        detection = detector.danger(text)

        assert detection.danger is False, text
        assert detection.type is None, text
        assert detector.is_safe(text) is False, text
