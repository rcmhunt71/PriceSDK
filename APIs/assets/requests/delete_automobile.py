from dataclasses import dataclass

from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class DeleteAutomobileRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    CUSTOMER_ID: str = "CustomerID"
    ASSET_ID: str = "AssetID"


class DeleteAutomobileRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, customer_id, asset_id, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.customer_id = customer_id
        self.asset_id = asset_id
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[DeleteAutomobileRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[DeleteAutomobileRequestParams.CUSTOMER_ID] = self.customer_id
        args[DeleteAutomobileRequestParams.ASSET_ID] = self.asset_id
        return args
