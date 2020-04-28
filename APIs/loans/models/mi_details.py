from dataclasses import dataclass

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
    _ADD_KEYS = list(getattr(MIDetailsInfoKeys, _) for _ in MIDetailsInfoKeys.__annotations__)
    _SUB_MODELS = [None for _ in range(len(_ADD_KEYS))]
