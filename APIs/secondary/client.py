from dataclasses import dataclass

from base.common.models.request import LoanNumberIdRequestModel
from base.clients.base_client import BaseClient
from base.common.response import CommonResponse

from APIs.secondary.requests.set_adjustment import SetAdjustmentRequest
from APIs.secondary.responses.get_adjustment_data import GetAdjustmentDataResponse


@dataclass
class ApiEndpoints:
    GET_ADJUSTMENT_DATA: str = "get_adjustment_data"
    SET_ADJUSTMENT: str = "set_adjustment"


class SecondaryClient(BaseClient):
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"
    json_headers = {
        CONTENT_TYPE: APPLICATION_JSON
    }

    def get_adjustment_data(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
                                                 session_id=self._get_session_id(session_id),
                                                 nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_ADJUSTMENT_DATA, response_model=GetAdjustmentDataResponse,
                        params=request_model.as_params_dict)

    def set_adjustment(self, loan_number_id, payload_dict=None, session_id=None, nonce=None, pretty_print=False,
                       **kwargs):
        request_model = SetAdjustmentRequest(loan_number_id=loan_number_id, payload_dict=payload_dict,
                                             session_id=self._get_session_id(session_id),
                                             nonce=self._get_nonce(nonce), pretty_print=pretty_print, **kwargs)

        return self.post(resource_endpoint=ApiEndpoints.SET_ADJUSTMENT, response_model=CommonResponse,
                         headers=self.json_headers, params=request_model.as_params_dict, data=request_model.payload)
