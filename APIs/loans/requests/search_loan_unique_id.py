from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


class SearchBy:
    ID_AND_NUMBER_AND_RETURN_FIRST_RECORD = 0
    ID_AND_RETURN_ID = 1
    NUMBER_AND_RETURN_CORRESPONDING_ID = 2
    ID_AND_NUMBER_AND_RETURN_CORRESPONDING_ID = 3
    NUMBER_AND_RETURN_FIRST_RECORD_ID = 4


@dataclass
class SearchLoanUniqueIdRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    SEARCH_MODE: str = "SearchMode"


class SearchLoanUniqueIdRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, search_mode, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.search_mode = search_mode
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[SearchLoanUniqueIdRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[SearchLoanUniqueIdRequestParams.SEARCH_MODE] = self.search_mode
        return args
