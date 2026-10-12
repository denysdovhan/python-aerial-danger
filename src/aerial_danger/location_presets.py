"""Area pattern presets for Aerial Danger."""

from typing import Final

from .locations.cherkasy_oblast import CHERKASY_OBLAST_REGION
from .locations.chernihiv_oblast import CHERNIHIV_OBLAST_REGION
from .locations.chernivtsi_oblast import CHERNIVTSI_OBLAST_REGION
from .locations.dnipropetrovsk_oblast import DNIPROPETROVSK_OBLAST_REGION
from .locations.donetsk_oblast import DONETSK_OBLAST_REGION
from .locations.ivano_frankivsk_oblast import IVANO_FRANKIVSK_OBLAST_REGION
from .locations.kharkiv_oblast import KHARKIV_OBLAST_REGION
from .locations.kherson_oblast import KHERSON_OBLAST_REGION
from .locations.khmelnytskyi_oblast import KHMELNYTSKYI_OBLAST_REGION
from .locations.kirovohrad_oblast import KIROVOHRAD_OBLAST_REGION
from .locations.kyiv import KYIV_REGION
from .locations.kyiv_oblast import KYIV_OBLAST_REGION
from .locations.luhansk_oblast import LUHANSK_OBLAST_REGION
from .locations.lviv_oblast import LVIV_OBLAST_REGION
from .locations.mykolaiv_oblast import MYKOLAIV_OBLAST_REGION
from .locations.odesa_oblast import ODESA_OBLAST_REGION
from .locations.poltava_oblast import POLTAVA_OBLAST_REGION
from .locations.rivne_oblast import RIVNE_OBLAST_REGION
from .locations.sumy_oblast import SUMY_OBLAST_REGION
from .locations.ternopil_oblast import TERNOPIL_OBLAST_REGION
from .locations.vinnytsia_oblast import VINNYTSIA_OBLAST_REGION
from .locations.volyn_oblast import VOLYN_OBLAST_REGION
from .locations.zakarpattia_oblast import ZAKARPATTIA_OBLAST_REGION
from .locations.zaporizhzhia_oblast import ZAPORIZHZHIA_OBLAST_REGION
from .locations.zhytomyr_oblast import ZHYTOMYR_OBLAST_REGION
from .models import LocalityPreset, RegionPreset

__all__ = ["LOCATION_PRESETS", "LocalityPreset", "RegionPreset"]

LOCATION_PRESETS: Final = {
    region.id: region
    for region in (
        CHERKASY_OBLAST_REGION,
        CHERNIHIV_OBLAST_REGION,
        CHERNIVTSI_OBLAST_REGION,
        DNIPROPETROVSK_OBLAST_REGION,
        DONETSK_OBLAST_REGION,
        IVANO_FRANKIVSK_OBLAST_REGION,
        KHARKIV_OBLAST_REGION,
        KHERSON_OBLAST_REGION,
        KHMELNYTSKYI_OBLAST_REGION,
        KIROVOHRAD_OBLAST_REGION,
        KYIV_REGION,
        KYIV_OBLAST_REGION,
        LUHANSK_OBLAST_REGION,
        LVIV_OBLAST_REGION,
        MYKOLAIV_OBLAST_REGION,
        ODESA_OBLAST_REGION,
        POLTAVA_OBLAST_REGION,
        RIVNE_OBLAST_REGION,
        SUMY_OBLAST_REGION,
        TERNOPIL_OBLAST_REGION,
        VINNYTSIA_OBLAST_REGION,
        VOLYN_OBLAST_REGION,
        ZAKARPATTIA_OBLAST_REGION,
        ZAPORIZHZHIA_OBLAST_REGION,
        ZHYTOMYR_OBLAST_REGION,
    )
}
