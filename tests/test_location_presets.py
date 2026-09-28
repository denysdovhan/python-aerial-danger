"""Tests for area pattern presets."""

# ruff: noqa: S101

import re

from aerial_danger import DangerDetector
from aerial_danger.location_presets import LOCATION_PRESETS
from aerial_danger.pattern_utils import (
    locality_ids,
    resolve_locality_patterns,
    resolve_region_patterns,
)

PRESET_EXAMPLES = {
    "cherkasy_oblast": ("Черкащиною", "Черкаській області"),
    "cherkasy_oblast_cherkasy": ("Черкас",),
    "chernihiv_oblast": ("Чернігівщиною", "Чернігівській області"),
    "chernihiv_oblast_chernihiv": ("Чернігова",),
    "chernihiv_oblast_semenivka": ("Семенівка", "Семенівку"),
    "chernivtsi_oblast": (
        "Буковиною",
        "Чернівеччиною",
        "Чернівецькою областю",
    ),
    "chernivtsi_oblast_chernivtsi": ("Чернівців",),
    "dnipropetrovsk_oblast": ("Дніпропетровщиною", "Дніпропетровській області"),
    "dnipropetrovsk_oblast_dnipro": ("Дніпром",),
    "dnipropetrovsk_oblast_kamianske": ("Кам'янському",),
    "dnipropetrovsk_oblast_kryvyi_rih": ("Кривого Рогу",),
    "dnipropetrovsk_oblast_pavlohrad": ("Павлоградом",),
    "donetsk_oblast": ("Донеччиною", "Донецькій області"),
    "donetsk_oblast_donetsk": ("Донецьку",),
    "donetsk_oblast_sloviansk": ("Словʼянськ",),
    "ivano_frankivsk_oblast": (
        "Франківщиною",
        "Івано-Франківщиною",
        "Івано-Франківській області",
    ),
    "ivano_frankivsk_oblast_ivano_frankivsk": ("Івано-Франківську",),
    "kharkiv_oblast": ("Харківщиною", "Харківській області"),
    "kharkiv_oblast_balakliia": ("Балаклією",),
    "kharkiv_oblast_bohodukhiv": ("Богодуховом",),
    "kharkiv_oblast_derzhprom": ("Держпрому",),
    "kharkiv_oblast_kharkiv": ("Харкові",),
    "kharkiv_oblast_khtz": ("хтз",),
    "kharkiv_oblast_kozacha_lopan": ("Козачою Лопанню",),
    "kharkiv_oblast_kulynychi": ("Кулиничах",),
    "kharkiv_oblast_kupiansk": ("Куп'янськом",),
    "kharkiv_oblast_piatykhatky": ("П'ятихатках",),
    "kharkiv_oblast_saltivka": ("Салтівкою",),
    "kharkiv_oblast_vokzal": ("Вокзал",),
    "kherson_oblast": ("Херсонщиною", "Херсонській області"),
    "kherson_oblast_kherson": ("Херсону",),
    "khmelnytskyi_oblast": ("Хмельниччиною", "Хмельницькій області"),
    "khmelnytskyi_oblast_khmelnytskyi": ("Хмельницького",),
    "kirovohrad_oblast": ("Кіровоградщиною", "Кіровоградській області"),
    "kirovohrad_oblast_kropyvnytskyi": ("Кропивницького",),
    "kyiv": ("Києва", "Києві", "Києву", "Києвом", "столиця"),
    "kyiv_akademmistechko": ("Академмістечком",),
    "kyiv_beresteiska": ("Берестейська", "Берестейську"),
    "kyiv_darnytsia": ("Дарницький масив",),
    "kyiv_lisovyi_masyv": ("Лісовий",),
    "kyiv_livoberezhnyi_masyv": ("Лівобережний",),
    "kyiv_minskyi_masyv": ("Мінський",),
    "kyiv_pasazhyrskyi": ("Київ-Пасажирський", "Київ Пасажирський"),
    "kyiv_shuliavka": ("Шуля", "Шулі", "Шулю", "Шулею", "Шульою", "Шуле"),
    "kyiv_rybalskyi_ostriv": ("Рибальський острів", "Рибальський"),
    "kyiv_sviatoshyn": ("Святошино",),
    "kyiv_tovarnyi": ("Київ товарний", "Київ-Товарний", "Київ Товарний"),
    "kyiv_troieshchyna": ("Троєщини",),
    "kyiv_vidradnyi": ("Відрадний",),
    "kyiv_voskresenka": ("Воскресенка",),
    "kyiv_vynohradar": ("Виноградаря", "Виноградара"),
    "kyiv_oblast": (
        "Київщина",
        "Київщини",
        "Київщині",
        "Київщину",
        "Київщиною",
        "Київської області",
        "Київській області",
        "Київську область",
        "Київською областю",
    ),
    "kyiv_oblast_bila_tserkva": ("Білої Церкви", "Білу Церкву", "БЦ"),
    "kyiv_oblast_bilohorodka": ("Білогородка",),
    "kyiv_oblast_boryspil": (
        "Борисполя",
        "Борисполю",
        "Борисполем",
        "Борисполі",
        "Борік",
    ),
    "luhansk_oblast": ("Луганщиною", "Луганській області"),
    "luhansk_oblast_luhansk": ("Луганську",),
    "lviv_oblast": ("Львівщиною", "Львівській області"),
    "lviv_oblast_lviv": ("Львова",),
    "mykolaiv_oblast": ("Миколаївщиною", "Миколаївській області"),
    "mykolaiv_oblast_mykolaiv": ("Миколаєва",),
    "mykolaiv_oblast_ochakiv": ("Очакова", "Очаковом"),
    "odesa_oblast": ("Одещина", "Одещини", "Одещиною", "Одеською областю"),
    "odesa_oblast_arkadiia": ("Аркадією",),
    "odesa_oblast_bilhorod_dnistrovskyi": ("Білгород Дністровському",),
    "odesa_oblast_chornomorsk": (
        "Чорноморськ",
        "Чорноморська",
        "Чорноморськом",
    ),
    "odesa_oblast_karolino_buhaz": ("Кароліно Бугазом",),
    "odesa_oblast_khadzhybeiskyi_raion": ("Хаджибейському районі",),
    "odesa_oblast_novi_biliari": ("Нові Білярі",),
    "odesa_oblast_odesa": ("Одесою",),
    "odesa_oblast_odesa_port": ("Одеському порту", "Одеса / порт"),
    "odesa_oblast_ovidiopol": ("Овідіополем",),
    "odesa_oblast_peresyp": ("Пересипом",),
    "odesa_oblast_zatoka": ("Затокою",),
    "poltava_oblast": ("Полтавщиною", "Полтавській області"),
    "poltava_oblast_poltava": ("Полтаву",),
    "rivne_oblast": ("Рівненщиною", "Рівненській області"),
    "rivne_oblast_rivne": ("Рівне",),
    "sumy_oblast": ("Сумщиною", "Сумській області"),
    "sumy_oblast_myropillia": ("Миропілля",),
    "sumy_oblast_shostka": ("Шостка", "Шостки", "Шостку"),
    "sumy_oblast_shostkynskyi_raion": ("Шосткинський район", "Шосткинському району"),
    "sumy_oblast_sumy": ("Сум",),
    "sumy_oblast_varachyne": ("Варачине",),
    "ternopil_oblast": ("Тернопільщиною", "Тернопільській області"),
    "ternopil_oblast_ternopil": ("Тернополя",),
    "vinnytsia_oblast": ("Вінниччиною", "Вінницькій області"),
    "vinnytsia_oblast_vinnytsia": ("Вінницю",),
    "volyn_oblast": ("Волинню", "Волинській області"),
    "volyn_oblast_lutsk": ("Луцьку",),
    "zakarpattia_oblast": ("Закарпатською областю",),
    "zakarpattia_oblast_uzhhorod": ("Ужгороді",),
    "zaporizhzhia_oblast": ("Запорізькою областю",),
    "zaporizhzhia_oblast_komyshuvakha": ("Комишувахою",),
    "zaporizhzhia_oblast_orikhiv": ("Оріховом",),
    "zaporizhzhia_oblast_vilniansk": ("Вільнянськом",),
    "zaporizhzhia_oblast_zaporizhzhia": ("Запоріжжі", "ЗП"),
    "zhytomyr_oblast": ("Житомирщиною", "Житомирській області"),
    "zhytomyr_oblast_zhytomyr": ("Житомиром",),
}


