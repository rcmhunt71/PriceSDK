from dataclasses import dataclass

from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class AddLoanFeeRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    FEE_ID: str = "FeeID"


class AddLoanFeeRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, fee_id, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.fee_id = fee_id
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[AddLoanFeeRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[AddLoanFeeRequestParams.FEE_ID] = self.fee_id
        return args
