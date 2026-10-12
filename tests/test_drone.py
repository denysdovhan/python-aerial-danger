"""Tests for drone danger detection."""

# ruff: noqa: S101

from aerial_danger import DangerDetector, DangerType
from aerial_danger.keywords import DRONE_DANGER
from aerial_danger.location_presets import LOCATION_PRESETS
from aerial_danger.pattern_utils import resolve_locality_patterns

from .common import LOCALITY_PATTERNS, REGION_PATTERNS

DRONE_CASES: list[tuple[str, str]] = [
    (DRONE_DANGER[10], "🛵 У бік Нивок."),
    (DRONE_DANGER[10], "🛵 Нивки, може бути гучно!"),
    (DRONE_DANGER[10], "🛵 Курс на Нивки/Святошино."),
    (DRONE_DANGER[11], "Святошино/Нивки 🛵"),
    (DRONE_DANGER[14], "Нивки над вами БПЛА!"),
    (DRONE_DANGER[21], "❗️ Київ — 1х Академ/Коцюбинське."),
    (
        DRONE_DANGER[21],
        "Київ:\n 1х Нивки/Сирець\n 2х Жуляни\n \n 1х ДВРЗ/Березняки",
    ),
    (DRONE_DANGER[21], "❗️ Київ — 1х Нивки Сирець"),
    (DRONE_DANGER[22], "Київ: \n 2х Куренівка Нивки \n 1х Бортничі"),
    (DRONE_DANGER[22], "❗️ Київ — 1х на Святошин."),
    (DRONE_DANGER[31], "Антонов йде!"),
]

DESCENT_DRONE_CASES: list[str] = [
    "1х падає на Солом'янку/Чоколівку.",
    "1х Білогородка падає.",
    "1х Білогородка. Падає.",
    "Падає Жуляни\n800м",
    "Сирець, падає",
    "1х на зниження Берестейська.",
    "Київ:\n🔻Зниження Нивки",
    "Київ:\n🔻Зниження Шулявка",
    "**🔻Зниження** Київ товарний",
]

DRONE_MESSAGE_CASES: list[str] = [
    *DESCENT_DRONE_CASES,
    "1х керований реактив у бік Виноградаря.",
    "Нивки увага БПЛА!",
    "🛵 Шахед на Академмістечко.",
    "🛵 Нивки!",
    "🛵На Святошино йде!",
    "🛵 Шулявка/Солома.",
    "🛵 Нивки – шахед.",
    "🟡🛵Академмістечко!",
    "🟡🛵 Шахед на Біличі/Берестейський проспект!",
    "На Нивки йде",
]

REPORTED_DRONE_LOCALITY_CASES: list[tuple[str, str]] = [
    (r"\bлісовий\b", "Область чистоНад Києвом 1, на Лісовий йде"),
    (
        r"\bбровар(и|ів|ах)?\b",
        "‼️🛵Залітають через Бровари на Київ.@operinform",
    ),
    (r"\bбровар(и|ів|ах)?\b", "Бровари на Київ БПЛА"),
    (
        r"\bостер\b",
        "🛵Реактивний Шахед через Остер на Київ!",
    ),
]

REGION_ONLY_DRONE_CASES: list[str] = [
    *DESCENT_DRONE_CASES,
    "🟡🛵 Шахеди над Києвом, вектор Теремки, Виноградар та Чоколівка!",
    "1х керований реактив у бік Виноградаря.",
    "⚠️ 5х БпЛА на північ від Києва. \n 6х БпЛА у напрямку Вишневе/Білогородка",
    "Область чистоНад Києвом 1, на Лісовий йде",
    "Над Києвом 1, на Лісовий йде",
    "Область чисто\nНад Києвом 1, на Лісовий йде",
    "🛵 БпЛА ➡️ курсом на Київ з північного сходу!",
    "‼️🛵Залітають через Бровари на Київ.@operinform",
    "Бровари на Київ БПЛА",
    "🛵Реактивний Шахед через Остер на Київ!",
    "🛵 Київ!",
]

