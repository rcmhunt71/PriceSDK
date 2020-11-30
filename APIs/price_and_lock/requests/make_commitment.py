from dataclasses import dataclass

from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class MakeCommitmentRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    INVESTOR_LOCK_DATE: str = "InvestorLockDate"
    INVESTOR_LOCK_EXPIRATION_DATE: str = "InvestorLockExpirationDate"
    INVESTOR_LOAN_NUMBER: str = "InvestorLoanNumber"
    COMMITMENT_NUMBER: str = "CommitmentNumber"


class MakeCommitmentRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, investor_lock_date, investor_lock_expiration_date, investor_loan_number,
                 commitment_number, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.investor_lock_date = investor_lock_date
        self.investor_lock_expiration_date = investor_lock_expiration_date
        self.investor_loan_number = investor_loan_number
        self.commitment_number = commitment_number
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[MakeCommitmentRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[MakeCommitmentRequestParams.INVESTOR_LOCK_DATE] = self.investor_lock_date
        args[MakeCommitmentRequestParams.INVESTOR_LOCK_EXPIRATION_DATE] = self.investor_lock_expiration_date
        args[MakeCommitmentRequestParams.INVESTOR_LOAN_NUMBER] = self.investor_loan_number
        args[MakeCommitmentRequestParams.COMMITMENT_NUMBER] = self.commitment_number
        return args
