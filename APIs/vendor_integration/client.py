from dataclasses import dataclass

from APIs.vendor_integration.requests.export_to_interface import ExportToInterfaceRequest
from APIs.vendor_integration.requests.form_free_verification import FormFreeVerificationRequest
from APIs.vendor_integration.requests.get_last_interface_file import GetLastInterfaceFileRequest
from APIs.vendor_integration.requests.get_verification_data import GetVerificationDataRequest
from APIs.vendor_integration.responses.export_to_interface import ExportToInterfaceResponse
from APIs.vendor_integration.responses.form_free_verification import FormFreeVerificationResponse
from APIs.vendor_integration.responses.get_media_center_data import GetMediaCenterDataResponse
from APIs.vendor_integration.responses.get_verification_data import GetVerificationDataResponse
from base.clients.base_client import BaseClient
from base.common.models.request import LoanNumberIdRequestModel
from base.common.response import CommonResponse


@dataclass
class ApiEndpoints:
    GET_LAST_INTERFACE_FILE: str = "get_last_interface_file"
    GET_MEDIA_CENTER_DATA: str = "get_media_center_data"
    GET_VERIFICATION_DATA: str = "get_verification_data"
    EXPORT_TO_INTERFACE: str = "export_to_interface"
    FORM_FREE_VERIFICATION: str = "form_free_verification"


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

    def get_verification_data(self, loan_number_id, customer_id, session_id=None, nonce=None, pretty_print=False):
        request_model = GetVerificationDataRequest(loan_number_id=loan_number_id, customer_id=customer_id,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_VERIFICATION_DATA, response_model=GetVerificationDataResponse,
            params=request_model.as_params_dict)

    def export_to_interface(self, interface_type, flags, behavior, loan_number_id, session_id=None, nonce=None,
            pretty_print=False):
        request_model = ExportToInterfaceRequest(interface_type=interface_type, flags=flags, behavior=behavior,
            loan_number_id=loan_number_id, session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
            pretty_print=pretty_print)
        return self.post(resource_endpoint=ApiEndpoints.EXPORT_TO_INTERFACE, response_model=ExportToInterfaceResponse,
                         params=request_model.as_params_dict, data=request_model.payload)

    def form_free_verification(self, loan_number_id, borrower_id, request_type, session_id=None, nonce=None,
            pretty_print=False):
        request_model = FormFreeVerificationRequest(loan_number_id=loan_number_id, borrower_id=borrower_id,
            request_type=request_type, session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
            pretty_print=pretty_print)
        return self.post(resource_endpoint=ApiEndpoints.FORM_FREE_VERIFICATION,
            response_model=FormFreeVerificationResponse,
            params=request_model.as_params_dict, data=request_model.payload)
