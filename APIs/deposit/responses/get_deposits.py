from APIs.deposit.models.deposit import Deposits, DepositsKeys
from base.common.response import CommonResponse


class GetDeposits(CommonResponse):
    ADD_KEYS = [DepositsKeys.DEPOSITS]
    SUB_MODELS = [Deposits]
