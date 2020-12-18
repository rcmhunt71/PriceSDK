from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class FeatureSettingsInfoKeys:
    NAME: str = "Name"
    VALUE: str = "Value"


@dataclass
class FeatureSettingsKeys:
    FEATURE_SETTINGS: str = "FeatureSettings"


class FeatureSettings(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(FeatureSettingsInfoKeys)]


class FeatureSettingsList(BaseListResponse):
    _SUB_MODEL = FeatureSettings
