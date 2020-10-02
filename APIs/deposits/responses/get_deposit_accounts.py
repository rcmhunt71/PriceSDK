from APIs.deposits.models.deposit_account import DepositAccounts, DepositAccountsKeys
from base.common.response import CommonResponse


class GetDepositAccountsResponse(CommonResponse):
    _ADD_KEYS = [DepositAccountsKeys.DEPOSIT_ACCOUNTS]
    _SUB_MODELS = [DepositAccounts]
