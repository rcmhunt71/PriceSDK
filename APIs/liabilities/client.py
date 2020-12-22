from dataclasses import dataclass
from base.common.models.request import LoanNumberIdRequestModel
from APIs.liabilities.requests.add_liability import AddLiabilityRequest
from APIs.liabilities.requests.delete_liability import DeleteLiabilityRequest
from APIs.liabilities.requests.set_liabilities import SetLiabilitiesRequest
from APIs.liabilities.responses.add_liability import AddLiabilityResponse
from APIs.liabilities.responses.get_liabilities import GetLiabilitiesResponse
from base.clients.base_client import BaseClient
from base.common.response import CommonResponse


@dataclass
class ApiEndpoints:
    ADD_LIABILITY: str = "add_liability"
    DELETE_LIABILITY: str = "delete_liability"
    GET_LIABILITIES: str = "get_liabilities"
    SET_LIABILITIES: str = "set_liabilities"


class LiabilitiesClient(BaseClient):
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"
    json_headers = {
        CONTENT_TYPE: APPLICATION_JSON
    }

    def get_liabilities(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
                                         session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
                                         pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_LIABILITIES, response_model=GetLiabilitiesResponse,
                        params=request_model.as_params_dict)

    def add_liability(self, loan_number_id, customer_id, session_id=None, nonce=None, pretty_print=False):
        request_model = AddLiabilityRequest(loan_number_id=loan_number_id, customer_id=customer_id,
                                             session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
                                             pretty_print=pretty_print)
        return self.post(resource_endpoint=ApiEndpoints.ADD_LIABILITY, response_model=AddLiabilityResponse,
                         params=request_model.as_params_dict, data=request_model.payload)

    def set_liabilities(self, loan_number_id, payload_dict=None, session_id=None, nonce=None, pretty_print=False, **kwargs):
        request_model = SetLiabilitiesRequest(loan_number_id=loan_number_id, payload_dict=payload_dict,
                                         session_id=self._get_session_id(session_id),
                                         nonce=self._get_nonce(nonce), pretty_print=pretty_print, **kwargs)
        return self.post(resource_endpoint=ApiEndpoints.SET_LIABILITIES, response_model=CommonResponse,
                        params=request_model.as_params_dict, data=request_model.as_json, headers=self.json_headers)

    def delete_liability(self, loan_number_id, customer_id, liability_id, session_id=None, nonce=None, pretty_print=False):
        request_model = DeleteLiabilityRequest(loan_number_id=loan_number_id, customer_id=customer_id, liability_id=liability_id,
                                           session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
                                           pretty_print=pretty_print)
        return self.post(resource_endpoint=ApiEndpoints.DELETE_LIABILITY, response_model=CommonResponse,
                         params=request_model.as_params_dict, data=request_model.payload)
