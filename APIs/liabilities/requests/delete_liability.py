from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class DeleteLiabilityRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    CUSTOMER_ID: str = "CustomerID"
    LIABILITY_ID: str = "LiabilityID"


class DeleteLiabilityRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, customer_id, liability_id, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.customer_id = customer_id
        self.liability_id = liability_id
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[DeleteLiabilityRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[DeleteLiabilityRequestParams.CUSTOMER_ID] = self.customer_id
        args[DeleteLiabilityRequestParams.LIABILITY_ID] = self.liability_id
        return args
