from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class ChangePortalPasswordRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    BORROWER_ID: str = "BorrowerID"
    NEW_PASSWORD: str = "NewPassword"


class ChangePortalPasswordRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, borrower_id, new_password, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.borrower_id = borrower_id
        self.new_password = new_password

        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[ChangePortalPasswordRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[ChangePortalPasswordRequestParams.BORROWER_ID] = self.borrower_id
        args[ChangePortalPasswordRequestParams.NEW_PASSWORD] = self.new_password
        return args
