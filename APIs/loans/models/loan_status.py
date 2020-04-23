from dataclasses import dataclass

from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class LoanStatusKeys:
    F_LOAN_NUMBER_ID: str = "FLoanNumberId"
    F_LOAN_STATUS: str = "FLoanStatus"
    LOAN_STATUSES: str = "LoanStatuses"


class LoanStatus(BaseResponse):
    _ADD_KEYS = [LoanStatusKeys.F_LOAN_NUMBER_ID, LoanStatusKeys.F_LOAN_STATUS]
    _SUB_MODELS = [None, None]


class LoanStatuses(BaseListResponse):
    _SUB_MODEL = LoanStatus
