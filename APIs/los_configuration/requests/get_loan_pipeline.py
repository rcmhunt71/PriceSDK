from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class GetLoanPipelineRequestParams(BaseRequestModelKeys):
    LOAN_QUERY_ID: str = "LoanQueryId"
    SORT_ASCENDING: str = "SortAscending"
    SORT_FIELDS: str = "SortFields"


class GetLoanPipelineRequest(SimpleRequestModel):
    def __init__(self, loan_query_id, sort_ascending, sort_fields, session_id, nonce, pretty_print):
        self.loan_query_id = loan_query_id
        self.sort_ascending = sort_ascending
        self.sort_fields = sort_fields
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetLoanPipelineRequestParams.LOAN_QUERY_ID] = self.loan_query_id
        args[GetLoanPipelineRequestParams.SORT_ASCENDING] = self.sort_ascending
        args[GetLoanPipelineRequestParams.SORT_FIELDS] = self.sort_fields
        return args
