from APIs.deposits.models.deposit import Deposits, DepositsKeys
from base.common.response import CommonResponse


class GetDepositsResponse(CommonResponse):
    _ADD_KEYS = [DepositsKeys.DEPOSITS]
    _SUB_MODELS = [Deposits]
