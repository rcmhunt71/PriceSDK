from APIs.liability.models.liability import AddLiabilityKeys
from base.common.response import CommonResponse


class AddLiability(CommonResponse):
    ADD_KEYS = [AddLiabilityKeys.LIABILITY_ID]
    SUB_MODELS = [None]
