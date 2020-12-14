from APIs.vendor_integration.models.media_center_data import MediaCenterDataKeys, MediaCenterData
from base.common.response import CommonResponse


class GetMediaCenterDataResponse(CommonResponse):
    _ADD_KEYS = [MediaCenterDataKeys.DATA]
    _SUB_MODELS = [MediaCenterData]
