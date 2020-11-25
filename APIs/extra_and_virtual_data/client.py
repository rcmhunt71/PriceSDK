from dataclasses import dataclass

from base.clients.base_client import BaseClient
from base.common.models.request import LoanNumberIdRequestModel
from base.common.response import CommonResponse

from APIs.extra_and_virtual_data.requests.set_extra_data import SetExtraDataRequest
from APIs.extra_and_virtual_data.responses.get_extra_data import GetExtraDataResponse


@dataclass
class ApiEndpoints:
    GET_EXTRA_DATA: str = "get_extra_data"
    SET_EXTRA_DATA: str = "set_extra_data"


class ExtraDataClient(BaseClient):

    def get_extra_data(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
                                                 session_id=self._get_session_id(session_id),
                                                 nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_EXTRA_DATA, response_model=GetExtraDataResponse,
                        params=request_model.as_params_dict)

    def set_extra_data(self, loan_number_id, extra_data_name, extra_data_value, row_number_id, session_id=None,
                       nonce=None, pretty_print=False):
        request_model = SetExtraDataRequest(loan_number_id=loan_number_id, extra_data_name=extra_data_name,
                                            extra_data_value=extra_data_value, row_number_id=row_number_id,
                                            session_id=self._get_session_id(session_id),
                                            nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.SET_EXTRA_DATA, response_model=CommonResponse,
                         params=request_model.as_params_dict, data=request_model.payload)
