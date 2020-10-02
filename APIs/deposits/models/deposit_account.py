from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class DepositAccountsInfoKeys:
    CUSTOMER_ID: str = "CustomerID"
    DEPOSIT_ID: str = "DepositID"
    DEPOSIT_ACCOUNT_ID: str = "DepositAccountID"
    ACCOUNT_TYPE: str = "AccountType"
    ACCOUNT_NUMBER: str = "AccountNumber"
    ACCOUNT_NAME: str = "AccountName"
    BALANCE: str = "Balance"
    GIFT_DEPOSITED:  str = "GiftDeposited"
    GIFT_SOURCE: str = "GiftSource"
    GIFT_DEPOSITED_AMOUNT: str = "GiftDepositedAmount"
    FIELDS: str = "Fields"


@dataclass
class DepositAccountsKeys:
    DEPOSIT_ACCOUNTS: str = "DepositAccounts"


@dataclass
class DepositAccountsFieldsKeys:
    FIELD_NAME: str = "FieldName"
    FIELD_VALUE: str = "FieldValue"


class DepositAccount(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(DepositAccountsInfoKeys)]


class DepositAccounts(BaseListResponse):
    _SUB_MODEL = DepositAccount


class DepositAccountFieldEntry(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(DepositAccountsFieldsKeys)]


class DepositAccountFieldList(BaseListResponse):
    _SUB_MODEL = DepositAccountFieldEntry


class DepositAccountRequestModel(BaseResponse):
    _ADD_KEYS = [DepositAccountsInfoKeys.CUSTOMER_ID, DepositAccountsInfoKeys.DEPOSIT_ID,
                 DepositAccountsInfoKeys.DEPOSIT_ACCOUNT_ID, DepositAccountsInfoKeys.FIELDS]
    _SUB_MODELS = [None, None, None, DepositAccountFieldList]
