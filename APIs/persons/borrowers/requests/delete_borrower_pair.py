from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class DeleteBorrowerPairRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    PRIMARY_BORROWER_ID: str = "PrimaryBorrowerId"
    SECONDARY_BORROWER_ID: str = "SecondaryBorrowerId"


class DeleteBorrowerPairRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, primary_borrower_id, secondary_borrower_id, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.primary_borrower_id = primary_borrower_id
        self.secondary_borrower_id = secondary_borrower_id
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[DeleteBorrowerPairRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[DeleteBorrowerPairRequestParams.PRIMARY_BORROWER_ID] = self.primary_borrower_id
        args[DeleteBorrowerPairRequestParams.SECONDARY_BORROWER_ID] = self.secondary_borrower_id
        return args
