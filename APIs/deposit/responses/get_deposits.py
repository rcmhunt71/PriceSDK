from APIs.deposit.models.deposit import Deposits, DepositsKeys
from base.common.response import CommonResponse


class GetDeposits(CommonResponse):
    _ADD_KEYS = [DepositsKeys.DEPOSITS]
    _SUB_MODELS = [Deposits]
