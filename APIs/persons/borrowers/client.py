from dataclasses import dataclass

from APIs.persons.borrowers.requests.add_consent import AddConsentRequest
from APIs.persons.borrowers.requests.delete_borrower_pair import DeleteBorrowerPairRequest
from APIs.persons.borrowers.requests.set_customer import SetCustomerRequest
from APIs.persons.borrowers.requests.set_person_data import SetPersonDataRequest
from APIs.persons.borrowers.responses.add_borrower_pair import AddBorrowerPairResponse
from APIs.persons.borrowers.responses.get_borrower import GetBorrowerResponse
from APIs.persons.borrowers.responses.get_customer_loan_list import GetCustomerLoanListResponse
from APIs.persons.borrowers.responses.get_customers import GetCustomersResponse
from base.common.models.request import LoanNumberIdRequestModel
from base.clients.base_client import BaseClient
from base.common.response import CommonResponse


@dataclass
class ApiEndpoints:
    ADD_BORROWER_PAIR: str = "add_borrower_pair"
    ADD_CONSENT: str = "add_consent"
    DELETE_BORROWER_PAIR: str = "delete_borrower_pair"
    GET_BORROWER: str = "get_borrower"
    GET_CUSTOMER_LOAN_LIST: str = "get_customer_loan_list"
    GET_CUSTOMERS: str = "get_customers"
    SET_CUSTOMER: str = "set_customer"
    SET_PERSON_DATA: str = "set_person_data"
    SET_BORROWER_AUTHENTICATION: str = "set_borrower_authentication"


class BorrowersClient(BaseClient):
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"
    json_headers = {CONTENT_TYPE: APPLICATION_JSON
    }

    def add_borrower_pair(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.post(resource_endpoint=ApiEndpoints.ADD_BORROWER_PAIR, response_model=AddBorrowerPairResponse,
            params=request_model.as_params_dict, data=request_model.payload)

    def add_consent(self, loan_number_id, consent_reason, consent_marketing_type, consent_opt_type, consent_source,
            borrower_id, session_id=None, nonce=None, pretty_print=False):
        request_model = AddConsentRequest(loan_number_id=loan_number_id, consent_reason=consent_reason,
            consent_marketing_type=consent_marketing_type, consent_opt_type=consent_opt_type,
            consent_source=consent_source, borrower_id=borrower_id, session_id=self._get_session_id(session_id),
            nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.post(resource_endpoint=ApiEndpoints.ADD_CONSENT, response_model=CommonResponse,
            params=request_model.as_params_dict, data=request_model.payload)

    def delete_borrower_pair(self, loan_number_id, primary_borrower_id, secondary_borrower_id, session_id=None,
            nonce=None, pretty_print=False):
        request_model = DeleteBorrowerPairRequest(loan_number_id=loan_number_id,
            primary_borrower_id=primary_borrower_id, secondary_borrower_id=secondary_borrower_id,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.post(resource_endpoint=ApiEndpoints.DELETE_BORROWER_PAIR, response_model=CommonResponse,
            params=request_model.as_params_dict, data=request_model.payload)

    def get_customer_loan_list(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_CUSTOMER_LOAN_LIST,
            response_model=GetCustomerLoanListResponse, params=request_model.as_params_dict)

    def get_borrower(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_BORROWER, response_model=GetBorrowerResponse,
            params=request_model.as_params_dict)

    def get_customers(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_CUSTOMERS, response_model=GetCustomersResponse,
            params=request_model.as_params_dict)

    def set_customer(self, loan_number_id, payload_dict=None, session_id=None, nonce=None, pretty_print=False,
            **kwargs):
        request_model = SetCustomerRequest(loan_number_id=loan_number_id, payload_dict=payload_dict,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print,
            **kwargs)
        return self.post(resource_endpoint=ApiEndpoints.SET_CUSTOMER, response_model=CommonResponse,
            params=request_model.as_params_dict, data=request_model.as_json, headers=self.json_headers)

    def set_person_data(self, loan_number_id, payload_dict=None, session_id=None, nonce=None, pretty_print=False,
            **kwargs):
        request_model = SetPersonDataRequest(loan_number_id=loan_number_id, payload_dict=payload_dict,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print,
            **kwargs)
        return self.post(resource_endpoint=ApiEndpoints.SET_PERSON_DATA, response_model=CommonResponse,
            params=request_model.as_params_dict, data=request_model.as_json, headers=self.json_headers)

    def set_borrower_authentication(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.post(resource_endpoint=ApiEndpoints.SET_BORROWER_AUTHENTICATION, response_model=CommonResponse,
            params=request_model.as_params_dict, data=request_model.payload)
