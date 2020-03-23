from dataclasses import dataclass

from PRICE.base.common.models.request import BaseRequestModel, BaseRequestModelKeys


@dataclass
class GetLoanRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_IDS: str = "LoanNumberIDs"
    PRETTY_PRINT: bool = "PrettyPrint"


class GetLoanRequest(BaseRequestModel):
    def __init__(self, session_id, nonce, loan_number_ids, pretty_print=False):
        self.loan_number_ids = loan_number_ids
        self.pretty_print = pretty_print
        super().__init__(session_id=session_id, nonce=nonce)

    def to_params(self):
        args = {
            GetLoanRequestParams.SESSION_ID: self.session_id,
            GetLoanRequestParams.NONCE: self.nonce,
            GetLoanRequestParams.LOAN_NUMBER_IDS: self.loan_number_ids,
        }
        if self.pretty_print:
            args[GetLoanRequestParams.PRETTY_PRINT] = self.pretty_print
        return args


class GetLoanDetailRequest(GetLoanRequest):
    pass


class GetFinalValueTagsRequest(GetLoanRequest):
    pass
