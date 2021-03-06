from dataclasses import dataclass

from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class GetLoanStatusesRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_IDS: str = "LoanNumberIDs"


class GetLoanStatusesRequest(SimpleRequestModel):
    def __init__(self, loan_number_ids, session_id, nonce, pretty_print):
        self.loan_number_ids = loan_number_ids
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetLoanStatusesRequestParams.LOAN_NUMBER_IDS] = self.loan_number_ids
        return args