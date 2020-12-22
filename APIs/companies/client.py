from dataclasses import dataclass

from APIs.companies.requests.get_company_license_types import GetCompanyLicenseTypesRequest, GetCompanyMembersRequest
from APIs.companies.requests.get_company_logo import GetCompanyLogoRequest
from APIs.companies.requests.set_companies import SetCompaniesRequest
from APIs.companies.requests.set_company_license_type import SetCompanyLicenseTypeRequest
from APIs.companies.responses.get_company_ids import GetCompanyIDsResponse
from APIs.companies.requests.add_company import AddCompanyRequest
from APIs.companies.requests.get_companies_by_ids import GetCompaniesByIDsRequest
from APIs.companies.requests.get_company_ids import GetCompanyIDsRequest
from APIs.companies.responses.add_company import AddCompanyResponse
from APIs.companies.responses.get_companies import GetCompaniesResponse, GetCompaniesByIDsResponse
from APIs.companies.responses.get_company_license_types import GetCompanyLicenseTypesResponse
from APIs.companies.responses.get_company_members import GetCompanyMembersResponse
from base.common.models.request import LoanNumberIdRequestModel
from base.clients.base_client import BaseClient
from base.common.response import CommonResponse


@dataclass
class ApiEndpoints:
    ADD_COMPANY: str = "add_company"
    GET_COMPANIES: str = "get_companies"
    GET_COMPANIES_BY_IDS: str = "get_companies_by_ids"
    GET_COMPANY_IDS: str = "get_company_ids"
    GET_COMPANY_LICENSE_TYPES: str = "get_company_license_types"
    GET_COMPANY_LOGO: str = "get_company_logo"
    GET_COMPANY_MEMBERS: str = "get_company_members"
    SET_COMPANIES: str = "set_companies"
    SET_COMPANY_LICENSE_TYPE: str = "set_company_license_type"


class CompaniesClient(BaseClient):
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"
    json_headers = {CONTENT_TYPE: APPLICATION_JSON
    }

    def add_company(self, company_type, field_name, field_value, referenced_only_once, employee_id, session_id=None,
            nonce=None, pretty_print=False):
        request_model = AddCompanyRequest(company_type=company_type, field_name=field_name, field_value=field_value,
            referenced_only_once=referenced_only_once, employee_id=employee_id,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.ADD_COMPANY, response_model=AddCompanyResponse,
            params=request_model.as_params_dict)

    def get_companies(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_COMPANIES, response_model=GetCompaniesResponse,
            params=request_model.as_params_dict)

    def get_companies_by_ids(self, company_ids, session_id=None, nonce=None, pretty_print=False):
        request_model = GetCompaniesByIDsRequest(company_ids=company_ids, session_id=self._get_session_id(session_id),
            nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_COMPANIES_BY_IDS, response_model=GetCompaniesByIDsResponse,
            params=request_model.as_params_dict)

    def get_company_ids(self, company_name, company_state=None, company_type=None, company_status=None, show_missing_data_companies=None,
            show_loan_specific_companies=None, show_loan_imported_companies=None, session_id=None, nonce=None,
            pretty_print=False):
        request_model = GetCompanyIDsRequest(company_name=company_name, company_state=company_state,
            company_type=company_type, company_status=company_status,
            show_missing_data_companies=show_missing_data_companies,
            show_loan_specific_companies=show_loan_specific_companies,
            show_loan_imported_companies=show_loan_imported_companies, session_id=self._get_session_id(session_id),
            nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_COMPANY_IDS, response_model=GetCompanyIDsResponse,
            params=request_model.as_params_dict)

    def get_company_license_types(self, company_id, session_id=None, nonce=None, pretty_print=False):
        request_model = GetCompanyLicenseTypesRequest(company_id=company_id,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_COMPANY_LICENSE_TYPES,
            response_model=GetCompanyLicenseTypesResponse, params=request_model.as_params_dict)

    # TODO Need to revisit Response later
    def get_company_logo(self, loan_number_id, height, width, session_id=None, nonce=None, pretty_print=False):
        request_model = GetCompanyLogoRequest(loan_number_id=loan_number_id, height=height, width=width,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_COMPANY_LOGO, response_model=CommonResponse,
            params=request_model.as_params_dict)

    def get_company_members(self, company_id, session_id=None, nonce=None, pretty_print=False):
        request_model = GetCompanyMembersRequest(company_id=company_id, session_id=self._get_session_id(session_id),
            nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_COMPANY_MEMBERS, response_model=GetCompanyMembersResponse,
            params=request_model.as_params_dict)

    def set_companies(self, loan_number_id, payload_dict=None, session_id=None, nonce=None, pretty_print=False,
            **kwargs):
        request_model = SetCompaniesRequest(loan_number_id=loan_number_id, payload_dict=payload_dict,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print,
            **kwargs)
        return self.post(resource_endpoint=ApiEndpoints.SET_COMPANIES, response_model=CommonResponse,
            params=request_model.as_params_dict, data=request_model.as_json, headers=self.json_headers)

    def set_company_license_type(self, company_id, license_number, company_type, session_id=None, nonce=None,
            pretty_print=False):
        request_model = SetCompanyLicenseTypeRequest(company_id=company_id, license_number=license_number,
            company_type=company_type, session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
            pretty_print=pretty_print)
        return self.post(resource_endpoint=ApiEndpoints.SET_COMPANY_LICENSE_TYPE, response_model=CommonResponse,
            params=request_model.as_params_dict, data=request_model.payload)
