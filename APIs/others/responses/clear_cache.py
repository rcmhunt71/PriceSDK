from dataclasses import dataclass
from base.common.response import CommonResponse


@dataclass
class ClearCacheKeys:
    SYSTEM_INFORMATION: str = "SystemInformation"


class ClearCacheResponse(CommonResponse):
    _ADD_KEYS = [ClearCacheKeys.SYSTEM_INFORMATION]
    _SUB_MODELS = [None]
