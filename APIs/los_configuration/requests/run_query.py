from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class RunQueryRequestParams(BaseRequestModelKeys):
    LOAN_ID_LIST: str = "LoanIDList"
    LOAN_QUERY_ID: str = "LoanQueryID"
    SORT_FIELD: str = "SortField"
    SORT_ASCENDING: str = "SortAscending"


class RunQueryRequest(SimpleRequestModel):
    def __init__(self, loan_id_list, loan_query_id, sort_field, sort_ascending, session_id, nonce, pretty_print):
        self.loan_id_list = loan_id_list
        self.loan_query_id = loan_query_id
        self.sort_field = sort_field
        self.sort_ascending = sort_ascending
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[RunQueryRequestParams.LOAN_ID_LIST] = self.loan_id_list
        args[RunQueryRequestParams.LOAN_QUERY_ID] = self.loan_query_id
        args[RunQueryRequestParams.SORT_FIELD] = self.sort_field
        args[RunQueryRequestParams.SORT_ASCENDING] = self.sort_ascending
        return args
