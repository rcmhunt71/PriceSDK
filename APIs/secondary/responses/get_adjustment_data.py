from base.common.response import CommonResponse
from APIs.secondary.models.get_adjustment_data import GetAdjustmentDataKeys, GetAdjustmentDataList


class GetAdjustmentDataResponse(CommonResponse):
    _ADD_KEYS = [GetAdjustmentDataKeys.ADJUSTMENTS]
    _SUB_MODELS = [GetAdjustmentDataList]
