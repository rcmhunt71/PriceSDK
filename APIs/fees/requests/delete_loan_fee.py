from dataclasses import dataclass

from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class DeleteLoanFeeRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    LOAN_FEE_ID: str = "LoanFeeID"


class DeleteLoanFeeRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, loan_fee_id, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.loan_fee_id = loan_fee_id
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[DeleteLoanFeeRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[DeleteLoanFeeRequestParams.LOAN_FEE_ID] = self.loan_fee_id
        return args
