from dataclasses import dataclass, fields

from base.responses.base_response import BaseResponse


@dataclass
class MIDetailsInfoKeys:
    MINAME: str = "MIName"
    MIPAYMENT_PERIOD: str = "MIPayment_Period"
    MIRENEWAL_TYPE: str = "MIRenewal_Type"
    MIZERODUEATCLOSING: str = "MIZeroDueAtClosing"
    MICOVERAGE: str = "MICoverage"
    MIPAYMENTTYPE: str = "MIPaymentType"
    MIRATEDETAILS: str = "MIRateDetails"


@dataclass
class MIDetailsKeys:
    LOANMIDETAILS: str = "LoanMIDetails"


class MIDetails(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(MIDetailsInfoKeys)]
    _SUB_MODELS = [None for _ in _ADD_KEYS]
