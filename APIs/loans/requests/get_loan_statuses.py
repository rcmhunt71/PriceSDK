from dataclasses import dataclass

from base.common.models.request import BaseRequestModel, BaseRequestModelKeys


@dataclass
class GetLoanStatusesParams(BaseRequestModelKeys):
    LOAN_NUMBER_IDS: str = "LoanNumberIDs"

class GetLoanStatusesRequest(BaseRequestModel):
    def __init__(self, session_id, nonce, loan_number_ids, pretty_print=False):
        self.loan_number_ids = loan_number_ids
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetLoanStatusesParams.LOAN_NUMBER_IDS] = self.loan_number_ids