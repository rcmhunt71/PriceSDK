from APIs.liability.models.liability import AddLiabilityKeys
from base.common.response import CommonResponse


class AddLiability(CommonResponse):
    _ADD_KEYS = [AddLiabilityKeys.LIABILITY_ID]
    _SUB_MODELS = [None]
