from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class RunQueryGridFieldsRequestParams(BaseRequestModelKeys):
    LOAN_QUERY_ID: str = "LoanQueryID"
    SORT_FIELDS: str = "SortFields"
    SORT_ASCENDING: str = "SortAscending"


class RunQueryGridFieldsRequest(SimpleRequestModel):
    def __init__(self, loan_query_id, sort_fields, sort_ascending, session_id, nonce, pretty_print):
        self.loan_query_id = loan_query_id
        self.sort_fields = sort_fields
        self.sort_ascending = sort_ascending
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[RunQueryGridFieldsRequestParams.LOAN_QUERY_ID] = self.loan_query_id
        args[RunQueryGridFieldsRequestParams.SORT_FIELDS] = self.sort_fields
        args[RunQueryGridFieldsRequestParams.SORT_ASCENDING] = self.sort_ascending
        return args
