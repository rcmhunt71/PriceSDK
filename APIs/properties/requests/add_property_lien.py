from dataclasses import dataclass

from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class AddPropertyLienRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    CUSTOMER_ID: str = "CustomerID"
    PROPERTY_ID: str = "PropertyID"


class AddPropertyLienRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, customer_id, property_id, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.customer_id = customer_id
        self.property_id = property_id
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[AddPropertyLienRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[AddPropertyLienRequestParams.CUSTOMER_ID] = self.customer_id
        args[AddPropertyLienRequestParams.PROPERTY_ID] = self.property_id
        return args
