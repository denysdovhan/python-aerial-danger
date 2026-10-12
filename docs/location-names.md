# Location name sources

Verified on 2026-10-12. The library owns location display names; Home Assistant
ships generated selector labels. Names do not change the matcher patterns.

## Existing labels

All 25 region labels and 168 locality labels in each language were copied exactly
from [ha-aerial-danger](https://github.com/denysdovhan/ha-aerial-danger/tree/83b9bb4/custom_components/aerial_danger/translations).
The expanded branch initially lacked 12 released presets. Merging current main
restored them and the released matching fixes before importing their labels.

## Official settlement names

604 additional settlement labels use the Ukrainian spelling from the Ministry's
[KATOTTG release of 2026-07-07](https://mininfra.gov.ua/storage/app/sites/1/uploaded-files/kodifikator-07-07.xlsx),
linked from the [official catalogue](https://mininfra.gov.ua/diialnist/rozvytok-mistsevoho-samovriaduvannia/kodyfikator-administratyvno-terytorialnykh-odynyts-ta-terytorii-terytorialnykh-hromad).
Downloaded workbook SHA-256: `5c5317759b2b90208e9b00338bc3db3c5e694272a166acf73f1543b3e18ecbea`.

Names were matched within their owning oblast using the locality ID's transliterated
suffix. Only a single distinct Ukrainian name was accepted automatically. Multiple
settlements with the same name can share a display name; this does not establish a
unique government identifier or coordinates. Those metadata are outside this change.

English settlement labels transliterate the verified Ukrainian name using the
[Cabinet of Ministers table](https://zakon.rada.gov.ua/laws/show/55-2010-%D0%BF#Text)
linked by the [State Migration Service](https://dmsu.gov.ua/services/transliteration.html).
They are transliterations, not literal English translations of proper names.
Apostrophes and soft signs are omitted; initial Є/Ї/Й/Ю/Я and зг are handled separately.
Existing HA English spellings remain unchanged.

These legacy ID spellings required explicit matching to the same oblast's register:

| Stable ID                             | Verified Ukrainian name |
| ------------------------------------- | ----------------------- |
| `chernihiv_oblast_novhorod_siverskyy` | Новгород-Сіверський     |
| `kharkiv_oblast_staryy_saltiv`        | Старий Салтів           |
| `kyiv_oblast_boyarka`                 | Боярка                  |
| `kyiv_oblast_gatne`                   | Гатне                   |
| `kyiv_oblast_kalita`                  | Калита                  |
| `kyiv_oblast_kryachky`                | Крячки                  |
| `kyiv_oblast_plyuty`                  | Плюти                   |
| `kyiv_oblast_skibyn`                  | Скибин                  |
| `kyiv_oblast_suvid`                   | Сувид                   |
| `kyiv_oblast_svitilnia`               | Світильня               |
| `mykolaiv_oblast_snigurivka`          | Снігурівка              |
| `odesa_oblast_mayaky`                 | Маяки                   |
| `sumy_oblast_putivl`                  | Путивль                 |

## Districts, neighbourhoods, and landmarks

The three named Kyiv districts use the register's additional level. Their English
labels translate район as District. The existing collective Петрівці preset stays
collective: the register lists Нові Петрівці and Старі Петрівці separately. No single
settlement identity is asserted for that preset. Existing IDs, including the legacy
`boyarka` and released `boiarka` entries, remain available for saved selections.

The other 12 names were checked against city authorities or the site's operator.
English names use transliteration, translated place-type words, or the operator's
Latin brand spelling. No additional matching aliases were derived from display names.

| ID                              | Ukrainian         | English                      | Evidence                                                                                                         |
| ------------------------------- | ----------------- | ---------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `kyiv_comfort_town`             | Комфорт Таун      | Comfort Town                 | [Source](https://comforttown.com.ua/main)                                                                        |
| `kyiv_faina_town`               | Файна Таун        | Fayna Town                   | [Source](https://faynatown.com.ua/living_quarter)                                                                |
| `kyiv_feofaniia`                | Феофанія          | Feofaniia                    | [Source](https://golos-2023.kyivcity.gov.ua/content/turystam.html)                                               |
| `kyiv_korchuvate`               | Корчувате         | Korchuvate                   | [Source](https://golos-2023.kyivcity.gov.ua/content/turystam.html)                                               |
| `kyiv_pyrohiv`                  | Пирогів           | Pyrohiv                      | [Source](https://golos-2023.kyivcity.gov.ua/content/turystam.html)                                               |
| `kyiv_respublika`               | Республіка        | Respublika                   | [Source](https://respublika.kiev.ua/)                                                                            |
| `kyiv_retroville`               | Ретровіль         | Retroville                   | [Source](https://retroville.ua/)                                                                                 |
| `kyiv_sotsmisto`                | Соцмісто          | Sotsmisto                    | [Source](https://dnipr.kyivcity.gov.ua/news/na-robochiy-naradi-obgovorili-detalniy-plan-teritorii-zhm-sotsmisto) |
| `kyiv_sovky`                    | Совки             | Sovky                        | [Source](https://solom-2023.kyivcity.gov.ua/content/mennyu-1.html?PrintVersion=)                                 |
| `kyiv_trukhaniv_island`         | Труханів острів   | Trukhaniv Island             | [Source](https://guide.kyivcity.gov.ua/places/trukhaniv-ostriv)                                                  |
| `kyiv_varshavskyi`              | Варшавський масив | Varshavskyi Residential Area | [Source](https://stolitsagroup.com/)                                                                             |
| `zaporizhzhia_oblast_sotsmisto` | Соцмісто          | Sotsmisto                    | [Source](https://zp.gov.ua/news/249009-u-molodiznomu-centri-vidkrilasia-fotovistavka)                            |