REACTIVE_DRONE_CASES: list[tuple[str, str, str]] = [
    (
        r"\bтроєщин(а|и|і|у|ою)?\b",
        DRONE_DANGER[0],
        "Реактивний Шахед наближається до Києва, вектор Троєщина.",
    ),
    (
        r"\bзаток(а|и|у|ою)?\b",
        DRONE_DANGER[1],
        "❗️ Реактивна ціль у напрямку Затока, Одещина.",
    ),
    (r"\bнив(ки|ками|ок)\b", DRONE_DANGER[2], "🛵 Реактивні БпЛА на Нивки"),
    (
        r"\bдніпропетровщин(а|и|і|у|ою)?\b",
        DRONE_DANGER[2],
        "🛵 Реактивний БпЛА на Дніпропетровщині, курс на північ Кривого Рогу.",
    ),
    (
        r"\bдимер(а|у|ом|і)?\b",
        DRONE_DANGER[2],
        "Київщина:\n1х реактивний БпЛА повз Димер у Вишгородському районі.",
    ),
    (
        r"\bбровар(и|ів|ах)?\b",
        DRONE_DANGER[2],
        "🛵 Реактивний БпЛА курсом на Бровари!",
    ),
    (
        r"\bодеськ(ий|ого|ому) район\b",
        DRONE_DANGER[3],
        "Пара реактивних клоунів в морі курсом на Одеський район.",
    ),
    (
        r"\bбровар(и|ів|ах)?\b",
        DRONE_DANGER[4],
        "Реактивний дрон повз Бровари.",
    ),
    (r"\bтро(я|ю)\b", DRONE_DANGER[4], "1 реактивний дрон летить на Трою."),
    (r"\bоболон(ь|і|ню)\b", DRONE_DANGER[4], "Реактивний дрон на Оболонь."),
    (r"\bсолом(а|ою|и)?\b", DRONE_DANGER[5], "Реактивний над Соломою🛵"),
    (r"\bвишгород", DRONE_DANGER[5], "Реактивний на Вишгород"),
    (r"\bславутич", DRONE_DANGER[5], "Реактивний повз Славутич на море"),
    (
        r"\bяготин(а|у|ом|і)?\b",
        DRONE_DANGER[6],
        "Реактивний в бік Яготина з Полтавщини",
    ),
    (
        r"\bбровар(и|ів|ах)?\b",
        DRONE_DANGER[6],
        "🛵Новий реактивний у бік Броварів та Борисполя!",
    ),
    (r"\bодес(а|и|у|ою)?\b", DRONE_DANGER[7], "Одеса наступний реактивний 5хв."),
    (r"\bславутич", DRONE_DANGER[7], "Славутич реактивний 5500 висота"),
    (r"\bлів(ий|ого|ому) берег\b", DRONE_DANGER[7], "Лівий берег - реактивний йде!"),
    (r"\bтро(я|ю)\b", DRONE_DANGER[7], "🛵 Троя, реактивний"),
    (r"\bніжин(а|у|ом|і)?\b", DRONE_DANGER[8], "2 реактивних на Ніжин йде"),
    (
        r"\bтроєщин(а|и|і|у|ою)?\b",
        DRONE_DANGER[8],
        "4 реактивних на Київ, перший на Троєщину/Оболонь.",
    ),
    (
        r"\bвідрадн(ий|ого|ому|им)?\b",
        DRONE_DANGER[9],
        "❗️ Київ 1х реактив, Відрадний Святошин",
    ),
    (
        r"\bкам[’']янськ(ий|ого|ому)?\b",
        DRONE_DANGER[9],
        "❗️ 1х реактив у Кам'янському районі Дніпропетровської області.",
    ),
]

REACTIVE_DRONE_AFTERMATH_CASES: list[tuple[str, str]] = [
    (
        r"\bдарницьк(ий|ого|ому)?\b",
        "Під час минулої повітряної атаки ворог застосував реактивний дрон "
        "типу “Герань-3”. Характерний звук було чутно в Дарницькому районі.",
    ),
    (
        r"\bнив(ки|ками|ок)\b",
        "Під час минулої атаки реактивний дрон було збито над Нивками.",
    ),
]


