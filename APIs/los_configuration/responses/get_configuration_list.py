from base.common.response import CommonResponse
from dataclasses import dataclass


@dataclass
class GetConfigurationListKeys:
    CONFIGURATION_LIST: str = "ConfigurationList"


class GetConfigurationListResponse(CommonResponse):
    _ADD_KEYS = [GetConfigurationListKeys.CONFIGURATION_LIST]
    _SUB_MODELS = [None]
