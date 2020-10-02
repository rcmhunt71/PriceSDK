from dataclasses import dataclass

from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class ClearDepositAccountRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    CUSTOMER_ID: str = "CustomerId"
    DEPOSIT_ID: str = "DepositId"
    DEPOSIT_ACCOUNT_ID: str = "DepositAccountId"


class ClearDepositAccountRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, customer_id, deposit_id, deposit_account_id, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.customer_id = customer_id
        self.deposit_id = deposit_id
        self.deposit_account_id = deposit_account_id
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[ClearDepositAccountRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[ClearDepositAccountRequestParams.CUSTOMER_ID] = self.customer_id
        args[ClearDepositAccountRequestParams.DEPOSIT_ID] = self.deposit_id
        args[ClearDepositAccountRequestParams.DEPOSIT_ACCOUNT_ID] = self.deposit_account_id
        return args
