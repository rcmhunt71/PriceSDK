from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class FormFreeVerificationRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    BORROWER_ID: str = "BorrowerID"
    REQUEST_TYPE: str = "RequestType"


class FormFreeVerificationRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, borrower_id, request_type, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.borrower_id = borrower_id
        self.request_type = request_type
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[FormFreeVerificationRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[FormFreeVerificationRequestParams.BORROWER_ID] = self.borrower_id
        args[FormFreeVerificationRequestParams.REQUEST_TYPE] = self.request_type
        return args