def test_drone_only() -> None:
    """Drone-specific helper should flag drone samples."""
    detector = DangerDetector(REGION_PATTERNS, LOCALITY_PATTERNS)
    for danger_template, text in DRONE_CASES:
        detection = detector.drone_danger(text)
        assert detection.danger is True, text
        assert detection.type == DangerType.DRONE, text
        assert detection.area_pattern is not None, text
        assert detection.danger_pattern == danger_template.replace(
            "{area}", detection.area_pattern
        ), text
        assert detector.danger(text).type == DangerType.DRONE, text


def test_drone_messages() -> None:
    """Drone messages should match their configured locality."""
    detector = DangerDetector(REGION_PATTERNS, LOCALITY_PATTERNS)
    for text in DRONE_MESSAGE_CASES:
        detection = detector.drone_danger(text)
        assert detection.danger is True, text
        assert detection.type == DangerType.DRONE, text
        assert detector.danger(text).type == DangerType.DRONE, text


def test_falling_drone_messages_match_selected_localities() -> None:
    """Falling alerts should match each selected area in the message."""
    cases = [
        ("kyiv_oblast", "kyiv_oblast_stoianka", "1х падає Стоянка."),
        ("kyiv", "kyiv_center", "1х падає Центр\n1.2 км"),
        ("kyiv", "kyiv_antonov", "1х падає Антонов\n1.2 км"),
    ]
    for region_id, locality_id, text in cases:
        localities = resolve_locality_patterns([], [region_id], [locality_id])
        detector = DangerDetector([], localities)
        detection = detector.drone_danger(text)

        assert detection.danger is True, text
        assert detection.type == DangerType.DRONE, text
        assert detector.danger(text).type == DangerType.DRONE, text


def test_reported_drone_messages_match_configured_locality() -> None:
    """Reported drone messages should use an explicitly configured locality."""
    for locality_pattern, text in REPORTED_DRONE_LOCALITY_CASES:
        detector = DangerDetector([], [locality_pattern])

        detection = detector.danger(text)

        assert detection.danger is True, text
        assert detection.type == DangerType.DRONE, text


def test_reported_drone_messages_do_not_match_region() -> None:
    """Reported drone messages should not fall through to a region match."""
    detector = DangerDetector([r"\bки(ї|є)в(а|у|ом|е|і)?\b"], [])
    for text in REGION_ONLY_DRONE_CASES:
        detection = detector.danger(text)

        assert detection.danger is False, text
        assert detection.type is None, text


def test_drone_route_requires_selected_locality() -> None:
    """A city mention must not trigger for a different selected neighborhood."""
    detector = DangerDetector(REGION_PATTERNS, LOCALITY_PATTERNS)
    text = "Область чистоНад Києвом 1, на Лісовий йде"

    detection = detector.danger(text)

    assert detection.danger is False
    assert detection.type is None
    assert detector.is_safe(text) is False


def test_drone_attention_requires_selected_locality() -> None:
    """A drone attention alert must not fall back to the configured city."""
    text = "Київ Виноградар увага по БПЛА"
    kyiv = LOCATION_PRESETS["kyiv"]
    for locality_id, expected_type in (
        (None, None),
        ("kyiv_nyvky", None),
        ("kyiv_vynohradar", DangerType.DRONE),
    ):
        localities = kyiv.localities[locality_id].patterns if locality_id else []
        detector = DangerDetector(kyiv.patterns, localities)

        detection = detector.danger(text)

        assert detection.danger is (expected_type is not None), locality_id
        assert detection.type == expected_type, locality_id
        assert detection.message == text
        assert detector.generic_danger(text).danger is False, locality_id
        assert detector.is_safe(text) is False


def test_reactive_drone_danger() -> None:
    """Reactive-drone alerts should match their area-specific phrase."""
    for area_pattern, danger_template, text in REACTIVE_DRONE_CASES:
        detector = DangerDetector([], [area_pattern])

        detection = detector.danger(text)

        assert detection.danger is True, text
        assert detection.type == DangerType.DRONE, text
        assert detection.danger_pattern == danger_template.replace(
            "{area}", area_pattern
        ), text


def test_reactive_drone_aftermath_does_not_match() -> None:
    """Reactive-drone aftermath should not raise danger flags."""
    for area_pattern, text in REACTIVE_DRONE_AFTERMATH_CASES:
        detector = DangerDetector([], [area_pattern])

        detection = detector.danger(text)

        assert detection.danger is False, text
        assert detection.type is None, text
