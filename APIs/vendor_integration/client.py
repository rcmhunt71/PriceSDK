from dataclasses import dataclass

from APIs.vendor_integration.requests.get_last_interface_file import GetLastInterfaceFileRequest
from APIs.vendor_integration.responses.get_media_center_data import GetMediaCenterDataResponse
from base.clients.base_client import BaseClient
from base.common.models.request import LoanNumberIdRequestModel
from base.common.response import CommonResponse


@dataclass
class ApiEndpoints:
    GET_LAST_INTERFACE_FILE: str = "get_last_interface_file"
    GET_MEDIA_CENTER_DATA: str = "get_media_center_data"


class VendorIntegrationClient(BaseClient):

    def get_last_interface_file(self, loan_number_id, which_interface, session_id=None, nonce=None, pretty_print=False):
        request_model = GetLastInterfaceFileRequest(loan_number_id=loan_number_id, which_interface=which_interface,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_LAST_INTERFACE_FILE,
            response_model=CommonResponse, params=request_model.as_params_dict)

    def get_media_center_data(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_MEDIA_CENTER_DATA, response_model=GetMediaCenterDataResponse,
            params=request_model.as_params_dict)
