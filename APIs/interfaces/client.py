from dataclasses import dataclass
from APIs.interfaces.requests.download_visionet_document import DownloadVisionetDocumentRequest
from APIs.interfaces.responses.response_freddiemac_systosys import ResponseFreddieMacSysToSysResponse
from base.clients.base_client import BaseClient
from base.common.models.request import LoanNumberIdRequestModel
from base.common.response import CommonResponse


@dataclass
class ApiEndpoints:
    DOWNLOAD_VISIONET_DOCUMENT: str = "download_visionet_document"
    RESPONSE_FREDDIE_MAC_SYS_TO_SYS: str = "response_freddiemac_systosys"


class InterfacesClient(BaseClient):

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
