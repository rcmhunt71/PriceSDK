from dataclasses import dataclass
from base.common.response import CommonResponse


@dataclass
class GetLoanSearchIdListKeys:
    LOAN_SEARCH_IDS: str = "LoanSearchIDs"


class GetLoanSearchIdListResponse(CommonResponse):
    _ADD_KEYS = [GetLoanSearchIdListKeys.LOAN_SEARCH_IDS]
    _SUB_MODELS = [None]
