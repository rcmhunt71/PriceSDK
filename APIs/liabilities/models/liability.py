from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse

@dataclass
class LiabilitiesInfoKeys:
    LIABILITY_ID: str = "LiabilityID"
    CUSTOMER_ID: str = "CustomerID"
    INSTITUTION_ID: str = "InstitutionID"
    LIABILITY_TYPE: str = "LiabilityType"
    ACCOUNT_NAME: str = "AccountName"
    ACCOUNT_NUMBER: str = "AccountNumber"
    BALANCE: str = "Balance"
    TERM: str = "Term"
    PAYMENT: str = "Payment"
    PAYOFF: str = "Payoff"
    TO_BE_PAID_OFF: str = "ToBePaidOff"


@dataclass
class LiabilitiesKeys:
    LIABILITIES: str = "Liabilities"


class Liability(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(LiabilitiesInfoKeys)]


class Liabilities(BaseListResponse):
    _SUB_MODEL = Liability
