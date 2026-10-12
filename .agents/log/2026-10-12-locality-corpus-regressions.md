---
title: Locality corpus regression coverage
date: 2026-10-12
status: wip
related_paths:
  - tests/test_location_presets.py
  - tests/test_drone.py
  - src/aerial_danger/locations/sumy_oblast.json
---

# Locality corpus regression coverage

## Decision

PR #9 review requested behavioral coverage beyond JSON validation. Extend the
shared `PRESET_EXAMPLES` with frozen, exact Telegram spelling excerpts. Include
all 619 IDs added against main and the 65 older IDs without examples, so equality
with the live registry prevents future additions from silently skipping coverage.
Keep the existing examples. Do not generate expectations from regexes at test time.

The saved six-channel CSV corpus supplies 933 new spelling excerpts; Файна Таун
adds one independently researched excerpt. The latter is from an aftermath post,
so it is only a lexical positive, not an active-danger fixture. Examples test
spellings and inflections, not geographical attribution or every regex alternative.
In particular, the identical spelling Харківщина is also an oblast reference;
its lexical fixture does not validate attribution to the Sumy settlement.

Use representative exact corpus excerpts to reject personal-name/common-word
collisions and substring matches. Three complete drone posts exercise selected
locality gating and preserved matched text. Fix Duboviazivka's ASCII-only
apostrophe using the existing `['’ʼ]` convention. Test canonical apostrophized
catalog names separately rather than inventing punctuation variants of messages.

## Verification

- Before the fix, the corpus spelling, canonical-name, and drone-message tests
  fail on Duboviazivka. After the fix, all three pass.
- Every new spelling excerpt was checked as an exact substring of its source;
  saved source text was checked byte-for-byte against the CSV message text.
- [x] Locked dependency sync, Ruff format/lint, and all 79 tests pass.
- [ ] Current-head CI after push.

## Sources

Only spelling excerpts are stored in the shared example table. Source links stay
here, outside fixtures. Multiple links follow the order of examples for that ID.
The public Файна Таун post reads `Файна Таун.\nВиродки рознесли будинок`.

