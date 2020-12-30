from dataclasses import dataclass

from APIs.interfaces.requests.auto_import_pcado_download import AutoImportPcadoDownloadRequest
from APIs.interfaces.requests.auto_import_pcadu_download import AutoImportPcaduDownloadRequest
from APIs.interfaces.requests.direct_mismo_closing_data import DirectMISMOClosingDataRequest
from APIs.interfaces.requests.docutech_pushback_response import DocutechPushbackResponseRequest
from APIs.interfaces.requests.download_visionet_document import DownloadVisionetDocumentRequest
from APIs.interfaces.requests.get_interface_problems import GetInterfaceProblemsRequest
from APIs.interfaces.requests.get_ucd_fields import GetUCDFieldsRequest
from APIs.interfaces.requests.set_fnma_selling_system import SetFNMASellingSystemRequest
from APIs.interfaces.requests.set_import_interface import SetImportInterfaceRequest
from APIs.interfaces.requests.trigger_event import TriggerEventRequest
from APIs.interfaces.responses.get_interface_problems import GetInterfaceProblemsResponse
from APIs.interfaces.responses.get_ucd_fields import GetUCDFieldsResponse
from APIs.interfaces.responses.auto_import_pcado_download import AutoImportPcadoDownloadResponse
from APIs.interfaces.responses.auto_import_pcadu_download import AutoImportPcaduDownloadResponse
from APIs.interfaces.requests.upload_mercury_vmp_file import UploadMercuryVMPFileRequest
from APIs.interfaces.responses.merge_freddiemac_systosys import MergeFreddieMacSysToSysResponse
from APIs.interfaces.responses.request_freddiemac_systosys import RequestFreddieMacSysToSysResponse
from APIs.interfaces.responses.response_freddiemac_systosys import ResponseFreddieMacSysToSysResponse
from APIs.interfaces.responses.set_import_interface import SetImportInterfaceResponse
from base.clients.base_client import BaseClient
from base.common.models.request import LoanNumberIdRequestModel
from base.common.response import CommonResponse


@dataclass
class ApiEndpoints:
    AUTO_IMPORT_PCADO_DOWNLOAD: str = "auto_import_pcado_download"
    AUTO_IMPORT_PCADU_DOWNLOAD: str = "auto_import_pcadu_download"
    DOWNLOAD_VISIONET_DOCUMENT: str = "download_visionet_document"
    RESPONSE_FREDDIE_MAC_SYS_TO_SYS: str = "response_freddiemac_systosys"
    DOCUTECH_PUSHBACK_RESPONSE: str = "docutech_pushback_response"
    MERGE_FREDDIE_MAC_SYS_TO_SYS: str = "merge_freddiemac_systosys"
    REQUEST_FREDDIE_MAC_SYS_TO_SYS: str = "request_freddiemac_systosys"
    SET_FNMA_SELLING_SYSTEM: str = "set_fnma_selling_system"
    DIRECT_MISMO_CLOSING_DATA: str = "direct_mismo_closing_data"
    SET_IMPORT_INTERFACE: str = "set_import_interface"
    TRIGGER_EVENT: str = "trigger_event"
    GET_UCD_FIELDS: str = "get_ucd_fields"
    GET_INTERFACE_PROBLEMS: str = "get_interface_problems"
    UPLOAD_MERCURY_VMP_FILE: str = "upload_mercury_vmp_file"


class InterfacesClient(BaseClient):
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"
    json_headers = {CONTENT_TYPE: APPLICATION_JSON}

    def auto_import_pcado_download(self, loan_number, session_id=None, nonce=None, pretty_print=False):
        request_model = AutoImportPcadoDownloadRequest(loan_number=loan_number,
                                                       session_id=self._get_session_id(session_id),
                                                       nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.AUTO_IMPORT_PCADO_DOWNLOAD, data=request_model.payload,
                         response_model=AutoImportPcadoDownloadResponse, params=request_model.as_params_dict)

    def auto_import_pcadu_download(self, loan_number, session_id=None, nonce=None, pretty_print=False):
        request_model = AutoImportPcaduDownloadRequest(loan_number=loan_number,
                                                       session_id=self._get_session_id(session_id),
                                                       nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.AUTO_IMPORT_PCADU_DOWNLOAD, data=request_model.payload,
                         response_model=AutoImportPcaduDownloadResponse, params=request_model.as_params_dict)

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
            params=request_model.as_params_dict, data=request_model.as_json, headers=self.json_headers)

    def direct_mismo_closing_data(self, loan_number_id, which_interface, behavior, flags, session_id=None, nonce=None,
            pretty_print=False):
        request_model = DirectMISMOClosingDataRequest(loan_number_id=loan_number_id, which_interface=which_interface,
            behavior=behavior, flags=flags, session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
            pretty_print=pretty_print)
        return self.post(resource_endpoint=ApiEndpoints.DIRECT_MISMO_CLOSING_DATA, response_model=CommonResponse,
            params=request_model.as_params_dict, data=request_model.payload)

    def set_import_interface(self, loan_number, import_option, do_process_liabilities=None,
                             import_a_single_credit_report=None, session_id=None, nonce=None, pretty_print=False):
        request_model = SetImportInterfaceRequest(loan_number=loan_number, import_option=import_option,
                                                  do_process_liabilities=do_process_liabilities,
                                                  import_a_single_credit_report=import_a_single_credit_report,
                                                  session_id=self._get_session_id(session_id),
                                                  nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.SET_IMPORT_INTERFACE, response_model=SetImportInterfaceResponse,
                         params=request_model.as_params_dict, data=request_model.payload)

    def trigger_event(self, loan_number_id, event_id, session_id=None, nonce=None, pretty_print=False):
        request_model = TriggerEventRequest(loan_number_id=loan_number_id, event_id=event_id, pretty_print=pretty_print,
                                            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce))

        return self.post(resource_endpoint=ApiEndpoints.TRIGGER_EVENT, response_model=CommonResponse,
                         params=request_model.as_params_dict, data=request_model.payload)

    def get_ucd_fields(self, loan_number_id, interface_id, session_id=None, nonce=None, pretty_print=False):
        request_model = GetUCDFieldsRequest(loan_number_id=loan_number_id, interface_id=interface_id,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_UCD_FIELDS,
            response_model=GetUCDFieldsResponse, params=request_model.as_params_dict)

    def get_interface_problems(self, loan_number_id, borrower_list, which_interface, session_id=None, nonce=None,
            pretty_print=False):
        request_model = GetInterfaceProblemsRequest(loan_number_id=loan_number_id, borrower_list=borrower_list,
            which_interface=which_interface, session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
            pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_INTERFACE_PROBLEMS,
            response_model=GetInterfaceProblemsResponse, params=request_model.as_params_dict)

    def upload_mercury_vmp_file(self, loan_number_id, upload_token, hash, session_id=None, nonce=None,
            pretty_print=False):
        request_model = UploadMercuryVMPFileRequest(loan_number_id=loan_number_id, upload_token=upload_token, hash=hash,
            pretty_print=pretty_print, session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce))

        return self.post(resource_endpoint=ApiEndpoints.UPLOAD_MERCURY_VMP_FILE, response_model=CommonResponse,
                         params=request_model.as_params_dict, data=request_model.payload)
