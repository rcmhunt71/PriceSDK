from dataclasses import dataclass

from base.clients.base_client import BaseClient
from base.common.models.request import LoanNumberIdRequestModel
from base.common.response import CommonResponse

from APIs.extra_and_virtual_data.requests.set_extra_data import SetExtraDataRequest
from APIs.extra_and_virtual_data.requests.get_virtual_data_grid import GetVirtualDataGridRequest
from APIs.extra_and_virtual_data.requests.put_virtual_data import PutVirtualDataRequest
from APIs.extra_and_virtual_data.requests.put_virtual_data_grid import PutVirtualDataGridRequest

from APIs.extra_and_virtual_data.responses.get_extra_data import GetExtraDataResponse
from APIs.extra_and_virtual_data.responses.get_virtual_data_grid import GetVirtualDataGridResponse


@dataclass
class ApiEndpoints:
    GET_EXTRA_DATA: str = "get_extra_data"
    SET_EXTRA_DATA: str = "set_extra_data"
    GET_VIRTUAL_DATA_GRID: str = "get_virtual_data_grid"
    PUT_VIRTUAL_DATA: str = "put_virtual_data"
    PUT_VIRTUAL_DATA_GRID: str = "put_virtual_data_grid"


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


class VirtualDataClient(BaseClient):
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"
    json_headers = {
        CONTENT_TYPE: APPLICATION_JSON
    }

    def get_virtual_data_grid(self, loan_number_id, table_name, session_id=None, nonce=None, pretty_print=False):
        request_model = GetVirtualDataGridRequest(loan_number_id=loan_number_id, table_name=table_name,
                                                  session_id=self._get_session_id(session_id),
                                                  nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_VIRTUAL_DATA_GRID, response_model=GetVirtualDataGridResponse,
                        params=request_model.as_params_dict)

    def put_virtual_data(self, loan_number_id, auto_append: bool = True, session_id=None, nonce=None,
                         pretty_print=False, **kwargs):
        """
        Format of sending keys can be controlled by auto_append:
            auto_append=True -> will append key to 'VirtualData-'
            auto_append=False -> will send key as is (without appending)
        """
        request_model = PutVirtualDataRequest(loan_number_id=loan_number_id, auto_append=auto_append,
                                              session_id=self._get_session_id(session_id),
                                              nonce=self._get_nonce(nonce), pretty_print=pretty_print, **kwargs)

        return self.post(resource_endpoint=ApiEndpoints.PUT_VIRTUAL_DATA, response_model=CommonResponse,
                         params=request_model.as_params_dict, data=request_model.payload)

    def put_virtual_data_grid(self, loan_number_id, payload_dict=None, session_id=None, nonce=None, pretty_print=False):
        """
        API endpoint doesn't support updating
        single FieldName & FieldValue -> **kwargs are not accepted
        """
        request_model = PutVirtualDataGridRequest(loan_number_id=loan_number_id, payload_dict=payload_dict,
                                                  session_id=self._get_session_id(session_id),
                                                  nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.PUT_VIRTUAL_DATA_GRID, response_model=CommonResponse,
                         headers=self.json_headers, params=request_model.as_params_dict, data=request_model.payload)
