from dataclasses import dataclass
from APIs.correspondent.requests.set_loan_correspondent import SetLoanCorrespondentRequest
from APIs.correspondent.responses.get_loan_correspondent import GetLoanCorrespondentResponse
from base.common.models.request import LoanNumberIdRequestModel
from base.clients.base_client import BaseClient
from base.common.response import CommonResponse


@dataclass
class ApiEndpoints:
    GET_LOAN_CORRESPONDENT: str = "get_loan_correspondent"
    SET_LOAN_CORRESPONDENT: str = "set_loan_correspondent"


class CorrespondentClient(BaseClient):
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"
    json_headers = {CONTENT_TYPE: APPLICATION_JSON}

    def get_loan_correspondent(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_LOAN_CORRESPONDENT,
            response_model=GetLoanCorrespondentResponse, params=request_model.as_params_dict)

    def set_loan_correspondent(self, loan_number_id, payload_dict=None, session_id=None, nonce=None, pretty_print=False,
            **kwargs):
        request_model = SetLoanCorrespondentRequest(loan_number_id=loan_number_id, payload_dict=payload_dict,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print,
            **kwargs)
        return self.post(resource_endpoint=ApiEndpoints.SET_LOAN_CORRESPONDENT, response_model=CommonResponse,
            params=request_model.as_params_dict, data=request_model.as_json, headers=self.json_headers)
