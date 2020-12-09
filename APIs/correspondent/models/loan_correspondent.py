from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse


@dataclass
class LoanCorrespondentInfoKeys:
    CORRESPONDENT_DELEGATED: str = "CorrespondentDelegated"
    CORRESPONDENT_SERVICING: str = "CorrespondentServicing"
    CORRESPONDENT_SERVICING_TRANSFER: str = "CorrespondentServicingTransfer"


@dataclass
class LoanCorrespondentKeys:
    LOAN_CORRESPONDENT: str = "LoanCorrespondent"


class LoanCorrespondent(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(LoanCorrespondentInfoKeys)]
