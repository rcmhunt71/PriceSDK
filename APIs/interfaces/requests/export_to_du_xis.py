from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class ExportToDuXisRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    CREDIT_REPORT_ID: str = "CreditReportID"
    CREDIT_VENDOR: str = "CreditVendor"
    CREDIT_ACCOUNT_PASSWORD: str = "CreditAccountPassword"
    BORROWER_SSN: str = "BorrowerSSN"
    CREDIT_ACCOUNT_NUMBER: str = "CreditAccountNumber"
    CREDIT_REQUEST_TYPE: str = "CreditRequestType"


class ExportToDuXisRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, credit_report_id, credit_vendor, credit_account_password, borrower_ssn,
                 credit_account_number, credit_request_type, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.credit_report_id = credit_report_id
        self.credit_vendor = credit_vendor
        self.credit_account_password = credit_account_password
        self.borrower_ssn = borrower_ssn
        self.credit_account_number = credit_account_number
        self.credit_request_type = credit_request_type
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[ExportToDuXisRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[ExportToDuXisRequestParams.CREDIT_REPORT_ID] = self.credit_report_id
        args[ExportToDuXisRequestParams.CREDIT_VENDOR] = self.credit_vendor
        args[ExportToDuXisRequestParams.CREDIT_ACCOUNT_PASSWORD] = self.credit_account_password
        args[ExportToDuXisRequestParams.BORROWER_SSN] = self.borrower_ssn
        args[ExportToDuXisRequestParams.CREDIT_ACCOUNT_NUMBER] = self.credit_account_number
        args[ExportToDuXisRequestParams.CREDIT_REQUEST_TYPE] = self.credit_request_type
        return args
