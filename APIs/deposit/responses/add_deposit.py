from APIs.deposit.models.add_deposit import AddDepositKeys
from base.common.response import CommonResponse


class AddDeposit(CommonResponse):
    _ADD_KEYS = [AddDepositKeys.DEPOSIT_ID, AddDepositKeys.DEPOSIT_ACCOUNT_ID]
    _SUB_MODELS = [None, None]
