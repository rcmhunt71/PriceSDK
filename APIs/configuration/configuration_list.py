from dataclasses import dataclass

from base.common.response import CommonResponse


@dataclass
class ConfigurationListKeys:
    CONFIGURATION_LIST: str = "ConfigurationList"


class ConfigurationList(CommonResponse):
    _ADD_KEYS = [ConfigurationListKeys.CONFIGURATION_LIST]
    _SUB_MODELS = [None]
