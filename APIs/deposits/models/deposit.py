from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class DepositsInfoKeys:
    CUSTOMER_ID: str = "CustomerID"
    DEPOSIT_ID: str = "DepositID"
    INSTITUTION_ID: str = "InstitutionID"
    VERIFY: str = "Verify"
    VERIFY_DATE: str = "VerifyDate"
    BOTH: str = "Both"


@dataclass
class DepositsKeys:
    DEPOSITS: str = "Deposits"


class Deposit(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(DepositsInfoKeys)]


class Deposits(BaseListResponse):
    _SUB_MODEL = Deposit
