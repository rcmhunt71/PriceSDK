from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class DeleteIncomeRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    CUSTOMER_ID: str = "CustomerID"
    INCOME_ID: str = "IncomeID"


class DeleteIncomeRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, customer_id, income_id, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.customer_id = customer_id
        self.income_id = income_id
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[DeleteIncomeRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[DeleteIncomeRequestParams.CUSTOMER_ID] = self.customer_id
        args[DeleteIncomeRequestParams.INCOME_ID] = self.income_id
        return args
