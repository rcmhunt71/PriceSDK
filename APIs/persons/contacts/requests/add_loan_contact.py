from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class AddLoanContactParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    CONTACT_ID: str = "ContactID"
    COMPANY_ID: str = "CompanyID"
    CONTACT_SETUP_ID: str = "ContactSetupID"


class AddLoanContactRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, contact_id, company_id, contact_setup_id, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.contact_id = contact_id
        self.company_id = company_id
        self.contact_setup_id = contact_setup_id
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[AddLoanContactParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[AddLoanContactParams.CONTACT_ID] = self.contact_id
        args[AddLoanContactParams.COMPANY_ID] = self.company_id
        args[AddLoanContactParams.CONTACT_SETUP_ID] = self.contact_setup_id
        return args
