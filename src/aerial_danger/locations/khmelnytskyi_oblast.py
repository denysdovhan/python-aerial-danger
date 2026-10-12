"""Location presets for khmelnytskyi oblast."""

from typing import Final

from aerial_danger.models import LocalityPreset, RegionPreset

KHMELNYTSKYI_OBLAST_REGION: Final = RegionPreset(
    id="khmelnytskyi_oblast",
    patterns=(
        r"\bхмельниччин(а|и|і|у|ою)\b",
        r"\bхмельницьк(а|ої|ій|у|ою) област(ь|і|ю)\b",
    ),
    localities={
        "khmelnytskyi_oblast_dunaivtsi": LocalityPreset(
            id="khmelnytskyi_oblast_dunaivtsi",
            patterns=(r"\bдунаївц(і|ів|ям|ями|ях)\b",),
        ),
        "khmelnytskyi_oblast_iziaslav": LocalityPreset(
            id="khmelnytskyi_oblast_iziaslav",
            patterns=(r"\bізяслав(а|у|ом|і)?\b",),
        ),
        "khmelnytskyi_oblast_khmelnytskyi": LocalityPreset(
            id="khmelnytskyi_oblast_khmelnytskyi",
            patterns=(r"\bхмельницьк(ий|ого|ому|им|ім)\b",),
        ),
        "khmelnytskyi_oblast_krasyliv": LocalityPreset(
            id="khmelnytskyi_oblast_krasyliv",
            patterns=(r"\bкрасил(ів|ова|ову|овом|ові)\b",),
        ),
        "khmelnytskyi_oblast_letychiv": LocalityPreset(
            id="khmelnytskyi_oblast_letychiv",
            patterns=(r"\bлетич(ів|ова|ову|овом|ові)\b",),
        ),
        "khmelnytskyi_oblast_netishyn": LocalityPreset(
            id="khmelnytskyi_oblast_netishyn",
            patterns=(r"\bнетішин(а|у|ом|і)?\b",),
        ),
        "khmelnytskyi_oblast_nova_ushytsia": LocalityPreset(
            id="khmelnytskyi_oblast_nova_ushytsia",
            patterns=(r"\bнов(а|ої|ій|у|ою)\s+ушиц(я|і|ю|ею)\b",),
        ),
        "khmelnytskyi_oblast_sataniv": LocalityPreset(
            id="khmelnytskyi_oblast_sataniv",
            patterns=(r"\bсатан(ів|ова|ову|овом|ові)\b",),
        ),
        "khmelnytskyi_oblast_shepetivka": LocalityPreset(
            id="khmelnytskyi_oblast_shepetivka",
            patterns=(r"\bшепетів(ка|ки|ці|ку|кою)\b",),
        ),
        "khmelnytskyi_oblast_slavuta": LocalityPreset(
            id="khmelnytskyi_oblast_slavuta",
            patterns=(r"\bславут(а|и|і|у|ою)\b",),
        ),
        "khmelnytskyi_oblast_smotrych": LocalityPreset(
            id="khmelnytskyi_oblast_smotrych",
            patterns=(r"\bсмотрич(а|у|ем|і)?\b",),
        ),
        "khmelnytskyi_oblast_stara_syniava": LocalityPreset(
            id="khmelnytskyi_oblast_stara_syniava",
            patterns=(r"\bстар(а|ої|ій|у|ою)\s+синяв(а|и|і|у|ою)\b",),
        ),
        "khmelnytskyi_oblast_stara_ushytsia": LocalityPreset(
            id="khmelnytskyi_oblast_stara_ushytsia",
            patterns=(r"\bстар(а|ої|ій|у|ою)\s+ушиц(я|і|ю|ею)\b",),
        ),
        "khmelnytskyi_oblast_starokostiantyniv": LocalityPreset(
            id="khmelnytskyi_oblast_starokostiantyniv",
            patterns=(
                r"\bстарокостянтин(ів|ова|ову|овом|ові)\b",
                r"\bстаркон(у|а)?\b",
            ),
        ),
        "khmelnytskyi_oblast_vinkivtsi": LocalityPreset(
            id="khmelnytskyi_oblast_vinkivtsi",
            patterns=(r"\bвіньківц(і|ів|ям|ями|ях)\b",),
        ),
        "khmelnytskyi_oblast_volochysk": LocalityPreset(
            id="khmelnytskyi_oblast_volochysk",
            patterns=(r"\bволочиськ(а|у|ом|і)?\b",),
        ),
        "khmelnytskyi_oblast_vovkovyntsi": LocalityPreset(
            id="khmelnytskyi_oblast_vovkovyntsi",
            patterns=(r"\bвовковинц(і|ів|ям|ями|ях)\b",),
        ),
        "khmelnytskyi_oblast_yarmolyntsi": LocalityPreset(
            id="khmelnytskyi_oblast_yarmolyntsi",
            patterns=(r"\bярмолин(ці|ців|цям|цями|цях)\b",),
        ),
        "khmelnytskyi_oblast_zakupne": LocalityPreset(
            id="khmelnytskyi_oblast_zakupne",
            patterns=(r"\bзакупн(е|ого|ому|им|ім)\b",),
        ),
    },
)
