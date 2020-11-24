from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class GetCompanyIDsParams(BaseRequestModelKeys):
    COMPANY_NAME: str = "CompanyName"
    COMPANY_STATE: str = "CompanyState"
    COMPANY_TYPE: str = "CompanyType"
    COMPANY_STATUS: str = "CompanyStatus"
    SHOW_MISSING_DATA_COMPANIES: str = "ShowMissingDataCompanies"
    SHOW_LOAN_SPECIFIC_COMPANIES: str = "ShowLoanSpecificCompanies"
    SHOW_LOAN_IMPORTED_COMPANIES: str = "ShowLoanImportedCompanies"


class GetCompanyIDsRequest(SimpleRequestModel):
    def __init__(self, company_name, company_state, company_type, company_status, show_missing_data_companies,
            show_loan_specific_companies, show_loan_imported_companies, session_id, nonce, pretty_print):
        self.company_name = company_name
        self.company_state = company_state
        self.company_type = company_type
        self.company_status = company_status
        self.show_missing_data_companies = show_missing_data_companies
        self.show_loan_specific_companies = show_loan_specific_companies
        self.show_loan_imported_companies = show_loan_imported_companies
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetCompanyIDsParams.COMPANY_NAME] = self.company_name
        args[GetCompanyIDsParams.COMPANY_STATE] = self.company_state
        args[GetCompanyIDsParams.COMPANY_TYPE] = self.company_type
        args[GetCompanyIDsParams.COMPANY_STATUS] = self.company_status
        args[GetCompanyIDsParams.SHOW_MISSING_DATA_COMPANIES] = self.show_missing_data_companies
        args[GetCompanyIDsParams.SHOW_LOAN_SPECIFIC_COMPANIES] = self.show_loan_specific_companies
        args[GetCompanyIDsParams.SHOW_LOAN_IMPORTED_COMPANIES] = self.show_loan_imported_companies
        return args
