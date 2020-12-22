from dataclasses import dataclass
from APIs.incomes.requests.add_income import AddIncomeRequest
from APIs.incomes.requests.delete_income import DeleteIncomeRequest
from APIs.incomes.requests.set_incomes import SetIncomesRequest
from APIs.incomes.responses.add_income import AddIncomeResponse
from APIs.incomes.responses.get_incomes import GetIncomesResponse
from base.common.models.request import LoanNumberIdRequestModel
from base.clients.base_client import BaseClient
from base.common.response import CommonResponse


@dataclass
class ApiEndpoints:
    ADD_INCOME: str = "add_income"
    DELETE_INCOME: str = "delete_income"
    GET_INCOMES: str = "get_incomes"
    SET_INCOMES: str = "set_incomes"


class IncomesClient(BaseClient):
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"
    json_headers = {
        CONTENT_TYPE: APPLICATION_JSON
    }

    def get_incomes(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
                                         session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
                                         pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_INCOMES, response_model=GetIncomesResponse,
                        params=request_model.as_params_dict)

    def add_income(self, loan_number_id, customer_id, session_id=None, nonce=None, pretty_print=False):
        request_model = AddIncomeRequest(loan_number_id=loan_number_id, customer_id=customer_id,
                                             session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
                                             pretty_print=pretty_print)
        return self.post(resource_endpoint=ApiEndpoints.ADD_INCOME, response_model=AddIncomeResponse,
                         params=request_model.as_params_dict, data=request_model.payload)

    def set_incomes(self, loan_number_id, payload_dict=None, session_id=None, nonce=None, pretty_print=False, **kwargs):
        request_model = SetIncomesRequest(loan_number_id=loan_number_id, payload_dict=payload_dict,
                                         session_id=self._get_session_id(session_id),
                                         nonce=self._get_nonce(nonce), pretty_print=pretty_print, **kwargs)
        return self.post(resource_endpoint=ApiEndpoints.SET_INCOMES, response_model=CommonResponse,
                        params=request_model.as_params_dict, data=request_model.as_json, headers=self.json_headers)

    def delete_income(self, loan_number_id, customer_id, income_id, session_id=None, nonce=None, pretty_print=False):
        request_model = DeleteIncomeRequest(loan_number_id=loan_number_id, customer_id=customer_id, income_id=income_id,
                                           session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
                                           pretty_print=pretty_print)
        return self.post(resource_endpoint=ApiEndpoints.DELETE_INCOME, response_model=CommonResponse,
                         params=request_model.as_params_dict, data=request_model.payload)
