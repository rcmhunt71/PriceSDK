from APIs.interfaces.models.get_ucd_fields import GetUCDFieldsKeys, GetUCDFieldsList
from base.common.response import CommonResponse


class GetUCDFieldsResponse(CommonResponse):
    _ADD_KEYS = [GetUCDFieldsKeys.DATA]
    _SUB_MODELS = [GetUCDFieldsList]