def test_registry_ids_ownership_and_compilation() -> None:
    """Test stable IDs, nested ownership, and valid regexes."""
    assert locality_ids([]) == []
    for region_id, region in LOCATION_PRESETS.items():
        assert region.id == region_id
        assert re.fullmatch(r"[a-z]+(?:_[a-z]+)*", region.id)
        for locality_id, locality in region.localities.items():
            assert locality.id == locality_id
            assert re.fullmatch(r"[a-z]+(?:_[a-z]+)*", locality.id)
        assert region.localities
        assert locality_ids([region_id]) == list(region.localities)
    for region in LOCATION_PRESETS.values():
        assert list(region.localities) == sorted(region.localities)
        DangerDetector.validate_patterns(
            region.patterns,
            *(preset.patterns for preset in region.localities.values()),
        )


def test_preset_examples() -> None:
    """Test preset aliases, inflections, and alternate spellings."""
    patterns_by_id = {}
    for region_id, region in LOCATION_PRESETS.items():
        patterns_by_id[region_id] = region.patterns
        patterns_by_id.update(
            {
                preset_id: preset.patterns
                for preset_id, preset in region.localities.items()
            }
        )

    assert PRESET_EXAMPLES.keys() <= patterns_by_id.keys()
    for preset_id, texts in PRESET_EXAMPLES.items():
        for text in texts:
            assert any(
                re.search(pattern, text, re.IGNORECASE | re.UNICODE)
                for pattern in patterns_by_id[preset_id]
            ), (preset_id, text)


def test_boundaries_and_safe_location_text() -> None:
    """Test preset boundaries and ordinary location text stay safe."""
    regions = resolve_region_patterns([], ["kyiv"])
    localities = resolve_locality_patterns([], ["kyiv"], ["kyiv_akademmistechko"])
    detector = DangerDetector(regions, localities)
    assert not any(re.search(pattern, "Київщина", re.IGNORECASE) for pattern in regions)
    assert not any(
        re.search(pattern, "академія", re.IGNORECASE) for pattern in localities
    )
    assert not detector.danger("Станція метро Академмістечко відкрита").danger


def test_resolve_custom_first_deduplicates_and_ignores_unknown_ids() -> None:
    """Test resolution order, deduplication, and current-definition lookup."""
    kyiv_pattern = LOCATION_PRESETS["kyiv"].patterns[0]
    regions = resolve_region_patterns([kyiv_pattern, "custom"], ["missing", "kyiv"])
    localities = resolve_locality_patterns(
        [], ["missing", "kyiv"], ["kyiv_nyvky", "missing"]
    )
    assert regions == [kyiv_pattern, "custom", LOCATION_PRESETS["kyiv"].patterns[1]]
    assert localities == list(
        LOCATION_PRESETS["kyiv"].localities["kyiv_nyvky"].patterns
    )
