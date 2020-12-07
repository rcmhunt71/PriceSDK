from APIs.los_configuration.models.get_fees import GetFeesKeys, GetFeesList
from base.common.response import CommonResponse


class GetFeesResponse(CommonResponse):
    _ADD_KEYS = [GetFeesKeys.FEES]
    _SUB_MODELS = [GetFeesList]
