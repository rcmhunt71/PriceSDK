from APIs.deposit.models.deposit_account import DepositAccounts, DepositAccountsKeys
from base.common.response import CommonResponse


class GetDepositAccounts(CommonResponse):
    _ADD_KEYS = [DepositAccountsKeys.DEPOSIT_ACCOUNTS]
    _SUB_MODELS = [DepositAccounts]
