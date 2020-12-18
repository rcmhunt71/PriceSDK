from dataclasses import dataclass
from base.common.response import CommonResponse


@dataclass
class SystemInformationKeys:
    SYSTEM_INFORMATION: str = "SystemInformation"


class SystemInformationResponse(CommonResponse):
    _ADD_KEYS = [SystemInformationKeys.SYSTEM_INFORMATION]
    _SUB_MODELS = [None]
