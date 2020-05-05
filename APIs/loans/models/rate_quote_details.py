from dataclasses import dataclass, fields

from base.responses.base_response import BaseResponse


@dataclass
class RateQuoteDetailsInfoKeys:
    VENDOR: str = "Vendor"
    PAYMENT_PERIOD: str = "PaymentPeriod"
    RENEWAL_TYPE: str = "RenewalType"
    ZERO_DUE_AT_CLOSING: str = "ZeroDueAtClosing"
    REFUNDABLE: str = "Refundable"
    COVERAGE: str = "Coverage"
    PAYMENT_TYPE: str = "PaymentType"
    MIS_SPECIAL_DEAL: str = "MISSpecialDeal"
    RATE_QUOTE_ID: str = "RateQuoteID"
    RATE_PLAN_TYPE: str = "RatePlanType"
    STATUS_DESCRIPTION: str = "StatusDescription"


@dataclass
class RateQuoteDetailsKeys:
    LOAN_RATE_QUOTE_DETAILS: str = "LoanRateQuoteDetails"


class RateQuoteDetails(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(RateQuoteDetailsInfoKeys)]
    _SUB_MODELS = [None for _ in _ADD_KEYS]

