from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class GetConfigurationListMultipleInfoKeys:
    NAME: str = "Name"
    CONFIGURATION: str = "Configuration"


@dataclass
class GetConfigurationListMultipleKeys:
    CONFIGURATION_LIST: str = "ConfigurationList"


class GetConfigurationListMultiple(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(GetConfigurationListMultipleInfoKeys)]


class GetConfigurationListMultipleList(BaseListResponse):
    _SUB_MODEL = GetConfigurationListMultiple
