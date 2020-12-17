from dataclasses import dataclass
from APIs.interfaces.requests.docutech_pushback_response import DocutechPushbackResponseRequest
from APIs.interfaces.requests.download_visionet_document import DownloadVisionetDocumentRequest
from APIs.interfaces.requests.set_fnma_selling_system import SetFNMASellingSystemRequest
from APIs.interfaces.responses.merge_freddiemac_systosys import MergeFreddieMacSysToSysResponse
from APIs.interfaces.responses.request_freddiemac_systosys import RequestFreddieMacSysToSysResponse
from APIs.interfaces.responses.response_freddiemac_systosys import ResponseFreddieMacSysToSysResponse
from base.clients.base_client import BaseClient
from base.common.models.request import LoanNumberIdRequestModel
from base.common.response import CommonResponse


@dataclass
class ApiEndpoints:
    DOWNLOAD_VISIONET_DOCUMENT: str = "download_visionet_document"
    RESPONSE_FREDDIE_MAC_SYS_TO_SYS: str = "response_freddiemac_systosys"
    DOCUTECH_PUSHBACK_RESPONSE: str = "docutech_pushback_response"
    MERGE_FREDDIE_MAC_SYS_TO_SYS: str = "merge_freddiemac_systosys"
    REQUEST_FREDDIE_MAC_SYS_TO_SYS: str = "request_freddiemac_systosys"
    SET_FNMA_SELLING_SYSTEM: str = "set_fnma_selling_system"


class InterfacesClient(BaseClient):
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"
    json_headers = {CONTENT_TYPE: APPLICATION_JSON}

    def download_visionet_document(self, job_id, app_id, app_secret, session_id=None, nonce=None, pretty_print=False):
        request_model = DownloadVisionetDocumentRequest(job_id=job_id, app_id=app_id, app_secret=app_secret,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.DOWNLOAD_VISIONET_DOCUMENT,
            response_model=CommonResponse, params=request_model.as_params_dict)

    def response_freddiemac_systosys(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.RESPONSE_FREDDIE_MAC_SYS_TO_SYS,
            response_model=ResponseFreddieMacSysToSysResponse, params=request_model.as_params_dict)

    def docutech_pushback_response(self, loan_number, token_key, hash, session_id=None, nonce=None, pretty_print=False):
        request_model = DocutechPushbackResponseRequest(loan_number=loan_number, token_key=token_key, hash=hash,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.post(resource_endpoint=ApiEndpoints.DOCUTECH_PUSHBACK_RESPONSE, response_model=CommonResponse,
            params=request_model.as_params_dict, data=request_model.payload)

    def merge_freddiemac_systosys(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.post(resource_endpoint=ApiEndpoints.MERGE_FREDDIE_MAC_SYS_TO_SYS,
            response_model=MergeFreddieMacSysToSysResponse,
            params=request_model.as_params_dict, data=request_model.payload)

    def request_freddiemac_systosys(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.post(resource_endpoint=ApiEndpoints.REQUEST_FREDDIE_MAC_SYS_TO_SYS,
            response_model=RequestFreddieMacSysToSysResponse,
            params=request_model.as_params_dict, data=request_model.payload)

    def set_fnma_selling_system(self, loan_number_id, payload_dict=None, session_id=None, nonce=None,
            pretty_print=False, **kwargs):
        request_model = SetFNMASellingSystemRequest(loan_number_id=loan_number_id, payload_dict=payload_dict,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print,
            **kwargs)
        return self.post(resource_endpoint=ApiEndpoints.SET_FNMA_SELLING_SYSTEM, response_model=CommonResponse,
            params=request_model.as_params_dict, data=request_model.payload, headers=self.json_headers)
