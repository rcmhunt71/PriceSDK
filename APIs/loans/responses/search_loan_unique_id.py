from dataclasses import dataclass
from base.common.response import CommonResponse


@dataclass
class SearchLoanUniqueIdKeys:
    LOAN_UNIQUE_IDS: str = "LoanUniqueIDs"


class SearchLoanUniqueIdResponse(CommonResponse):
    _ADD_KEYS = [SearchLoanUniqueIdKeys.LOAN_UNIQUE_IDS]
    _SUB_MODELS = [None]
