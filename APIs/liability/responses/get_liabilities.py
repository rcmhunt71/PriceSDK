from base.common.response import CommonResponse

from APIs.liability.models.liability import LiabilityEntriesList, LiabilitiesKeys


class GetLiabilities(CommonResponse):
    _ADD_KEYS = [LiabilitiesKeys.LIABILITIES]
    _SUB_MODELS = [LiabilityEntriesList]
