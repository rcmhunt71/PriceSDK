from dataclasses import dataclass
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class GetLoanStatusConfigInfoKeys:
    STATUS: str = "Status"


@dataclass
class GetLoanStatusConfigKeys:
    LOAN_STATUSES: str = "LoanStatuses"


class GetLoanStatusConfig(BaseResponse):
    _ADD_KEYS = [GetLoanStatusConfigInfoKeys.STATUS]


class GetLoanStatusConfigList(BaseListResponse):
    _SUB_MODEL = GetLoanStatusConfig