| Preset                                     | Observed excerpts and source posts                                                                                |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| `cherkasy_oblast_buky`                     | [Буки](https://t.me/AerisRimor/77483)                                                                             |
| `cherkasy_oblast_chornobai`                | [Чорнобай](https://t.me/AerisRimor/66096); [Чорнобаю](https://t.me/AerisRimor/82052)                              |
| `cherkasy_oblast_chyhyryn`                 | [Чигирин](https://t.me/AerisRimor/86520)                                                                          |
| `cherkasy_oblast_drabiv`                   | [Драбів](https://t.me/AerisRimor/81697)                                                                           |
| `cherkasy_oblast_helmiaziv`                | [Гельмязів](https://t.me/AerisRimor/68933); [Гельмязова](https://t.me/AerisRimor/87084)                           |
| `cherkasy_oblast_horodyshche`              | [городище](https://t.me/kyiv_airdef/58933); [Городища](https://t.me/AerisRimor/66605)                             |
| `cherkasy_oblast_irdyn`                    | [Ірдинь](https://t.me/war_monitor/45089)                                                                          |
| `cherkasy_oblast_irkliiv`                  | [Іркліїв](https://t.me/AerisRimor/70032)                                                                          |
| `cherkasy_oblast_kalynopil`                | [Калинопіль](https://t.me/kpszsu/69835); [Калинополя](https://t.me/AerisRimor/80465)                              |
| `cherkasy_oblast_kamianka`                 | [Кам'янка](https://t.me/AerisRimor/65065); [Камʼянка](https://t.me/AerisRimor/83847)                              |
| `cherkasy_oblast_kaniv`                    | [Канів](https://t.me/AerisRimor/76502)                                                                            |
| `cherkasy_oblast_korsun_shevchenkivskyi`   | [Корсунь-Шевченківський](https://t.me/AerisRimor/66650); [Корсунь Шевченківський](https://t.me/kyiv_airdef/55686) |
| `cherkasy_oblast_lysianka`                 | [Лисянка](https://t.me/AerisRimor/68940)                                                                          |
| `cherkasy_oblast_monastyryshche`           | [Монастирище](https://t.me/AerisRimor/77514); [Монастирища](https://t.me/kpszsu/65850)                            |
| `cherkasy_oblast_moshny`                   | [Мошни](https://t.me/AerisRimor/80455)                                                                            |
| `cherkasy_oblast_shpola`                   | [Шпола](https://t.me/AerisRimor/86380)                                                                            |
| `cherkasy_oblast_smila`                    | [сміла](https://t.me/kyiv_airdef/33512)                                                                           |
| `cherkasy_oblast_talne`                    | [Тальне](https://t.me/AerisRimor/77491)                                                                           |
| `cherkasy_oblast_trakhtemyriv`             | [Трахтемирів](https://t.me/kyiv_airdef/59493); [Трахтемирова](https://t.me/AerisRimor/78543)                      |
| `cherkasy_oblast_tsvitkove`                | [Цвіткове](https://t.me/AerisRimor/66633); [Цвіткового](https://t.me/kpszsu/62584)                                |
| `cherkasy_oblast_tsybuliv`                 | [Цибулів](https://t.me/AerisRimor/65760)                                                                          |
| `cherkasy_oblast_uman`                     | [умань](https://t.me/kyiv_airdef/44141)                                                                           |
| `cherkasy_oblast_vilshana`                 | [Вільшана](https://t.me/AerisRimor/69448); [Вільшани](https://t.me/war_monitor/41047)                             |
| `cherkasy_oblast_zhashkiv`                 | [Жашків](https://t.me/AerisRimor/77482)                                                                           |
| `cherkasy_oblast_zolotonosha`              | [Золотоноша](https://t.me/AerisRimor/70740); [Золотоношу](https://t.me/AerisRimor/76415)                          |
| `cherkasy_oblast_zvenyhorodka`             | [Звенигородка](https://t.me/AerisRimor/77468); [Звенигородку](https://t.me/AerisRimor/87858)                      |
| `chernihiv_oblast_bakhmach`                | [Бахмач](https://t.me/AerisRimor/77448)                                                                           |
| `chernihiv_oblast_baturyn`                 | [Батурин](https://t.me/AerisRimor/69388)                                                                          |
| `chernihiv_oblast_berezna`                 | [Березна](https://t.me/AerisRimor/73985)                                                                          |
| `chernihiv_oblast_bobrovytsia`             | [БОБРОВИЦЯ](https://t.me/kyiv_airdef/37826); [Бобровицю](https://t.me/kyiv_airdef/61398)                          |
| `chernihiv_oblast_borzna`                  | [Борзна](https://t.me/kyiv_airdef/41172)                                                                          |
| `chernihiv_oblast_desna`                   | [ДЕСНУ](https://t.me/kyiv_airdef/42322)                                                                           |
| `chernihiv_oblast_dihtiari`                | [Дігтярі](https://t.me/AerisRimor/71471)                                                                          |
| `chernihiv_oblast_dobrianka`               | [Добрянка](https://t.me/kyiv_airdef/43731); [Добрянку](https://t.me/AerisRimor/73677)                             |
| `chernihiv_oblast_honcharivske`            | [Гончарівське](https://t.me/kyiv_airdef/41592); [Гончарівського](https://t.me/kyiv_airdef/55978)                  |
| `chernihiv_oblast_horodnia`                | [Городня](https://t.me/AerisRimor/85155)                                                                          |
| `chernihiv_oblast_ichnia`                  | [ічня](https://t.me/kyiv_airdef/37705)                                                                            |
| `chernihiv_oblast_kholmy`                  | [Холми](https://t.me/AerisRimor/79671)                                                                            |
| `chernihiv_oblast_kipti`                   | [Кіпті](https://t.me/kyiv_airdef/41809)                                                                           |
| `chernihiv_oblast_koriukivka`              | [Корюківка](https://t.me/AerisRimor/79675); [Корюківку](https://t.me/kyiv_airdef/56175)                           |
| `chernihiv_oblast_korop`                   | [Короп](https://t.me/AerisRimor/72805)                                                                            |
| `chernihiv_oblast_kozelets`                | [Козелець](https://t.me/kyiv_airdef/58418); [Козельця](https://t.me/AerisRimor/78116)                             |
| `chernihiv_oblast_kulykivka`               | [Куликівка](https://t.me/AerisRimor/81452); [Куликівку](https://t.me/AerisRimor/72806)                            |
| `chernihiv_oblast_ladan`                   | [Ладан](https://t.me/kyiv_airdef/43644)                                                                           |
| `chernihiv_oblast_lebedyn`                 | [Лебедин](https://t.me/kyiv_airdef/58836)                                                                         |
| `chernihiv_oblast_liubech`                 | [Любеч](https://t.me/kyiv_airdef/44811)                                                                           |
| `chernihiv_oblast_losynivka`               | [Лосинівка](https://t.me/AerisRimor/65698); [Лосинівку](https://t.me/AerisRimor/79935)                            |
| `chernihiv_oblast_lynovytsia`              | [Линовиця](https://t.me/AerisRimor/64863); [Линовицю](https://t.me/kpszsu/64310)                                  |
| `chernihiv_oblast_makoshyne`               | [Макошине](https://t.me/AerisRimor/87990); [Макошиного](https://t.me/kpszsu/72604)                                |
| `chernihiv_oblast_mala_divytsia`           | [Мала Дівиця](https://t.me/AerisRimor/72480); [Малу Дівицю](https://t.me/kyiv_airdef/48746)                       |
| `chernihiv_oblast_mena`                    | [Мена](https://t.me/AerisRimor/73986)                                                                             |
| `chernihiv_oblast_mryn`                    | [Мрин](https://t.me/kyiv_airdef/55876)                                                                            |
| `chernihiv_oblast_nizhyn`                  | [Ніжин](https://t.me/AerisRimor/72487)                                                                            |
| `chernihiv_oblast_nosivka`                 | [Носівка](https://t.me/kyiv_airdef/39578)                                                                         |
| `chernihiv_oblast_nova_basan`              | [Нова Басань](https://t.me/AerisRimor/84155); [Нову Басань](https://t.me/AerisRimor/81115)                        |
| `chernihiv_oblast_novhorod_siverskyy`      | [Новгород-Сіверський](https://t.me/AerisRimor/65503); [Новгород-Сіверського](https://t.me/kpszsu/66365)           |
| `chernihiv_oblast_olyshivka`               | [Олишівка](https://t.me/kyiv_airdef/37290); [Олишівку](https://t.me/AerisRimor/83742)                             |
| `chernihiv_oblast_oster`                   | [ОСТЕР](https://t.me/kyiv_airdef/31476)                                                                           |
| `chernihiv_oblast_parafiivka`              | [Парафіївка](https://t.me/AerisRimor/65417); [Парафіївку](https://t.me/AerisRimor/84352)                          |
| `chernihiv_oblast_peremoha`                | [Перемогу](https://t.me/kyiv_airdef/58902)                                                                        |
| `chernihiv_oblast_pryluky`                 | [Прилуки](https://t.me/AerisRimor/77953)                                                                          |
| `chernihiv_oblast_ripky`                   | [Ріпки](https://t.me/kyiv_airdef/65545)                                                                           |
| `chernihiv_oblast_sedniv`                  | [Седнів](https://t.me/AerisRimor/86915)                                                                           |
| `chernihiv_oblast_shestovytsia`            | [Шестовиця](https://t.me/AerisRimor/69055)                                                                        |
| `chernihiv_oblast_snovsk`                  | [Сновськ](https://t.me/AerisRimor/72162)                                                                          |
| `chernihiv_oblast_sorokoshychi`            | [Сорокошичі](https://t.me/kyiv_airdef/63511)                                                                      |
| `chernihiv_oblast_sosnytsia`               | [Сосниця](https://t.me/AerisRimor/79752)                                                                          |
| `chernihiv_oblast_sribne`                  | [Срібне](https://t.me/AerisRimor/80176)                                                                           |
| `chernihiv_oblast_talalaivka`              | [Талалаївка](https://t.me/AerisRimor/71096); [Талалаївку](https://t.me/AerisRimor/72685)                          |
| `chernihiv_oblast_varva`                   | [Варва](https://t.me/kyiv_airdef/43644)                                                                           |
| `chernivtsi_oblast_khotyn`                 | [Хотин](https://t.me/operinform/51553)                                                                            |
| `chernivtsi_oblast_kitsman`                | [Кіцмань](https://t.me/AerisRimor/70265)                                                                          |
| `chernivtsi_oblast_novodnistrovsk`         | [Новодністровськ](https://t.me/war_monitor/45807); [Новодністровська](https://t.me/war_monitor/38608)             |
| `dnipropetrovsk_oblast_apostolove`         | [Апостолове](https://t.me/AerisRimor/67315); [Апостолового](https://t.me/kpszsu/65598)                            |
| `dnipropetrovsk_oblast_aviatorske`         | [Авіаторське](https://t.me/AerisRimor/67463); [Авіаторського](https://t.me/AerisRimor/67739)                      |
| `dnipropetrovsk_oblast_bozhedarivka`       | [Божедарівка](https://t.me/AerisRimor/64732); [Божедарівку](https://t.me/AerisRimor/77616)                        |
| `dnipropetrovsk_oblast_chaplyne`           | [Чаплине](https://t.me/kpszsu/62323)                                                                              |
| `dnipropetrovsk_oblast_cherkaske`          | [Черкаське](https://t.me/kpszsu/61536); [Черкаського](https://t.me/war_monitor/40082)                             |
| `dnipropetrovsk_oblast_dorohe`             | [Дороге](https://t.me/AerisRimor/67499)                                                                           |
| `dnipropetrovsk_oblast_doslidne`           | [Дослідне](https://t.me/AerisRimor/86707)                                                                         |
| `dnipropetrovsk_oblast_hirnytske`          | [Гірницьке](https://t.me/kpszsu/61251)                                                                            |
| `dnipropetrovsk_oblast_hubynykha`          | [Губиниха](https://t.me/AerisRimor/71603); [Губиниху](https://t.me/kpszsu/81052)                                  |
| `dnipropetrovsk_oblast_karnaukhivka`       | [Карнаухівка](https://t.me/AerisRimor/67725); [Карнаухівки](https://t.me/kpszsu/65413)                            |
| `dnipropetrovsk_oblast_krynychky`          | [Кринички](https://t.me/AerisRimor/77107); [Криничок](https://t.me/AerisRimor/79234)                              |
| `dnipropetrovsk_oblast_kurylivka`          | [Курилівка](https://t.me/AerisRimor/70007); [Курилівку](https://t.me/AerisRimor/86069)                            |
| `dnipropetrovsk_oblast_lykhivka`           | [Лихівка](https://t.me/AerisRimor/86675)                                                                          |
| `dnipropetrovsk_oblast_marhanets`          | [Марганець](https://t.me/kpszsu/73746); [Марганця](https://t.me/kpszsu/68566)                                     |
| `dnipropetrovsk_oblast_mezhova`            | [Межова](https://t.me/kpszsu/59591)                                                                               |
| `dnipropetrovsk_oblast_nikopol`            | [Нікополь](https://t.me/AerisRimor/77106); [Нікополя](https://t.me/AerisRimor/76623)                              |
| `dnipropetrovsk_oblast_obukhivka`          | [Обухівка](https://t.me/AerisRimor/71690); [Обухівку](https://t.me/AerisRimor/86051)                              |
| `dnipropetrovsk_oblast_pereshchepyne`      | [Перещепине](https://t.me/AerisRimor/83952); [Перещепиним](https://t.me/AerisRimor/77675)                         |
| `dnipropetrovsk_oblast_petropavlivka`      | [Петропавлівка](https://t.me/nebo_raketa/43824); [Петропавлівку](https://t.me/kyiv_airdef/49997)                  |
| `dnipropetrovsk_oblast_petrykivka`         | [Петриківка](https://t.me/AerisRimor/66683); [Петриківку](https://t.me/kpszsu/65582)                              |
| `dnipropetrovsk_oblast_pokrov`             | [Покров](https://t.me/AerisRimor/72343)                                                                           |
| `dnipropetrovsk_oblast_pokrovske`          | [Покровське](https://t.me/AerisRimor/79265); [Покровського](https://t.me/kpszsu/66852)                            |
| `dnipropetrovsk_oblast_prosiana`           | [Просяна](https://t.me/kpszsu/63910)                                                                              |
| `dnipropetrovsk_oblast_pysmenne`           | [Письменне](https://t.me/AerisRimor/70317); [Письменного](https://t.me/kpszsu/62931)                              |
| `dnipropetrovsk_oblast_radushne`           | [Радушне](https://t.me/operinform/55325)                                                                          |
| `dnipropetrovsk_oblast_samar`              | [самар](https://t.me/kyiv_airdef/45715)                                                                           |
| `dnipropetrovsk_oblast_shakhtarske`        | [Шахтарське](https://t.me/kpszsu/65301)                                                                           |
| `dnipropetrovsk_oblast_shyroke`            | [Широке](https://t.me/AerisRimor/76786)                                                                           |
| `dnipropetrovsk_oblast_slavhorod`          | [Славгород](https://t.me/kpszsu/61311); [Славгорода](https://t.me/kpszsu/66196)                                   |
| `dnipropetrovsk_oblast_solone`             | [Солоне](https://t.me/AerisRimor/73724)                                                                           |
| `dnipropetrovsk_oblast_synelnykove`        | [Синельникове](https://t.me/AerisRimor/67245); [Синельникового](https://t.me/war_monitor/39100)                   |
| `dnipropetrovsk_oblast_ternivka`           | [Тернівка](https://t.me/AerisRimor/68958); [Тернівку](https://t.me/AerisRimor/72271)                              |
| `dnipropetrovsk_oblast_tsarychanka`        | [Царичанка](https://t.me/war_monitor/43081); [Царичанку](https://t.me/AerisRimor/82742)                           |
| `dnipropetrovsk_oblast_vasylkivka`         | [Васильківка](https://t.me/AerisRimor/65199); [Васильківку](https://t.me/kpszsu/67951)                            |
| `dnipropetrovsk_oblast_verkhivtseve`       | [Верхівцеве](https://t.me/kpszsu/68935); [Верхівцевого](https://t.me/kpszsu/65405)                                |
| `dnipropetrovsk_oblast_verkhnodniprovsk`   | [Верхньодніпровськ](https://t.me/AerisRimor/68729); [Верхньодніпровська](https://t.me/kpszsu/77604)               |
| `dnipropetrovsk_oblast_vilnohirsk`         | [Вільногірськ](https://t.me/AerisRimor/70260); [Вільногірська](https://t.me/kpszsu/70893)                         |
| `dnipropetrovsk_oblast_yurivka`            | [Юр'ївка](https://t.me/AerisRimor/82711)                                                                          |
| `dnipropetrovsk_oblast_zelenodolsk`        | [Зеленодольськ](https://t.me/AerisRimor/72365); [Зеленодольська](https://t.me/kpszsu/65038)                       |
| `dnipropetrovsk_oblast_zhovti_vody`        | [Жовті Води](https://t.me/AerisRimor/68960); [Жовтих Вод](https://t.me/AerisRimor/74152)                          |
| `donetsk_oblast_dobropillia`               | [Добропілля](https://t.me/kpszsu/71513)                                                                           |
| `donetsk_oblast_kramatorsk`                | [Краматорськ](https://t.me/kpszsu/76877); [Краматорська](https://t.me/kpszsu/62208)                               |
| `donetsk_oblast_novodonetske`              | [Новодонецьке](https://t.me/kpszsu/65263); [Новодонецького](https://t.me/kpszsu/71300)                            |
| `ivano_frankivsk_oblast_burshtyn`          | [Бурштин](https://t.me/kpszsu/70725)                                                                              |
| `ivano_frankivsk_oblast_kalush`            | [Калуш](https://t.me/AerisRimor/77595)                                                                            |
| `ivano_frankivsk_oblast_kolomyia`          | [Коломия](https://t.me/AerisRimor/69097)                                                                          |
| `ivano_frankivsk_oblast_rohatyn`           | [Рогатин](https://t.me/AerisRimor/65548)                                                                          |
| `kharkiv_oblast_andriivka`                 | [Андріївка](https://t.me/kyiv_airdef/68131); [Андріївку](https://t.me/kyiv_airdef/58837)                          |
| `kharkiv_oblast_barvinkove`                | [Барвінкове](https://t.me/AerisRimor/84428)                                                                       |
| `kharkiv_oblast_berestyn`                  | [Берестин](https://t.me/AerisRimor/82714); [Берестина](https://t.me/AerisRimor/73686)                             |
| `kharkiv_oblast_bezliudivka`               | [Безлюдівка](https://t.me/AerisRimor/71327); [Безлюдівку](https://t.me/kpszsu/72122)                              |
| `kharkiv_oblast_blyzniuky`                 | [Близнюки](https://t.me/kpszsu/71548); [Близнюків](https://t.me/kpszsu/67815)                                     |
| `kharkiv_oblast_chuhuiv`                   | [Чугуїв](https://t.me/kyiv_airdef/32324)                                                                          |
| `kharkiv_oblast_derhachi`                  | [Дергачі](https://t.me/AerisRimor/74483)                                                                          |
| `kharkiv_oblast_donets`                    | [Донець](https://t.me/kpszsu/63261)                                                                               |
| `kharkiv_oblast_huty`                      | [Гути](https://t.me/AerisRimor/77204)                                                                             |
| `kharkiv_oblast_izium`                     | [Ізюм](https://t.me/AerisRimor/72632)                                                                             |
| `kharkiv_oblast_kehychivka`                | [Кегичівка](https://t.me/AerisRimor/86060); [Кегичівки](https://t.me/kpszsu/74191)                                |
| `kharkiv_oblast_kolomak`                   | [Коломак](https://t.me/AerisRimor/83548)                                                                          |
| `kharkiv_oblast_koviahy`                   | [Ковʼяги](https://t.me/AerisRimor/77362)                                                                          |
| `kharkiv_oblast_krasnokutsk`               | [Краснокутськ](https://t.me/AerisRimor/77360); [Краснокутська](https://t.me/kpszsu/59617)                         |
| `kharkiv_oblast_krasnopavlivka`            | [Краснопавлівка](https://t.me/operinform/56094); [Краснопавлівку](https://t.me/kpszsu/73374)                      |
| `kharkiv_oblast_liubotyn`                  | [Люботин](https://t.me/kpszsu/70392)                                                                              |
| `kharkiv_oblast_lozova`                    | [Лозова](https://t.me/AerisRimor/76114)                                                                           |
| `kharkiv_oblast_mala_danylivka`            | [Мала Данилівка](https://t.me/AerisRimor/74080); [Малу Данилівку](https://t.me/kpszsu/65585)                      |
| `kharkiv_oblast_merefa`                    | [Мерефа](https://t.me/AerisRimor/71870)                                                                           |
| `kharkiv_oblast_nova_vodolaha`             | [Нова Водолага](https://t.me/kpszsu/71148); [Нову Водолагу](https://t.me/kpszsu/74592)                            |
| `kharkiv_oblast_pechenihy`                 | [Печеніги](https://t.me/AerisRimor/79201); [Печенігів](https://t.me/kpszsu/66226)                                 |
| `kharkiv_oblast_peresichne`                | [Пересічне](https://t.me/AerisRimor/77745)                                                                        |
| `kharkiv_oblast_pisochyn`                  | [Пісочин](https://t.me/AerisRimor/73235)                                                                          |
| `kharkiv_oblast_prolisne`                  | [Пролісне](https://t.me/kpszsu/80616); [Пролісного](https://t.me/kpszsu/69745)                                    |
| `kharkiv_oblast_prykolotne`                | [Приколотне](https://t.me/kpszsu/59771)                                                                           |
| `kharkiv_oblast_rohan`                     | [Рогань](https://t.me/AerisRimor/69959)                                                                           |
| `kharkiv_oblast_sakhnovshchyna`            | [Сахновщина](https://t.me/AerisRimor/65672); [Сахновщини](https://t.me/AerisRimor/66419)                          |
| `kharkiv_oblast_savyntsi`                  | [Савинці](https://t.me/kpszsu/80300)                                                                              |
| `kharkiv_oblast_sharivka`                  | [Шарівка](https://t.me/kpszsu/61246)                                                                              |
| `kharkiv_oblast_shevchenkove`              | [Шевченкове](https://t.me/kyiv_airdef/47502)                                                                      |
| `kharkiv_oblast_slatyne`                   | [Слатине](https://t.me/kpszsu/68531)                                                                              |
| `kharkiv_oblast_slobozhanske`              | [Слобожанське](https://t.me/AerisRimor/66780); [Слобожанським](https://t.me/AerisRimor/67302)                     |
| `kharkiv_oblast_staryi_merchyk`            | [Старий Мерчик](https://t.me/kpszsu/66595); [Старого Мерчика](https://t.me/kpszsu/67818)                          |
| `kharkiv_oblast_staryy_saltiv`             | [Старий Салтів](https://t.me/AerisRimor/83681); [Старого Салтова](https://t.me/kpszsu/74148)                      |
| `kharkiv_oblast_valky`                     | [Валки](https://t.me/AerisRimor/87168)                                                                            |
| `kharkiv_oblast_vasyshcheve`               | [Васищеве](https://t.me/kpszsu/66094)                                                                             |
| `kharkiv_oblast_velykyi_burluk`            | [Великий Бурлук](https://t.me/kpszsu/69243); [Великого Бурлука](https://t.me/kpszsu/69747)                        |
| `kharkiv_oblast_vilshany`                  | [Вільшани](https://t.me/war_monitor/41047); [Вільшан](https://t.me/kpszsu/72730)                                  |
| `kharkiv_oblast_vysokyi`                   | [Високий](https://t.me/AerisRimor/72107)                                                                          |
| `kharkiv_oblast_zlatopil`                  | [Златопіль](https://t.me/AerisRimor/83812)                                                                        |
| `kharkiv_oblast_zmiiv`                     | [Зміїв](https://t.me/AerisRimor/83214)                                                                            |
| `kharkiv_oblast_zolochiv`                  | [Золочів](https://t.me/AerisRimor/72338)                                                                          |
| `kherson_oblast_arkhanhelske`              | [Архангельське](https://t.me/kpszsu/77866); [Архангельського](https://t.me/kpszsu/74232)                          |
| `kherson_oblast_beryslav`                  | [Берислав](https://t.me/kpszsu/70621); [Берислава](https://t.me/AerisRimor/81796)                                 |
| `kherson_oblast_stanislav`                 | [Станіслав](https://t.me/AerisRimor/81649); [Станіслава](https://t.me/AerisRimor/80614)                           |
| `kherson_oblast_vysokopillia`              | [Високопілля](https://t.me/kpszsu/70622)                                                                          |
| `khmelnytskyi_oblast_dunaivtsi`            | [Дунаївці](https://t.me/AerisRimor/65067); [Дунаївців](https://t.me/operinform/55361)                             |
| `khmelnytskyi_oblast_iziaslav`             | [Ізяслав](https://t.me/AerisRimor/77523)                                                                          |
| `khmelnytskyi_oblast_krasyliv`             | [Красилів](https://t.me/AerisRimor/81143); [Красилова](https://t.me/AerisRimor/77528)                             |
| `khmelnytskyi_oblast_letychiv`             | [Летичів](https://t.me/AerisRimor/65097)                                                                          |
| `khmelnytskyi_oblast_netishyn`             | [Нетішин](https://t.me/AerisRimor/69196)                                                                          |
| `khmelnytskyi_oblast_nova_ushytsia`        | [Нова Ушиця](https://t.me/AerisRimor/77525)                                                                       |
| `khmelnytskyi_oblast_sataniv`              | [Сатанів](https://t.me/AerisRimor/65405)                                                                          |
| `khmelnytskyi_oblast_shepetivka`           | [Шепетівка](https://t.me/AerisRimor/77518); [Шепетівку](https://t.me/kpszsu/76612)                                |
| `khmelnytskyi_oblast_slavuta`              | [Славута](https://t.me/nebo_raketa/38332)                                                                         |
| `khmelnytskyi_oblast_smotrych`             | [Смотрич](https://t.me/AerisRimor/65395)                                                                          |
| `khmelnytskyi_oblast_stara_syniava`        | [Стара Синява](https://t.me/AerisRimor/65372); [Стару Синяву](https://t.me/kpszsu/59027)                          |
| `khmelnytskyi_oblast_stara_ushytsia`       | [Стара Ушиця](https://t.me/AerisRimor/87208)                                                                      |
| `khmelnytskyi_oblast_starokostiantyniv`    | [Старокостянтинів](https://t.me/kpszsu/61647); [Старкон](https://t.me/AerisRimor/73291)                           |
| `khmelnytskyi_oblast_vinkivtsi`            | [Віньківці](https://t.me/war_monitor/45806); [Віньківців](https://t.me/AerisRimor/65479)                          |
| `khmelnytskyi_oblast_volochysk`            | [Волочиськ](https://t.me/AerisRimor/87239)                                                                        |
| `khmelnytskyi_oblast_vovkovyntsi`          | [Вовковинці](https://t.me/AerisRimor/69040)                                                                       |
| `khmelnytskyi_oblast_yarmolyntsi`          | [Ярмолинці](https://t.me/AerisRimor/77560)                                                                        |
| `khmelnytskyi_oblast_zakupne`              | [Закупне](https://t.me/AerisRimor/65405)                                                                          |
| `kirovohrad_oblast_adzhamka`               | [Аджамка](https://t.me/AerisRimor/86061)                                                                          |
| `kirovohrad_oblast_blahovishchenske`       | [Благовіщенське](https://t.me/AerisRimor/65352)                                                                   |
| `kirovohrad_oblast_bobrynets`              | [Бобринець](https://t.me/AerisRimor/71067); [Бобринця](https://t.me/AerisRimor/66375)                             |
| `kirovohrad_oblast_dolynska`               | [Долинська](https://t.me/AerisRimor/66666); [Долинську](https://t.me/AerisRimor/70166)                            |
| `kirovohrad_oblast_haivoron`               | [Гайворон](https://t.me/AerisRimor/66585); [Гайворона](https://t.me/AerisRimor/69030)                             |
| `kirovohrad_oblast_holovanivsk`            | [Голованівськ](https://t.me/AerisRimor/83758)                                                                     |
| `kirovohrad_oblast_kamianets`              | [Камʼянець](https://t.me/kyiv_airdef/43210); [Кам'янець](https://t.me/kpszsu/65185)                               |
| `kirovohrad_oblast_khmelove`               | [Хмельове](https://t.me/kpszsu/59016); [Хмельового](https://t.me/kpszsu/70865)                                    |
| `kirovohrad_oblast_kompaniivka`            | [Компаніївка](https://t.me/AerisRimor/79277); [Компаніївку](https://t.me/AerisRimor/70599)                        |
| `kirovohrad_oblast_lisove`                 | [Лісове](https://t.me/AerisRimor/83785)                                                                           |
| `kirovohrad_oblast_mala_vyska`             | [Мала Виска](https://t.me/AerisRimor/77803); [Малу Виску](https://t.me/AerisRimor/83691)                          |
| `kirovohrad_oblast_nova_praha`             | [Нова Прага](https://t.me/AerisRimor/83781); [Нову Прагу](https://t.me/AerisRimor/83091)                          |
| `kirovohrad_oblast_novoarkhanhelsk`        | [Новоархангельськ](https://t.me/AerisRimor/65024); [Новоархангельська](https://t.me/kpszsu/59247)                 |
| `kirovohrad_oblast_novomyrhorod`           | [Новомиргород](https://t.me/AerisRimor/80231); [Новомиргорода](https://t.me/kpszsu/78537)                         |
| `kirovohrad_oblast_novoukrainka`           | [Новоукраїнка](https://t.me/AerisRimor/80053); [Новоукраїнку](https://t.me/AerisRimor/86128)                      |
| `kirovohrad_oblast_oleksandriia`           | [Олександрія](https://t.me/AerisRimor/86524); [Олександрію](https://t.me/AerisRimor/71475)                        |
| `kirovohrad_oblast_oleksandriiske`         | [Олександрійське](https://t.me/AerisRimor/88380); [Олександрійського](https://t.me/AerisRimor/65115)              |
| `kirovohrad_oblast_onufriivka`             | [Онуфріївка](https://t.me/AerisRimor/69527); [Онуфріївку](https://t.me/AerisRimor/85383)                          |
| `kirovohrad_oblast_pantaivka`              | [Пантаївка](https://t.me/AerisRimor/83098); [Пантаївку](https://t.me/AerisRimor/85923)                            |
| `kirovohrad_oblast_pavlysh`                | [Павлиш](https://t.me/AerisRimor/83776)                                                                           |
| `kirovohrad_oblast_petrove`                | [Петрове](https://t.me/AerisRimor/83518)                                                                          |
| `kirovohrad_oblast_pomichna`               | [Помічна](https://t.me/AerisRimor/82074)                                                                          |
| `kirovohrad_oblast_smoline`                | [Смоліне](https://t.me/AerisRimor/82067)                                                                          |
| `kirovohrad_oblast_sozonivka`              | [Созонівка](https://t.me/AerisRimor/86658); [Созонівку](https://t.me/AerisRimor/87024)                            |
| `kirovohrad_oblast_svitlovodsk`            | [Світловодськ](https://t.me/AerisRimor/87554); [Світловодськом](https://t.me/AerisRimor/79157)                    |
| `kirovohrad_oblast_tsybuleve`              | [Цибулеве](https://t.me/AerisRimor/80900)                                                                         |
| `kirovohrad_oblast_ustynivka`              | [Устинівка](https://t.me/AerisRimor/80050); [Устинівку](https://t.me/AerisRimor/83684)                            |
| `kirovohrad_oblast_velyka_vyska`           | [Велика Виска](https://t.me/AerisRimor/86072); [Велику Виску](https://t.me/AerisRimor/82063)                      |
| `kirovohrad_oblast_vilshanka`              | [Вільшанка](https://t.me/kyiv_airdef/68187); [Вільшанки](https://t.me/kyiv_airdef/61932)                          |
| `kyiv_antonov`                             | [Антонов](https://t.me/AerisRimor/68658)                                                                          |
| `kyiv_berezniaky`                          | [Березняки](https://t.me/AerisRimor/67263)                                                                        |
| `kyiv_berkovets`                           | [Берковець](https://t.me/AerisRimor/68645)                                                                        |
| `kyiv_bilychi`                             | [Біличі](https://t.me/AerisRimor/67402)                                                                           |
| `kyiv_borshchahivka`                       | [Борщагу](https://t.me/AerisRimor/68339)                                                                          |
| `kyiv_bortnychi`                           | [Бортничі](https://t.me/AerisRimor/66181)                                                                         |
| `kyiv_bykivnia`                            | [Биківні](https://t.me/AerisRimor/68508)                                                                          |
| `kyiv_center`                              | [центром](https://t.me/AerisRimor/64676)                                                                          |
| `kyiv_chokolivka`                          | [Чоколівка](https://t.me/AerisRimor/66105)                                                                        |
| `kyiv_comfort_town`                        | [Комфорт Таун](https://t.me/nebo_raketa/40090); [Комфорттаун](https://t.me/AerisRimor/82755)                      |
| `kyiv_demiivka`                            | [Деміївки](https://t.me/AerisRimor/67265)                                                                         |
| `kyiv_desnianskyi_district`                | [Деснянський район](https://t.me/nebo_raketa/36142); [Деснянському районі](https://t.me/nebo_raketa/36552)        |
| `kyiv_dniprovskyi_district`                | [Дніпровський район](https://t.me/AerisRimor/72724); [Дніпровському районі](https://t.me/war_monitor/40287)       |
| `kyiv_dorohzhychi`                         | [Дорогожичі](https://t.me/AerisRimor/87106)                                                                       |
| `kyiv_dvrz`                                | [ДВРЗ](https://t.me/AerisRimor/67095)                                                                             |
| `kyiv_faina_town`                          | [Файна Таун](https://t.me/smolii_ukraine/110941)                                                                  |
| `kyiv_feofaniia`                           | [ФЕОФАНІЯ](https://t.me/kyiv_airdef/32687); [Феофанію](https://t.me/kpszsu/80940)                                 |
| `kyiv_halahany`                            | [Галагани](https://t.me/AerisRimor/65013)                                                                         |
| `kyiv_hidropark`                           | [Гідропарком](https://t.me/AerisRimor/69376)                                                                      |
| `kyiv_holosiiv`                            | [Голос](https://t.me/AerisRimor/65378)                                                                            |
| `kyiv_ipodrom`                             | [Іподром](https://t.me/AerisRimor/64673)                                                                          |
| `kyiv_karavaievi_dachi`                    | [Кардачі](https://t.me/AerisRimor/66859)                                                                          |
| `kyiv_kharkivskyi_masyv`                   | [Харківський масив](https://t.me/AerisRimor/68360)                                                                |
| `kyiv_khutir`                              | [Червоний хутір](https://t.me/AerisRimor/65042)                                                                   |
| `kyiv_klov`                                | [Клов](https://t.me/AerisRimor/69723)                                                                             |
| `kyiv_koncha_zaspa`                        | [Заспа](https://t.me/AerisRimor/65376)                                                                            |
| `kyiv_korchuvate`                          | [Корчувате](https://t.me/kyiv_airdef/56506)                                                                       |
| `kyiv_kpi`                                 | [КПІ](https://t.me/AerisRimor/68655)                                                                              |
| `kyiv_kurenivka`                           | [Куренівка](https://t.me/AerisRimor/66864)                                                                        |
| `kyiv_left_bank`                           | [лівобережжя](https://t.me/AerisRimor/64999)                                                                      |
| `kyiv_lukianivka`                          | [Лук'янівку](https://t.me/AerisRimor/66861)                                                                       |
| `kyiv_lypky`                               | [Липки](https://t.me/AerisRimor/69723)                                                                            |
| `kyiv_muromets`                            | [муромець](https://t.me/kyiv_airdef/58869)                                                                        |
| `kyiv_mysholovka`                          | [Мишоловка](https://t.me/AerisRimor/66646)                                                                        |
| `kyiv_nova_zabudova`                       | [Нову Забудова](https://t.me/AerisRimor/69727)                                                                    |
| `kyiv_nyvky`                               | [Нивки](https://t.me/AerisRimor/65013)                                                                            |
| `kyiv_nyzhni_sady`                         | [Нижні Сади](https://t.me/AerisRimor/68397)                                                                       |
| `kyiv_oblast_babyntsi`                     | [Бабинці](https://t.me/kyiv_airdef/62420)                                                                         |
| `kyiv_oblast_bahryn`                       | [Багрин](https://t.me/kyiv_airdef/64061)                                                                          |
| `kyiv_oblast_barakhty`                     | [Барахти](https://t.me/kyiv_airdef/60760)                                                                         |
| `kyiv_oblast_baryshivka`                   | [Баришівка](https://t.me/kyiv_airdef/33527); [Баришівку](https://t.me/kyiv_airdef/31667)                          |
| `kyiv_oblast_berezan`                      | [Березань](https://t.me/kyiv_airdef/31668); [Березані](https://t.me/kyiv_airdef/44851)                            |
| `kyiv_oblast_bezpiatne`                    | [безпʼятне](https://t.me/kyiv_airdef/69311)                                                                       |
| `kyiv_oblast_blystavytsia`                 | [Блиставиця](https://t.me/kyiv_airdef/58779); [Блиставицю](https://t.me/kyiv_airdef/68646)                        |
| `kyiv_oblast_bobryk`                       | [Бобрик](https://t.me/kyiv_airdef/59758)                                                                          |
| `kyiv_oblast_bobrytsia`                    | [Бобриця](https://t.me/kyiv_airdef/31725)                                                                         |
| `kyiv_oblast_bodenky`                      | [Боденьки](https://t.me/kyiv_airdef/36506)                                                                        |
| `kyiv_oblast_bohuslav`                     | [Богуслав](https://t.me/kyiv_airdef/54831); [Богуслава](https://t.me/kyiv_airdef/32002)                           |
| `kyiv_oblast_borova`                       | [Борова](https://t.me/kyiv_airdef/36441)                                                                          |
| `kyiv_oblast_boyarka`                      | [Боярка](https://t.me/AerisRimor/84447)                                                                           |
| `kyiv_oblast_brovary`                      | [Бровари](https://t.me/AerisRimor/65331)                                                                          |
| `kyiv_oblast_bucha`                        | [Буча](https://t.me/AerisRimor/65134)                                                                             |
| `kyiv_oblast_buzova`                       | [Бузова](https://t.me/kyiv_airdef/60588)                                                                          |
| `kyiv_oblast_byshiv`                       | [Бишів](https://t.me/kyiv_airdef/33463)                                                                           |
| `kyiv_oblast_chabany`                      | [Чабани](https://t.me/AerisRimor/85596)                                                                           |
| `kyiv_oblast_chaiky`                       | [Чайками](https://t.me/AerisRimor/66099)                                                                          |
| `kyiv_oblast_chornobyl`                    | [Чорнобиль](https://t.me/kyiv_airdef/61383); [Чорнобиля](https://t.me/kyiv_airdef/52666)                          |
| `kyiv_oblast_dereviana`                    | [Деревʼяна](https://t.me/kyiv_airdef/50689); [Дерев’яна](https://t.me/kyiv_airdef/55478)                          |
| `kyiv_oblast_divychky`                     | [Дівички](https://t.me/AerisRimor/64954)                                                                          |
| `kyiv_oblast_doslidnytske`                 | [дослідницьке](https://t.me/kyiv_airdef/37437); [Дослідницького](https://t.me/AerisRimor/65120)                   |
| `kyiv_oblast_dudarkiv`                     | [Дударків](https://t.me/kyiv_airdef/32057); [Дударкова](https://t.me/kyiv_airdef/58839)                           |
| `kyiv_oblast_dymer`                        | [Димер](https://t.me/AerisRimor/64846)                                                                            |
| `kyiv_oblast_dytiatky`                     | [Дитятки](https://t.me/kyiv_airdef/46350)                                                                         |
| `kyiv_oblast_fastiv`                       | [Фастів](https://t.me/kyiv_airdef/34895)                                                                          |
| `kyiv_oblast_fenevychi`                    | [феневичі](https://t.me/kyiv_airdef/68118); [Феневичів](https://t.me/kyiv_airdef/67813)                           |
| `kyiv_oblast_fursy`                        | [Фурси](https://t.me/kyiv_airdef/43308)                                                                           |
| `kyiv_oblast_gatne`                        | [Гатне](https://t.me/AerisRimor/86865)                                                                            |
| `kyiv_oblast_hlibivka`                     | [Глібівка](https://t.me/AerisRimor/79617); [Глібівку](https://t.me/AerisRimor/82625)                              |
| `kyiv_oblast_hoholiv`                      | [Гоголів](https://t.me/AerisRimor/76658)                                                                          |
| `kyiv_oblast_hora`                         | [Гора](https://t.me/kyiv_airdef/35616)                                                                            |
| `kyiv_oblast_horenka`                      | [Горенка](https://t.me/AerisRimor/81218)                                                                          |
| `kyiv_oblast_horenychi`                    | [Гореничі](https://t.me/kyiv_airdef/37595)                                                                        |
| `kyiv_oblast_hostomel`                     | [Гостомель](https://t.me/AerisRimor/65132)                                                                        |
| `kyiv_oblast_hotianivka`                   | [Хотянівка](https://t.me/AerisRimor/67093)                                                                        |
| `kyiv_oblast_hrebinky`                     | [Гребінки](https://t.me/kyiv_airdef/31888); [Гребінками](https://t.me/AerisRimor/64959)                           |
| `kyiv_oblast_hvozdiv`                      | [гвоздів](https://t.me/kyiv_airdef/58617)                                                                         |
| `kyiv_oblast_kaharlyk`                     | [Кагарлик](https://t.me/kyiv_airdef/33480); [Кагарлика](https://t.me/AerisRimor/83333)                            |
| `kyiv_oblast_kalita`                       | [Калита](https://t.me/kyiv_airdef/33042)                                                                          |
| `kyiv_oblast_kapitanivka`                  | [Капітанівка](https://t.me/kyiv_airdef/65712); [Капітанівку](https://t.me/AerisRimor/83677)                       |
| `kyiv_oblast_khalepia`                     | [Халепʼя](https://t.me/kyiv_airdef/55003)                                                                         |
| `kyiv_oblast_khodosivka`                   | [Ходосівка](https://t.me/kyiv_airdef/31943); [Ходосівку](https://t.me/kyiv_airdef/40484)                          |
| `kyiv_oblast_khotiv`                       | [Хотів](https://t.me/kyiv_airdef/31708)                                                                           |
| `kyiv_oblast_khotsky`                      | [Хоцьки](https://t.me/kyiv_airdef/58035)                                                                          |
| `kyiv_oblast_klavdiievo_tarasove`          | [Клавдієво-Тарасове](https://t.me/kyiv_airdef/45752); [клавдієво тарасове](https://t.me/kyiv_airdef/58890)        |
| `kyiv_oblast_kobtsi`                       | [Кобці](https://t.me/kyiv_airdef/56370)                                                                           |
| `kyiv_oblast_kodaky`                       | [Кодаки](https://t.me/kyiv_airdef/61362)                                                                          |
| `kyiv_oblast_kodra`                        | [Кодра](https://t.me/kyiv_airdef/58718)                                                                           |
| `kyiv_oblast_kopachiv`                     | [Копачів](https://t.me/kyiv_airdef/56807)                                                                         |
| `kyiv_oblast_kopyliv`                      | [Копилів](https://t.me/nebo_raketa/43908)                                                                         |
| `kyiv_oblast_kotsiubynske`                 | [Коцюбинське](https://t.me/AerisRimor/69563)                                                                      |
| `kyiv_oblast_kovalyn`                      | [Ковалин](https://t.me/kyiv_airdef/59638)                                                                         |
| `kyiv_oblast_kozarovychi`                  | [козаровичі](https://t.me/kyiv_airdef/68163)                                                                      |
| `kyiv_oblast_kozhanka`                     | [Кожанка](https://t.me/AerisRimor/81401)                                                                          |
| `kyiv_oblast_krasiatychi`                  | [Красятичі](https://t.me/kyiv_airdef/62335); [Красятичів](https://t.me/kyiv_airdef/45313)                         |
| `kyiv_oblast_krasylivka`                   | [Красилівка](https://t.me/kyiv_airdef/46570); [Красилівкою](https://t.me/AerisRimor/79627)                        |
| `kyiv_oblast_kremenyshche`                 | [кременище](https://t.me/kyiv_airdef/58679)                                                                       |
| `kyiv_oblast_krenychi`                     | [Креничі](https://t.me/kyiv_airdef/57027)                                                                         |
| `kyiv_oblast_kruhlyk`                      | [круглик](https://t.me/kyiv_airdef/48289)                                                                         |
| `kyiv_oblast_kryachky`                     | [Крячки](https://t.me/kyiv_airdef/53084)                                                                          |
| `kyiv_oblast_kulibaba`                     | [кулібаба](https://t.me/kyiv_airdef/69309)                                                                        |
| `kyiv_oblast_kvitneve`                     | [Квітневе](https://t.me/kyiv_airdef/34600); [Квітневого](https://t.me/AerisRimor/79767)                           |
| `kyiv_oblast_kyiliv`                       | [Кийлів](https://t.me/kyiv_airdef/34279)                                                                          |
| `kyiv_oblast_lebedivka`                    | [Лебедівка](https://t.me/kyiv_airdef/36303); [Лебедівку](https://t.me/kyiv_airdef/33770)                          |
| `kyiv_oblast_lisnyky`                      | [Лісники](https://t.me/AerisRimor/87750)                                                                          |
| `kyiv_oblast_litky`                        | [Літки](https://t.me/kyiv_airdef/48780)                                                                           |
| `kyiv_oblast_litochky`                     | [Літочки](https://t.me/kyiv_airdef/38509)                                                                         |
| `kyiv_oblast_liubartsi`                    | [Любарці](https://t.me/kyiv_airdef/63103)                                                                         |
| `kyiv_oblast_lypovyi_skytok`               | [Липовий Скиток](https://t.me/kyiv_airdef/60523)                                                                  |
| `kyiv_oblast_maliutianka`                  | [Малютянка](https://t.me/kyiv_airdef/42752); [Малютянку](https://t.me/kyiv_airdef/64058)                          |
| `kyiv_oblast_markhalivka`                  | [Мархалівка](https://t.me/AerisRimor/88107); [Мархалівку](https://t.me/AerisRimor/86721)                          |
| `kyiv_oblast_mokrets`                      | [Мокрець](https://t.me/AerisRimor/83445)                                                                          |
| `kyiv_oblast_moshchun`                     | [Мощун](https://t.me/AerisRimor/87988)                                                                            |
| `kyiv_oblast_mriia`                        | [Мрія](https://t.me/kyiv_airdef/53655)                                                                            |
| `kyiv_oblast_myla`                         | [Мила](https://t.me/kyiv_airdef/49312)                                                                            |
| `kyiv_oblast_myronivka`                    | [Миронівка](https://t.me/kyiv_airdef/38005); [Миронівку](https://t.me/kyiv_airdef/46046)                          |
| `kyiv_oblast_mytnytsia`                    | [Митниця](https://t.me/kyiv_airdef/59820)                                                                         |
| `kyiv_oblast_nalyvaikivka`                 | [НАЛИВАЙКІВКА](https://t.me/kyiv_airdef/42399); [Наливайківку](https://t.me/kyiv_airdef/41728)                    |
| `kyiv_oblast_nehrashi`                     | [Неграші](https://t.me/kyiv_airdef/44542)                                                                         |
| `kyiv_oblast_nemishaieve`                  | [Немішаєве](https://t.me/kyiv_airdef/42096); [Немішаєво](https://t.me/nebo_raketa/44203)                          |
| `kyiv_oblast_neshcheriv`                   | [Нещерів](https://t.me/kyiv_airdef/64459)                                                                         |
| `kyiv_oblast_nove_zalissia`                | [нове залісся](https://t.me/kyiv_airdef/68548)                                                                    |
| `kyiv_oblast_novi_bezradychi`              | [Нові Безрадичі](https://t.me/kyiv_airdef/56729)                                                                  |
| `kyiv_oblast_novosilky`                    | [Новосілки](https://t.me/kyiv_airdef/33006)                                                                       |
| `kyiv_oblast_nyzhcha_dubechnia`            | [Нижча Дубечня](https://t.me/kyiv_airdef/51362); [Нижчу Дубечню](https://t.me/kyiv_airdef/34880)                  |
| `kyiv_oblast_obukhiv`                      | [Обухів](https://t.me/AerisRimor/64847)                                                                           |
| `kyiv_oblast_orane`                        | [Оране](https://t.me/kyiv_airdef/58710)                                                                           |
| `kyiv_oblast_ostriiky`                     | [Острійки](https://t.me/kyiv_airdef/62237)                                                                        |
| `kyiv_oblast_pereiaslav`                   | [Переяслав](https://t.me/kyiv_airdef/33465); [Переяслава](https://t.me/kyiv_airdef/42722)                         |
| `kyiv_oblast_petrivtsi`                    | [Петрівці](https://t.me/kyiv_airdef/33784); [Петрівців](https://t.me/AerisRimor/69817)                            |
| `kyiv_oblast_petropavlivska_borshchahivka` | [Петропавлівську Борщагівку](https://t.me/AerisRimor/81135)                                                       |
| `kyiv_oblast_pidhirtsi`                    | [Підгірці](https://t.me/kyiv_airdef/35725)                                                                        |
| `kyiv_oblast_piskivka`                     | [Пісківка](https://t.me/kyiv_airdef/32430); [Пісківку](https://t.me/kyiv_airdef/62582)                            |
| `kyiv_oblast_plyuty`                       | [Плюти](https://t.me/kyiv_airdef/50692)                                                                           |
| `kyiv_oblast_pohreby`                      | [Погреби](https://t.me/AerisRimor/66873)                                                                          |
| `kyiv_oblast_protsiv`                      | [Проців](https://t.me/kyiv_airdef/46809)                                                                          |
| `kyiv_oblast_prypiat`                      | [Припʼять](https://t.me/kyiv_airdef/41988); [Прип'ять](https://t.me/kpszsu/64432)                                 |
| `kyiv_oblast_pukhivka`                     | [Пухівка](https://t.me/kyiv_airdef/38638)                                                                         |
| `kyiv_oblast_rohoziv`                      | [Рогозів](https://t.me/AerisRimor/78555)                                                                          |
| `kyiv_oblast_rokytne`                      | [Рокитне](https://t.me/kyiv_airdef/31949)                                                                         |
| `kyiv_oblast_romanivka`                    | [Романівка](https://t.me/kyiv_airdef/49667); [Романівку](https://t.me/AerisRimor/83274)                           |
| `kyiv_oblast_romankiv`                     | [Романків](https://t.me/kyiv_airdef/43410)                                                                        |
| `kyiv_oblast_roslavychi`                   | [Рославичі](https://t.me/AerisRimor/82411)                                                                        |
| `kyiv_oblast_rovzhi`                       | [Ровжі](https://t.me/kyiv_airdef/48767)                                                                           |
| `kyiv_oblast_rozhivka`                     | [Рожівка](https://t.me/kyiv_airdef/32992)                                                                         |
| `kyiv_oblast_rozhny`                       | [Рожни](https://t.me/kyiv_airdef/34428)                                                                           |
| `kyiv_oblast_rusaniv`                      | [Русанів](https://t.me/kyiv_airdef/35707)                                                                         |
| `kyiv_oblast_rzhyshchiv`                   | [Ржищів](https://t.me/kyiv_airdef/33466)                                                                          |
| `kyiv_oblast_semypolky`                    | [Семиполки](https://t.me/kyiv_airdef/34607); [Семиполок](https://t.me/nebo_raketa/35346)                          |
| `kyiv_oblast_shchaslyve`                   | [ЩАСЛИВЕ](https://t.me/kyiv_airdef/41360)                                                                         |
| `kyiv_oblast_shkarivka`                    | [шкарівка](https://t.me/kyiv_airdef/68687); [Шкарівки](https://t.me/kyiv_airdef/43310)                            |
| `kyiv_oblast_shpytky`                      | [Шпитьки](https://t.me/kyiv_airdef/61216)                                                                         |
| `kyiv_oblast_skibyn`                       | [Скибин](https://t.me/kyiv_airdef/58234)                                                                          |
| `kyiv_oblast_skvyra`                       | [СКВИРА](https://t.me/kyiv_airdef/43204)                                                                          |
| `kyiv_oblast_staiky`                       | [Стайки](https://t.me/kyiv_airdef/58897)                                                                          |
| `kyiv_oblast_stare`                        | [Старе](https://t.me/kyiv_airdef/47480)                                                                           |
| `kyiv_oblast_stavyshche`                   | [Ставище](https://t.me/kyiv_airdef/35796)                                                                         |
| `kyiv_oblast_strakholissia`                | [Страхолісся](https://t.me/kyiv_airdef/39554)                                                                     |
| `kyiv_oblast_sukholuchchia`                | [Сухолуччя](https://t.me/kyiv_airdef/52450)                                                                       |
| `kyiv_oblast_sulymivka`                    | [Сулимівка](https://t.me/kyiv_airdef/58916); [Сулимівку](https://t.me/kyiv_airdef/55836)                          |
| `kyiv_oblast_suvid`                        | [Сувид](https://t.me/kyiv_airdef/41600)                                                                           |
| `kyiv_oblast_sviatopetrivske`              | [Святопетрівське](https://t.me/AerisRimor/82120); [Святопетрівського](https://t.me/AerisRimor/84918)              |
| `kyiv_oblast_svitilnia`                    | [Світильня](https://t.me/kyiv_airdef/60139); [Світильню](https://t.me/kyiv_airdef/45413)                          |
| `kyiv_oblast_tarashcha`                    | [Тараща](https://t.me/kyiv_airdef/37029)                                                                          |
| `kyiv_oblast_tarasivka`                    | [Тарасівка](https://t.me/kyiv_airdef/44929); [Тарасівку](https://t.me/kyiv_airdef/57969)                          |
| `kyiv_oblast_tatsenky`                     | [Таценки](https://t.me/kyiv_airdef/52839)                                                                         |
| `kyiv_oblast_terezyne`                     | [Терезине](https://t.me/kyiv_airdef/59232)                                                                        |
| `kyiv_oblast_tetiiv`                       | [Тетіїв](https://t.me/kyiv_airdef/54200)                                                                          |
| `kyiv_oblast_tolokun`                      | [Толокунь](https://t.me/kyiv_airdef/38406); [Толокуні](https://t.me/AerisRimor/82395)                             |
| `kyiv_oblast_trebukhiv`                    | [Требухів](https://t.me/kyiv_airdef/32899); [Требухова](https://t.me/AerisRimor/79843)                            |
| `kyiv_oblast_trushky`                      | [Трушки](https://t.me/AerisRimor/64925)                                                                           |
| `kyiv_oblast_trypillia`                    | [Трипілля](https://t.me/AerisRimor/76848); [Трипіллям](https://t.me/kyiv_airdef/60064)                            |
| `kyiv_oblast_ukrainka`                     | [Українки](https://t.me/AerisRimor/65633)                                                                         |
| `kyiv_oblast_uzyn`                         | [Узин](https://t.me/kyiv_airdef/31889)                                                                            |
| `kyiv_oblast_velyka_buhaivka`              | [Велика Бугаївка](https://t.me/kyiv_airdef/56825); [Велику Бугаївку](https://t.me/kyiv_airdef/56841)              |
| `kyiv_oblast_velyka_dymerka`               | [Велика Димерка](https://t.me/kyiv_airdef/33092); [Велику Димерку](https://t.me/kpszsu/80906)                     |
| `kyiv_oblast_velyki_dmytrovychi`           | [Великі Дмитровичі](https://t.me/kyiv_airdef/52844)                                                               |
| `kyiv_oblast_velykopolovetske`             | [Великополовецьке](https://t.me/AerisRimor/64888)                                                                 |
| `kyiv_oblast_velykyi_krupil`               | [Великий Крупіль](https://t.me/kyiv_airdef/59523)                                                                 |
| `kyiv_oblast_veremia`                      | [Веремʼя](https://t.me/kyiv_airdef/57347)                                                                         |
| `kyiv_oblast_volodarka`                    | [Володарка](https://t.me/kyiv_airdef/51705); [Володарки](https://t.me/kyiv_airdef/59704)                          |
| `kyiv_oblast_voronkiv`                     | [Вороньків](https://t.me/AerisRimor/88083)                                                                        |
| `kyiv_oblast_voropaiv`                     | [Воропаїв](https://t.me/kyiv_airdef/34879); [Воропаєва](https://t.me/kyiv_airdef/58822)                           |
| `kyiv_oblast_vorzel`                       | [Ворзель](https://t.me/AerisRimor/66098)                                                                          |
| `kyiv_oblast_vyshcha_dubechnia`            | [Вища Дубечня](https://t.me/kyiv_airdef/36512); [Вищу Дубечню](https://t.me/kyiv_airdef/39874)                    |
| `kyiv_oblast_vyshenky`                     | [Вишеньки](https://t.me/kyiv_airdef/32082); [Вишеньками](https://t.me/AerisRimor/70859)                           |
| `kyiv_oblast_vyshhorod`                    | [Вишгород](https://t.me/AerisRimor/65139)                                                                         |
| `kyiv_oblast_vytachiv`                     | [Витачів](https://t.me/kyiv_airdef/54256)                                                                         |
| `kyiv_oblast_yahotyn`                      | [Яготин](https://t.me/kyiv_airdef/35243)                                                                          |
| `kyiv_oblast_yasnohorodka`                 | [Ясногородка](https://t.me/AerisRimor/87614); [Ясногородки](https://t.me/kyiv_airdef/53470)                       |
| `kyiv_oblast_yatsky`                       | [Яцьки](https://t.me/kyiv_airdef/55842)                                                                           |
| `kyiv_oblast_yerkivtsi`                    | [Єрківці](https://t.me/kyiv_airdef/59637)                                                                         |
| `kyiv_oblast_yurivka`                      | [Юрівка](https://t.me/kyiv_airdef/57594)                                                                          |
| `kyiv_oblast_zalissia`                     | [залісся](https://t.me/kyiv_airdef/69064)                                                                         |
| `kyiv_oblast_zalizne`                      | [Залізне](https://t.me/kyiv_airdef/56801)                                                                         |
| `kyiv_oblast_zarichchia`                   | [заріччя](https://t.me/kyiv_airdef/68193)                                                                         |
| `kyiv_oblast_zavorychi`                    | [Заворичі](https://t.me/kyiv_airdef/44212); [Заворичів](https://t.me/kyiv_airdef/54747)                           |
| `kyiv_oblast_zelenyi_bir`                  | [Зелений Бір](https://t.me/kyiv_airdef/56863)                                                                     |
| `kyiv_oblast_zghurivka`                    | [Згурівка](https://t.me/kyiv_airdef/31637); [Згурівки](https://t.me/kyiv_airdef/38305)                            |
| `kyiv_oblast_zherebiatyn`                  | [Жеребʼятин](https://t.me/kyiv_airdef/67629); [Жереб'ятин](https://t.me/war_monitor/45325)                        |
| `kyiv_oblast_zhk_sofiia`                   | [ЖК Софія](https://t.me/AerisRimor/68340)                                                                         |
| `kyiv_oblast_zhukivtsi`                    | [Жуківці](https://t.me/kyiv_airdef/50688)                                                                         |
| `kyiv_oblast_zhukyn`                       | [Жукин](https://t.me/kyiv_airdef/33618)                                                                           |
| `kyiv_obolon`                              | [Оболонський](https://t.me/AerisRimor/65633)                                                                      |
| `kyiv_osokorky`                            | [Осокорками](https://t.me/AerisRimor/68408)                                                                       |
| `kyiv_pechersk`                            | [Печерський](https://t.me/AerisRimor/68953)                                                                       |
| `kyiv_pochaiana`                           | [Почайну](https://t.me/AerisRimor/66862)                                                                          |
| `kyiv_podil`                               | [Поділ](https://t.me/AerisRimor/65508)                                                                            |
| `kyiv_pozniaky`                            | [Позняки](https://t.me/AerisRimor/68409)                                                                          |
| `kyiv_priorka`                             | [Пріорка](https://t.me/AerisRimor/68643)                                                                          |
| `kyiv_pushcha_vodytsia`                    | [Пуща](https://t.me/AerisRimor/66102)                                                                             |
| `kyiv_pyrohiv`                             | [пирогів](https://t.me/kyiv_airdef/31958)                                                                         |
| `kyiv_rembaza`                             | [Рембаза](https://t.me/AerisRimor/67087)                                                                          |
| `kyiv_respublika`                          | [Республіку](https://t.me/AerisRimor/66856)                                                                       |
| `kyiv_retroville`                          | [Ретровіль](https://t.me/kyiv_airdef/48465); [Retroville](https://t.me/operinform/58276)                          |
| `kyiv_right_bank`                          | [правобережжі](https://t.me/AerisRimor/64962)                                                                     |
| `kyiv_rusanivka`                           | [Русанівка](https://t.me/AerisRimor/66886)                                                                        |
| `kyiv_rusanivski_sady`                     | [Русанівські сади](https://t.me/AerisRimor/68639)                                                                 |
| `kyiv_shevchenkivskyi_district`            | [Шевченківський район](https://t.me/kyiv_airdef/32162); [Шевченківському районі](https://t.me/nebo_raketa/37985)  |
| `kyiv_solomianka`                          | [Солом'янський](https://t.me/AerisRimor/65633)                                                                    |
| `kyiv_sotsmisto`                           | [Соцмісто](https://t.me/AerisRimor/86913); [Соцмістт](https://t.me/kyiv_airdef/36878)                             |
| `kyiv_sovky`                               | [Совки](https://t.me/AerisRimor/84845)                                                                            |
| `kyiv_syrets`                              | [Сирець](https://t.me/AerisRimor/66107)                                                                           |
| `kyiv_telychka`                            | [Теличка](https://t.me/AerisRimor/67266)                                                                          |
| `kyiv_teremky`                             | [Теремки](https://t.me/AerisRimor/65008)                                                                          |
| `kyiv_trukhaniv_island`                    | [Труханів острів](https://t.me/kyiv_airdef/34796); [Труханів](https://t.me/AerisRimor/86821)                      |
| `kyiv_varshavskyi`                         | [Варшавський масив](https://t.me/nebo_raketa/41817); [ЖК Варшавський](https://t.me/kyiv_airdef/62798)             |
| `kyiv_vita_lytovska`                       | [Віта-Литовська](https://t.me/AerisRimor/69308)                                                                   |
| `kyiv_vydubychi`                           | [Видубичі](https://t.me/AerisRimor/67264)                                                                         |
| `kyiv_zhuliany`                            | [Жуляни](https://t.me/AerisRimor/65907)                                                                           |
| `kyiv_zvirynets`                           | [Звіринець](https://t.me/AerisRimor/71568)                                                                        |
| `lviv_oblast_bibrka`                       | [Бібрка](https://t.me/AerisRimor/65548)                                                                           |
| `lviv_oblast_stryi`                        | [Стрий](https://t.me/AerisRimor/65555)                                                                            |
| `lviv_oblast_zhovkva`                      | [Жовква](https://t.me/operinform/52450)                                                                           |
| `lviv_oblast_zhydachiv`                    | [Жидачів](https://t.me/AerisRimor/65549)                                                                          |
| `mykolaiv_oblast_arbuzynka`                | [Арбузинка](https://t.me/AerisRimor/73683); [Арбузинку](https://t.me/kpszsu/78514)                                |
| `mykolaiv_oblast_bashtanka`                | [Баштанка](https://t.me/kpszsu/67445); [Баштанку](https://t.me/AerisRimor/78914)                                  |
| `mykolaiv_oblast_bereznehuvate`            | [Березнегувате](https://t.me/AerisRimor/75437); [Березнегуватого](https://t.me/kpszsu/66879)                      |
| `mykolaiv_oblast_bratske`                  | [Братське](https://t.me/AerisRimor/73683)                                                                         |
| `mykolaiv_oblast_kazanka`                  | [Казанка](https://t.me/AerisRimor/75438)                                                                          |
| `mykolaiv_oblast_kobleve`                  | [Коблеве](https://t.me/kpszsu/60009)                                                                              |
| `mykolaiv_oblast_kryve_ozero`              | [Криве Озеро](https://t.me/AerisRimor/86357)                                                                      |
| `mykolaiv_oblast_morske`                   | [Морське](https://t.me/kpszsu/71859)                                                                              |
| `mykolaiv_oblast_novyi_buh`                | [Новий Буг](https://t.me/kyiv_airdef/43270); [Нового Буга](https://t.me/AerisRimor/81614)                         |
| `mykolaiv_oblast_olshanske`                | [Ольшанське](https://t.me/kpszsu/60373)                                                                           |
| `mykolaiv_oblast_pervomaisk`               | [первомайськ](https://t.me/kyiv_airdef/32566); [Первомайська](https://t.me/AerisRimor/83034)                      |
| `mykolaiv_oblast_pivdennoukrainsk`         | [Південноукраїнськ](https://t.me/AerisRimor/68951); [Південноукраїнська](https://t.me/kpszsu/78645)               |
| `mykolaiv_oblast_rybakivka`                | [Рибаківка](https://t.me/AerisRimor/71762); [Рибаківку](https://t.me/AerisRimor/83026)                            |
| `mykolaiv_oblast_snigurivka`               | [Снігурівка](https://t.me/AerisRimor/80038); [Снігурівку](https://t.me/kpszsu/63517)                              |
| `mykolaiv_oblast_tokarivka`                | [Токарівка](https://t.me/AerisRimor/65716); [Токарівку](https://t.me/kpszsu/78686)                                |
| `mykolaiv_oblast_trykhaty`                 | [Трихати](https://t.me/AerisRimor/66940)                                                                          |
| `mykolaiv_oblast_veselynove`               | [Веселинове](https://t.me/AerisRimor/65716); [Веселинового](https://t.me/kpszsu/78538)                            |
| `mykolaiv_oblast_voskresenske`             | [Воскресенське](https://t.me/kpszsu/60886); [Воскресенського](https://t.me/kpszsu/80241)                          |
| `mykolaiv_oblast_voznesensk`               | [ВОЗНЕСЕНСЬК](https://t.me/AerisRimor/81623); [Вознесенська](https://t.me/AerisRimor/82706)                       |
| `mykolaiv_oblast_vozsiiatske`              | [Возсіятське](https://t.me/AerisRimor/77743)                                                                      |
| `mykolaiv_oblast_yelanets`                 | [Єланець](https://t.me/AerisRimor/79357)                                                                          |
| `odesa_oblast_altestove`                   | [Алтестове](https://t.me/war_monitor/45240)                                                                       |
| `odesa_oblast_ananiv`                      | [Ананьїв](https://t.me/AerisRimor/80472)                                                                          |
| `odesa_oblast_artsyz`                      | [Арциз](https://t.me/AerisRimor/77682)                                                                            |
| `odesa_oblast_avanhard`                    | [Авангард](https://t.me/AerisRimor/88126)                                                                         |
| `odesa_oblast_balta`                       | [Балта](https://t.me/AerisRimor/80472)                                                                            |
| `odesa_oblast_baraboi`                     | [Барабой](https://t.me/AerisRimor/67370)                                                                          |
| `odesa_oblast_berezivka`                   | [Березівка](https://t.me/AerisRimor/76510); [Березівки](https://t.me/AerisRimor/79138)                            |
| `odesa_oblast_biliaivka`                   | [Біляївка](https://t.me/AerisRimor/66159); [Біляївки](https://t.me/AerisRimor/72392)                              |
| `odesa_oblast_biliari`                     | [Білярі](https://t.me/war_monitor/38508)                                                                          |
| `odesa_oblast_bolhrad`                     | [Болград](https://t.me/kpszsu/59177)                                                                              |
| `odesa_oblast_buialyk`                     | [Буялик](https://t.me/AerisRimor/77388)                                                                           |
| `odesa_oblast_chornomorske`                | [Чорноморське](https://t.me/AerisRimor/86153)                                                                     |
| `odesa_oblast_dachne`                      | [Дачне](https://t.me/AerisRimor/73145)                                                                            |
| `odesa_oblast_dalnyk`                      | [Дальник](https://t.me/AerisRimor/77660)                                                                          |
| `odesa_oblast_dobroslav`                   | [Доброслав](https://t.me/AerisRimor/78444); [Доброслава](https://t.me/AerisRimor/80768)                           |
| `odesa_oblast_fontanka`                    | [Фонтанка](https://t.me/AerisRimor/65322); [Фонтанку](https://t.me/AerisRimor/65601)                              |
| `odesa_oblast_hrybivka`                    | [Грибівка](https://t.me/AerisRimor/85524); [Грибівки](https://t.me/kpszsu/70888)                                  |
| `odesa_oblast_hryhorivka`                  | [Григорівка](https://t.me/AerisRimor/75103); [Григорівку](https://t.me/AerisRimor/75140)                          |
| `odesa_oblast_ilichanka`                   | [Ілічанка](https://t.me/AerisRimor/64785)                                                                         |
| `odesa_oblast_ivanivka`                    | [Іванівка](https://t.me/AerisRimor/65617); [Іванівки](https://t.me/kpszsu/61564)                                  |
| `odesa_oblast_izmail`                      | [Ізмаїл](https://t.me/AerisRimor/66407)                                                                           |
| `odesa_oblast_katlabuh`                    | [Катлабуг](https://t.me/kpszsu/67984); [Катлабугу](https://t.me/kpszsu/76859)                                     |
| `odesa_oblast_kiliia`                      | [Кілія](https://t.me/AerisRimor/66352)                                                                            |
| `odesa_oblast_kosa`                        | [Косу](https://t.me/AerisRimor/77959)                                                                             |
| `odesa_oblast_kosy`                        | [Коси](https://t.me/AerisRimor/74967)                                                                             |
| `odesa_oblast_krasnosilka`                 | [Красносілка](https://t.me/AerisRimor/73035); [Красносілки](https://t.me/AerisRimor/65636)                        |
| `odesa_oblast_kurisove`                    | [Курісове](https://t.me/AerisRimor/76491)                                                                         |
| `odesa_oblast_kurortne`                    | [Курортне](https://t.me/war_monitor/43004); [Курортному](https://t.me/AerisRimor/73456)                           |
| `odesa_oblast_liubashivka`                 | [Любашівка](https://t.me/AerisRimor/80471); [Любашівку](https://t.me/AerisRimor/65724)                            |
| `odesa_oblast_lyman`                       | [Лиман](https://t.me/AerisRimor/75083)                                                                            |
| `odesa_oblast_lymanka`                     | [Лиманка](https://t.me/AerisRimor/74957)                                                                          |
| `odesa_oblast_malodolynske`                | [Малодолинське](https://t.me/AerisRimor/65311)                                                                    |
| `odesa_oblast_malyi_fontan`                | [Малий Фонтан](https://t.me/AerisRimor/65287)                                                                     |
| `odesa_oblast_mayaky`                      | [Маяки](https://t.me/AerisRimor/80515)                                                                            |
| `odesa_oblast_moldovanka`                  | [Молдованка](https://t.me/AerisRimor/75588)                                                                       |
| `odesa_oblast_nadlymanske`                 | [Надлиманське](https://t.me/AerisRimor/82537)                                                                     |
| `odesa_oblast_nova_dolyna`                 | [Нова Долина](https://t.me/AerisRimor/82536); [Нову Долину](https://t.me/AerisRimor/68601)                        |
| `odesa_oblast_oleksandrivka`               | [Олександрівка](https://t.me/kyiv_airdef/34369); [Олександрівки](https://t.me/kyiv_airdef/58304)                  |
| `odesa_oblast_orlivka`                     | [Орлівка](https://t.me/AerisRimor/67500)                                                                          |
| `odesa_oblast_pivdenne`                    | [Південне](https://t.me/AerisRimor/65193)                                                                         |
| `odesa_oblast_podilsk`                     | [Подільськ](https://t.me/operinform/52059); [Подільська](https://t.me/kpszsu/76938)                               |
| `odesa_oblast_prylymanske`                 | [Прилиманське](https://t.me/AerisRimor/82535)                                                                     |
| `odesa_oblast_prymorske`                   | [Приморське](https://t.me/AerisRimor/77330); [Приморського](https://t.me/AerisRimor/77357)                        |
| `odesa_oblast_reni`                        | [Рені](https://t.me/kpszsu/72563)                                                                                 |
| `odesa_oblast_rozdilna`                    | [Роздільна](https://t.me/war_monitor/45606); [Роздільної](https://t.me/AerisRimor/80671)                          |
| `odesa_oblast_sanzhiika`                   | [Санжійка](https://t.me/AerisRimor/68520); [Санжійки](https://t.me/AerisRimor/77172)                              |
| `odesa_oblast_sarata`                      | [Сарата](https://t.me/kpszsu/75644)                                                                               |
| `odesa_oblast_shabo`                       | [Шабо](https://t.me/AerisRimor/75090)                                                                             |
| `odesa_oblast_shyriaieve`                  | [Ширяєве](https://t.me/kpszsu/76591)                                                                              |
| `odesa_oblast_starokozache`                | [Старокозаче](https://t.me/AerisRimor/86080); [Старокозачого](https://t.me/kpszsu/72289)                          |
| `odesa_oblast_sukhyi_lyman`                | [Сухий Лиман](https://t.me/AerisRimor/67075)                                                                      |
| `odesa_oblast_tairove`                     | [Таїрове](https://t.me/AerisRimor/74992)                                                                          |
| `odesa_oblast_tatarbunary`                 | [Татарбунари](https://t.me/AerisRimor/76357); [Татарбунарів](https://t.me/kpszsu/65026)                           |
| `odesa_oblast_teplodar`                    | [Теплодар](https://t.me/AerisRimor/75109); [Теплодару](https://t.me/AerisRimor/87335)                             |
| `odesa_oblast_tuzly`                       | [Тузли](https://t.me/AerisRimor/78400)                                                                            |
| `odesa_oblast_usatove`                     | [Усатове](https://t.me/AerisRimor/86213)                                                                          |
| `odesa_oblast_velykodolynske`              | [Великодолинське](https://t.me/AerisRimor/66143); [Великодолинського](https://t.me/AerisRimor/85941)              |
| `odesa_oblast_velykyi_dalnyk`              | [Великий Дальник](https://t.me/AerisRimor/78652); [Великого Дальника](https://t.me/AerisRimor/72389)              |
| `odesa_oblast_vylkove`                     | [Вилкове](https://t.me/AerisRimor/77024)                                                                          |
| `poltava_oblast_bilyky`                    | [Білики](https://t.me/AerisRimor/64998)                                                                           |
| `poltava_oblast_chornukhy`                 | [Чорнухи](https://t.me/AerisRimor/88265)                                                                          |
| `poltava_oblast_chutove`                   | [Чутове](https://t.me/AerisRimor/83548)                                                                           |
| `poltava_oblast_dykanka`                   | [Диканька](https://t.me/AerisRimor/73094); [Диканьку](https://t.me/AerisRimor/86073)                              |
| `poltava_oblast_hadiach`                   | [Гадяч](https://t.me/kyiv_airdef/37361)                                                                           |
| `poltava_oblast_hlobyne`                   | [Глобине](https://t.me/AerisRimor/65050)                                                                          |
| `poltava_oblast_hoholeve`                  | [Гоголеве](https://t.me/AerisRimor/69221); [Гоголевого](https://t.me/kpszsu/63242)                                |
| `poltava_oblast_horishni_plavni`           | [Горішні Плавні](https://t.me/war_monitor/40957); [Горішніх Плавнів](https://t.me/AerisRimor/65612)               |
| `poltava_oblast_hradyzk`                   | [Градизьк](https://t.me/AerisRimor/83569); [Градизька](https://t.me/AerisRimor/85846)                             |
| `poltava_oblast_hrebinka`                  | [Гребінка](https://t.me/AerisRimor/87649); [Гребінки](https://t.me/kyiv_airdef/31888)                             |
| `poltava_oblast_karlivka`                  | [Карлівка](https://t.me/kpszsu/60276); [Карлівки](https://t.me/kpszsu/61427)                                      |
| `poltava_oblast_khorol`                    | [Хорол](https://t.me/AerisRimor/65325)                                                                            |
| `poltava_oblast_kobeliaky`                 | [Кобеляки](https://t.me/AerisRimor/86381)                                                                         |
| `poltava_oblast_komyshnia`                 | [Комишня](https://t.me/AerisRimor/71084)                                                                          |
| `poltava_oblast_kotelva`                   | [Котельва](https://t.me/AerisRimor/86709); [Котельву](https://t.me/AerisRimor/73087)                              |
| `poltava_oblast_kozelshchyna`              | [Козельщина](https://t.me/war_monitor/43642); [Козельщини](https://t.me/AerisRimor/70389)                         |
| `poltava_oblast_kremenchuk`                | [кременчук](https://t.me/kyiv_airdef/39826); [Кременчука](https://t.me/war_monitor/44296)                         |
| `poltava_oblast_lokhvytsia`                | [Лохвиця](https://t.me/AerisRimor/80888)                                                                          |
| `poltava_oblast_lubny`                     | [ЛУБНИ](https://t.me/kyiv_airdef/42375)                                                                           |
| `poltava_oblast_mashivka`                  | [Машівка](https://t.me/AerisRimor/83549)                                                                          |
| `poltava_oblast_myrhorod`                  | [МИРГОРОД](https://t.me/kyiv_airdef/42374); [Миргородом](https://t.me/AerisRimor/71235)                           |
| `poltava_oblast_novi_sanzhary`             | [Нові Санжари](https://t.me/AerisRimor/82055); [Нових Санжарів](https://t.me/kpszsu/76152)                        |
| `poltava_oblast_novoorzhytske`             | [Новооржицьке](https://t.me/AerisRimor/71086); [Новооржицького](https://t.me/kpszsu/69786)                        |
| `poltava_oblast_opishnia`                  | [Опішня](https://t.me/AerisRimor/78861)                                                                           |
| `poltava_oblast_pyriatyn`                  | [Пирятин](https://t.me/kyiv_airdef/50113)                                                                         |
| `poltava_oblast_reshetylivka`              | [Решетилівка](https://t.me/AerisRimor/72091); [Решетилівку](https://t.me/AerisRimor/83678)                        |
| `poltava_oblast_romodan`                   | [Ромодан](https://t.me/AerisRimor/68739)                                                                          |
| `poltava_oblast_shyshaky`                  | [Шишаки](https://t.me/AerisRimor/80644)                                                                           |
| `poltava_oblast_skorokhodove`              | [Скороходове](https://t.me/kpszsu/69998); [Скороходового](https://t.me/kpszsu/65098)                              |
| `poltava_oblast_velyka_bahachka`           | [Велика Багачка](https://t.me/AerisRimor/66400); [Великою Багачкою](https://t.me/AerisRimor/80577)                |
| `poltava_oblast_velyki_sorochyntsi`        | [Великі Сорочинці](https://t.me/war_monitor/38864); [Великих Сорочинців](https://t.me/kpszsu/80980)               |
| `poltava_oblast_vyrishalne`                | [Вирішальне](https://t.me/AerisRimor/68286); [вирішальному](https://t.me/AerisRimor/68770)                        |
| `poltava_oblast_zavodske`                  | [Заводське](https://t.me/AerisRimor/80888); [Заводського](https://t.me/AerisRimor/65086)                          |
| `poltava_oblast_zinkiv`                    | [Зіньків](https://t.me/AerisRimor/87179)                                                                          |
| `rivne_oblast_berezne`                     | [Березне](https://t.me/AerisRimor/87069)                                                                          |
| `rivne_oblast_dubno`                       | [Дубно](https://t.me/war_monitor/42051)                                                                           |
| `rivne_oblast_dubrovytsia`                 | [Дубровиця](https://t.me/operinform/53200); [Дубровицю](https://t.me/war_monitor/44501)                           |
| `rivne_oblast_hoshcha`                     | [Гоща](https://t.me/war_monitor/44439)                                                                            |
| `rivne_oblast_klevan`                      | [Клевань](https://t.me/AerisRimor/68246)                                                                          |
| `rivne_oblast_korets`                      | [Корець](https://t.me/AerisRimor/87260)                                                                           |
| `rivne_oblast_kostopil`                    | [Костопіль](https://t.me/AerisRimor/69149); [Костополя](https://t.me/AerisRimor/87016)                            |
| `rivne_oblast_mizoch`                      | [Мізоч](https://t.me/AerisRimor/87040)                                                                            |
| `rivne_oblast_sarny`                       | [Сарни](https://t.me/AerisRimor/69198)                                                                            |
| `rivne_oblast_stepan`                      | [Степань](https://t.me/war_monitor/45596)                                                                         |
| `rivne_oblast_tomashhorod`                 | [Томашгород](https://t.me/kpszsu/70064)                                                                           |
| `rivne_oblast_varash`                      | [Вараш](https://t.me/AerisRimor/87981)                                                                            |
| `rivne_oblast_zdolbuniv`                   | [Здолбунів](https://t.me/AerisRimor/69145)                                                                        |
| `sumy_oblast_bilopillia`                   | [Білопілля](https://t.me/AerisRimor/81632)                                                                        |
| `sumy_oblast_boromlia`                     | [Боромля](https://t.me/operinform/51647)                                                                          |
| `sumy_oblast_buryn`                        | [Буринь](https://t.me/kpszsu/64777)                                                                               |
| `sumy_oblast_chupakhivka`                  | [Чупахівка](https://t.me/AerisRimor/78053); [Чупахівки](https://t.me/AerisRimor/65725)                            |
| `sumy_oblast_dmytrivka`                    | [Дмитрівка](https://t.me/kyiv_airdef/61612); [Дмитрівку](https://t.me/kpszsu/80928)                               |
| `sumy_oblast_duboviazivka`                 | [Дубовʼязівка](https://t.me/AerisRimor/76751); [Дубов'язівка](https://t.me/AerisRimor/71849)                      |
| `sumy_oblast_esman`                        | [Есмань](https://t.me/kpszsu/78343)                                                                               |
| `sumy_oblast_hlukhiv`                      | [ГЛУХІВ](https://t.me/kyiv_airdef/43928)                                                                          |
| `sumy_oblast_kharkivshchyna`               | [Харківщина](https://t.me/kyiv_airdef/31807); [Харківщину](https://t.me/kyiv_airdef/62972)                        |
| `sumy_oblast_khotin`                       | [Хотінь](https://t.me/kpszsu/64555)                                                                               |
| `sumy_oblast_konotop`                      | [конотоп](https://t.me/kyiv_airdef/39965)                                                                         |
| `sumy_oblast_krasnopillia`                 | [Краснопілля](https://t.me/AerisRimor/79797)                                                                      |
| `sumy_oblast_krolevets`                    | [Кролевець](https://t.me/AerisRimor/73981); [Кролевця](https://t.me/AerisRimor/69696)                             |
| `sumy_oblast_kyrykivka`                    | [Кириківка](https://t.me/kpszsu/67834); [Кириківку](https://t.me/AerisRimor/86076)                                |
| `sumy_oblast_lebedyn`                      | [Лебедин](https://t.me/kyiv_airdef/58836)                                                                         |
| `sumy_oblast_lypova_dolyna`                | [Липова Долина](https://t.me/AerisRimor/80886); [Липової Долини](https://t.me/kpszsu/67241)                       |
| `sumy_oblast_mykolaivka`                   | [Миколаївка](https://t.me/nebo_raketa/47762); [Миколаївку](https://t.me/kyiv_airdef/44538)                        |
| `sumy_oblast_nedryhailiv`                  | [Недригайлів](https://t.me/kpszsu/71352)                                                                          |
| `sumy_oblast_nyzy`                         | [Низи](https://t.me/AerisRimor/79539)                                                                             |
| `sumy_oblast_okhtyrka`                     | [охтирка](https://t.me/kyiv_airdef/44757)                                                                         |
| `sumy_oblast_putivl`                       | [Путивль](https://t.me/kpszsu/61582)                                                                              |
| `sumy_oblast_romny`                        | [ромни](https://t.me/kyiv_airdef/43856)                                                                           |
| `sumy_oblast_shalyhyne`                    | [Шалигине](https://t.me/AerisRimor/70711); [Шалигиного](https://t.me/kpszsu/69768)                                |
| `sumy_oblast_svesa`                        | [Свеса](https://t.me/AerisRimor/74471)                                                                            |
| `sumy_oblast_terny`                        | [Терни](https://t.me/AerisRimor/80642)                                                                            |
| `sumy_oblast_trostianets`                  | [тростянець](https://t.me/kyiv_airdef/37991)                                                                      |
| `sumy_oblast_ulianivka`                    | [Улянівка](https://t.me/AerisRimor/64865); [Улянівку](https://t.me/kpszsu/61169)                                  |
| `sumy_oblast_velyka_pysarivka`             | [Велика Писарівка](https://t.me/war_monitor/38867); [Велику Писарівку](https://t.me/kpszsu/59453)                 |
| `sumy_oblast_voronizh`                     | [Вороніж](https://t.me/nebo_raketa/45723)                                                                         |
| `sumy_oblast_vorozhba`                     | [Ворожба](https://t.me/AerisRimor/76469)                                                                          |
| `sumy_oblast_yampil`                       | [Ямпіль](https://t.me/AerisRimor/74471)                                                                           |
| `sumy_oblast_znob_novhorodske`             | [Зноб-Новгородське](https://t.me/kpszsu/63935)                                                                    |
| `ternopil_oblast_chortkiv`                 | [Чортків](https://t.me/AerisRimor/77572)                                                                          |
| `ternopil_oblast_hrymailiv`                | [Гримайлів](https://t.me/AerisRimor/77530)                                                                        |
| `ternopil_oblast_khorostkiv`               | [Хоростків](https://t.me/AerisRimor/77536)                                                                        |
| `ternopil_oblast_kozova`                   | [Козова](https://t.me/AerisRimor/77540)                                                                           |
| `ternopil_oblast_kremenets`                | [Кременець](https://t.me/AerisRimor/79835); [Кременця](https://t.me/AerisRimor/81169)                             |
| `ternopil_oblast_lanivtsi`                 | [Ланівці](https://t.me/AerisRimor/77581)                                                                          |
| `ternopil_oblast_terebovlia`               | [Теребовля](https://t.me/AerisRimor/77561); [Теребовлі](https://t.me/operinform/55363)                            |
| `ternopil_oblast_velyki_birky`             | [Великі Бірки](https://t.me/AerisRimor/68217)                                                                     |
| `ternopil_oblast_vyshnivets`               | [Вишнівець](https://t.me/AerisRimor/65413)                                                                        |
| `vinnytsia_oblast_bar`                     | [Бар](https://t.me/AerisRimor/77527)                                                                              |
| `vinnytsia_oblast_bershad`                 | [Бершадь](https://t.me/AerisRimor/65533)                                                                          |
| `vinnytsia_oblast_bratslav`                | [Брацлав](https://t.me/AerisRimor/65100)                                                                          |
| `vinnytsia_oblast_chechelnyk`              | [Чечельник](https://t.me/AerisRimor/86756); [Чечельника](https://t.me/AerisRimor/79819)                           |
| `vinnytsia_oblast_dashiv`                  | [Дашів](https://t.me/AerisRimor/65057)                                                                            |
| `vinnytsia_oblast_haisyn`                  | [ГАЙСИН](https://t.me/kyiv_airdef/43948)                                                                          |
| `vinnytsia_oblast_hlukhivtsi`              | [Глухівці](https://t.me/AerisRimor/86192)                                                                         |
| `vinnytsia_oblast_hnivan`                  | [Гнівань](https://t.me/AerisRimor/81128)                                                                          |
| `vinnytsia_oblast_illintsi`                | [Іллінці](https://t.me/AerisRimor/77513)                                                                          |
| `vinnytsia_oblast_khmilnyk`                | [Хмільник](https://t.me/AerisRimor/68153); [Хмільника](https://t.me/AerisRimor/87116)                             |
| `vinnytsia_oblast_kopaihorod`              | [Копайгород](https://t.me/AerisRimor/65361); [Копайгорода](https://t.me/kpszsu/80027)                             |
| `vinnytsia_oblast_koziatyn`                | [Козятин](https://t.me/AerisRimor/77503)                                                                          |
| `vinnytsia_oblast_kryzhopil`               | [Крижопіль](https://t.me/AerisRimor/71314); [Крижополя](https://t.me/AerisRimor/86356)                            |
| `vinnytsia_oblast_ladyzhyn`                | [Ладижин](https://t.me/kpszsu/67453)                                                                              |
| `vinnytsia_oblast_lypovets`                | [Липовець](https://t.me/AerisRimor/65098); [Липовця](https://t.me/kpszsu/79770)                                   |
| `vinnytsia_oblast_murovani_kurylivtsi`     | [Муровані Курилівці](https://t.me/AerisRimor/65369); [Мурованих Курилівців](https://t.me/kpszsu/79859)            |
| `vinnytsia_oblast_nemyriv`                 | [Немирів](https://t.me/AerisRimor/77500)                                                                          |
| `vinnytsia_oblast_orativ`                  | [Оратів](https://t.me/AerisRimor/68130)                                                                           |
| `vinnytsia_oblast_pohrebyshche`            | [Погребище](https://t.me/AerisRimor/77506); [Погребища](https://t.me/AerisRimor/86777)                            |
| `vinnytsia_oblast_rakhny_lisovi`           | [Рахни-Лісові](https://t.me/AerisRimor/81126); [Рахни Лісові](https://t.me/war_monitor/45790)                     |
| `vinnytsia_oblast_sharhorod`               | [Шаргород](https://t.me/AerisRimor/65360); [Шаргорода](https://t.me/AerisRimor/69125)                             |
| `vinnytsia_oblast_shpykiv`                 | [Шпиків](https://t.me/AerisRimor/86436)                                                                           |
| `vinnytsia_oblast_sytkivtsi`               | [Ситківці](https://t.me/AerisRimor/65060); [Ситківців](https://t.me/AerisRimor/83895)                             |
| `vinnytsia_oblast_teplyk`                  | [Теплик](https://t.me/AerisRimor/65142)                                                                           |
| `vinnytsia_oblast_tomashpil`               | [Томашпіль](https://t.me/AerisRimor/69019)                                                                        |
| `vinnytsia_oblast_trostianets`             | [тростянець](https://t.me/kyiv_airdef/37991)                                                                      |
| `vinnytsia_oblast_tulchyn`                 | [Тульчин](https://t.me/kpszsu/74973)                                                                              |
| `vinnytsia_oblast_turbiv`                  | [Турбів](https://t.me/AerisRimor/65939)                                                                           |
| `vinnytsia_oblast_tyvriv`                  | [Тиврів](https://t.me/AerisRimor/71115)                                                                           |
| `vinnytsia_oblast_ulaniv`                  | [Уланів](https://t.me/AerisRimor/68153)                                                                           |
| `vinnytsia_oblast_vapniarka`               | [Вапнярку](https://t.me/kpszsu/79702)                                                                             |
| `vinnytsia_oblast_voronovytsia`            | [Вороновиця](https://t.me/AerisRimor/83167); [Вороновиці](https://t.me/kpszsu/66107)                              |
| `vinnytsia_oblast_zhmerynka`               | [жмеринка](https://t.me/kyiv_airdef/43208); [Жмеринки](https://t.me/kyiv_airdef/37417)                            |
| `volyn_oblast_kolky`                       | [Колки](https://t.me/war_monitor/44522)                                                                           |
| `volyn_oblast_kovel`                       | [Ковель](https://t.me/war_monitor/44499)                                                                          |
| `volyn_oblast_liubeshiv`                   | [Любешів](https://t.me/war_monitor/44500)                                                                         |
| `volyn_oblast_tsuman`                      | [Цумань](https://t.me/AerisRimor/69149)                                                                           |
| `volyn_oblast_volodymyr`                   | [на Володимир](https://t.me/AerisRimor/77537); [від Володимир](https://t.me/AerisRimor/77544)                     |
| `zakarpattia_oblast_mukachevo`             | [Мукачево](https://t.me/operinform/52453)                                                                         |
| `zaporizhzhia_oblast_balabyne`             | [Балабине](https://t.me/kpszsu/64535); [Балабиного](https://t.me/kpszsu/68190)                                    |
| `zaporizhzhia_oblast_kushuhum`             | [Кушугум](https://t.me/kpszsu/64535)                                                                              |
| `zaporizhzhia_oblast_novomykolaivka`       | [Новомиколаївка](https://t.me/AerisRimor/68479); [Новомиколаївки](https://t.me/kpszsu/59775)                      |
| `zaporizhzhia_oblast_sotsmisto`            | [Соцмісто](https://t.me/AerisRimor/86913); [Соцмістт](https://t.me/kyiv_airdef/36878)                             |
| `zhytomyr_oblast_andrushivka`              | [Андрушівка](https://t.me/AerisRimor/66550); [Андрушівку](https://t.me/AerisRimor/79918)                          |
| `zhytomyr_oblast_berdychiv`                | [Бердичів](https://t.me/AerisRimor/87624); [Бердичева](https://t.me/AerisRimor/69576)                             |
| `zhytomyr_oblast_brusyliv`                 | [Брусилів](https://t.me/AerisRimor/65129); [Брусилова](https://t.me/AerisRimor/65092)                             |
| `zhytomyr_oblast_cherniakhiv`              | [Черняхів](https://t.me/kyiv_airdef/63331); [Черняхова](https://t.me/AerisRimor/86022)                            |
| `zhytomyr_oblast_chopovychi`               | [Чоповичі](https://t.me/AerisRimor/69073)                                                                         |
| `zhytomyr_oblast_chudniv`                  | [Чуднів](https://t.me/AerisRimor/66552)                                                                           |
| `zhytomyr_oblast_dovbysh`                  | [Довбиш](https://t.me/AerisRimor/69085)                                                                           |
| `zhytomyr_oblast_irshansk`                 | [Іршанськ](https://t.me/AerisRimor/87366)                                                                         |
| `zhytomyr_oblast_khoroshiv`                | [Хорошів](https://t.me/AerisRimor/69085)                                                                          |
| `zhytomyr_oblast_kornyn`                   | [Корнин](https://t.me/AerisRimor/86779)                                                                           |
| `zhytomyr_oblast_korosten`                 | [Коростень](https://t.me/kyiv_airdef/65644); [Коростеня](https://t.me/AerisRimor/79801)                           |
| `zhytomyr_oblast_korostyshiv`              | [Коростишів](https://t.me/operinform/52472)                                                                       |
| `zhytomyr_oblast_liubar`                   | [Любар](https://t.me/AerisRimor/65943)                                                                            |
| `zhytomyr_oblast_luhyny`                   | [Лугини](https://t.me/kpszsu/62178)                                                                               |
| `zhytomyr_oblast_malyn`                    | [Малин](https://t.me/AerisRimor/73169)                                                                            |
| `zhytomyr_oblast_narodychi`                | [Народичі](https://t.me/AerisRimor/88310); [Народичів](https://t.me/kpszsu/62886)                                 |
| `zhytomyr_oblast_nova_borova`              | [Нова Борова](https://t.me/AerisRimor/65815)                                                                      |
| `zhytomyr_oblast_novohuivynske`            | [Новогуйвинське](https://t.me/AerisRimor/65485)                                                                   |
| `zhytomyr_oblast_olevsk`                   | [Олевськ](https://t.me/AerisRimor/85942)                                                                          |
| `zhytomyr_oblast_ovruch`                   | [Овруч](https://t.me/AerisRimor/79800)                                                                            |
| `zhytomyr_oblast_ozerne`                   | [Озерне](https://t.me/AerisRimor/84936)                                                                           |
| `zhytomyr_oblast_pulyny`                   | [Пулини](https://t.me/AerisRimor/69085)                                                                           |
| `zhytomyr_oblast_radomyshl`                | [Радомишль](https://t.me/AerisRimor/86449); [Радомишля](https://t.me/AerisRimor/87793)                            |
| `zhytomyr_oblast_ruzhyn`                   | [Ружин](https://t.me/AerisRimor/81311)                                                                            |
| `zhytomyr_oblast_zarichany`                | [Зарічани](https://t.me/AerisRimor/68901)                                                                         |
| `zhytomyr_oblast_zviahel`                  | [Звягель](https://t.me/AerisRimor/68225)                                                                          |

## Collision and message sources

| Fixture                                      | Source                                                         |
| -------------------------------------------- | -------------------------------------------------------------- |
| Володимир Зеленський (personal name)         | https://t.me/nebo_raketa/40352                                 |
| високого калібру (adjective)                 | https://t.me/AerisRimor/68574                                  |
| мрії мрії (common noun)                      | https://t.me/AerisRimor/76342                                  |
| Конотопський (longer word)                   | https://t.me/AerisRimor/74236                                  |
| Коростень against Остер; Бровари against Бар | Sources for the corresponding positive spelling excerpts above |
| Modifier-letter apostrophe drone alert       | https://t.me/AerisRimor/76751                                  |
| ASCII apostrophe drone alert                 | https://t.me/kpszsu/60544                                      |
| Berdychiv drone route                        | https://t.me/AerisRimor/69576                                  |
