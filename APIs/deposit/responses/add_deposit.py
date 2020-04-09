from APIs.deposit.models.add_deposit import AddDepositKeys
from base.common.response import CommonResponse


class AddDeposit(CommonResponse):
    ADD_KEYS = [AddDepositKeys.DEPOSIT_ID, AddDepositKeys.DEPOSIT_ACCOUNT_ID]
    SUB_MODELS = [None, None]
