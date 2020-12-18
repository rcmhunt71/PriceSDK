from APIs.others.models.feature_settings import FeatureSettingsKeys, FeatureSettingsList
from base.common.response import CommonResponse


class GetFeatureSettingsResponse(CommonResponse):
    _ADD_KEYS = [FeatureSettingsKeys.FEATURE_SETTINGS]
    _SUB_MODELS = [FeatureSettingsList]
