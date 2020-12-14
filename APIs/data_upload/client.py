from dataclasses import dataclass
from APIs.data_upload.requests.retrieve_data import RetrieveDataRequest
from APIs.data_upload.responses.register_parameter_set import RegisterParameterSetResponse
from APIs.data_upload.requests.process_string import ProcessStringRequest
from APIs.data_upload.requests.upload_data import UploadDataRequest
from APIs.data_upload.responses.process_string import ProcessStringResponse
from APIs.data_upload.responses.upload_data import UploadDataResponse
from base.clients.base_client import BaseClient
from base.common.models.request import SimpleRequestModel
from base.common.response import CommonResponse


@dataclass
class ApiEndpoints:
    PROCESS_STRING: str = "process_string"
    UPLOAD_DATA: str = "upload_data"
    REGISTER_PARAMETER_SET: str = "register_parameter_set"
    RETRIEVE_DATA: str = "retrieve_data"


class DataUploadClient(BaseClient):
    CONTENT_TYPE = "Content-Type"
    APPLICATION_OCTET = "application/octet-stream"
    ACCEPT_ENCODING = "Accept-Encoding"
    ENCODING_FORMAT = "deflate, gzip, identity"
    upload_headers = {CONTENT_TYPE: APPLICATION_OCTET, ACCEPT_ENCODING: ENCODING_FORMAT}

    def process_string(self, loan_number_id, parameter_set_key, data_language=None, session_id=None, nonce=None,
            pretty_print=False):
        request_model = ProcessStringRequest(loan_number_id=loan_number_id, parameter_set_key=parameter_set_key,
            data_language=data_language, session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
            pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.PROCESS_STRING, response_model=ProcessStringResponse,
            params=request_model.as_params_dict)

    def upload_data(self, token, append, type, payload_dict=None, session_id=None, nonce=None, pretty_print=False):
        request_model = UploadDataRequest(token=token, append=append, type=type, payload_dict=payload_dict,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.post(resource_endpoint=ApiEndpoints.UPLOAD_DATA, response_model=UploadDataResponse,
            params=request_model.as_params_dict, data=request_model.payload, headers=self.upload_headers)

    def register_parameter_set(self, payload_dict=None, session_id=None, nonce=None, pretty_print=False):
        request_model = SimpleRequestModel(payload=payload_dict, session_id=self._get_session_id(session_id),
            nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.post(resource_endpoint=ApiEndpoints.REGISTER_PARAMETER_SET,
            response_model=RegisterParameterSetResponse, params=request_model.as_params_dict,
            data=request_model.payload)

    def retrieve_data(self, token, type, hash, session_id=None, nonce=None, pretty_print=False):
        request_model = RetrieveDataRequest(token=token, type=type, hash=hash,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.RETRIEVE_DATA, response_model=CommonResponse,
            params=request_model.as_params_dict)
