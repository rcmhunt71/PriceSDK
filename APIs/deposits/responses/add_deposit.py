from APIs.deposits.models.add_deposit import AddDepositKeys
from base.common.response import CommonResponse


class AddDepositResponse(CommonResponse):
    _ADD_KEYS = [AddDepositKeys.DEPOSIT_ID, AddDepositKeys.DEPOSIT_ACCOUNT_ID]
    _SUB_MODELS = [None, None]
