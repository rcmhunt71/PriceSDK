from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel


@dataclass
class GetLoanPrintFormsRequestParams:
    LOAN_NUMBER_ID: str = "LoanNumberID"
    SORT_BY: str = "SortBy"


class GetLoanPrintFormsRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, sort_by, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.sort_by = sort_by
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetLoanPrintFormsRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[GetLoanPrintFormsRequestParams.SORT_BY] = self.sort_by
        return args
