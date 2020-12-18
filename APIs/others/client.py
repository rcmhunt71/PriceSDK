from dataclasses import dataclass

from APIs.others.requests.change_portal_password import ChangePortalPasswordRequest
from APIs.others.requests.html2pdf import HTML2PDFRequest
from APIs.others.requests.search_tokenkey import SearchTokenkeyRequest
from APIs.others.responses.clear_cache import ClearCacheResponse
from APIs.others.responses.method_list import MethodListResponse
from APIs.others.responses.search_tokenkey import SearchTokenkeyResponse
from APIs.others.responses.system_information import SystemInformationResponse
from base.clients.base_client import BaseClient
from base.common.models.request import SimpleRequestModel
from base.common.response import CommonResponse


@dataclass
class ApiEndpoints:
    CLEAR_CACHE: str = "clear_cache"
    HTML2PDF: str = "html2pdf"
    METHOD_LIST: str = "method_list"
    SEARCH_TOKENKEY: str = "search_tokenkey"
    SYSTEM_INFORMATION: str = "system_information"
    CHANGE_PORTAL_PASSWORD: str = "change_portal_password"


class OthersClient(BaseClient):
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"
    json_headers = {CONTENT_TYPE: APPLICATION_JSON}

    def clear_cache(self, session_id=None, nonce=None, pretty_print=False):
        request_model = SimpleRequestModel(session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
            pretty_print=pretty_print)
        return self.post(resource_endpoint=ApiEndpoints.CLEAR_CACHE, response_model=ClearCacheResponse,
            params=request_model.as_params_dict, data=request_model.payload)

    def html2pdf(self, html, zoom_factor, time_delay, paper_size, session_id=None, nonce=None, pretty_print=False):
        request_model = HTML2PDFRequest(html=html, zoom_factor=zoom_factor, time_delay=time_delay, paper_size=paper_size,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.HTML2PDF, response_model=CommonResponse,
            params=request_model.as_params_dict)

    def method_list(self, session_id=None, nonce=None, pretty_print=False):
        request_model = SimpleRequestModel(session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
            pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.METHOD_LIST, response_model=MethodListResponse,
            params=request_model.as_params_dict)

    def search_tokenkey(self, token_key, session_id=None, nonce=None, pretty_print=False):
        request_model = SearchTokenkeyRequest(token_key=token_key, session_id=self._get_session_id(session_id),
            nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.SEARCH_TOKENKEY, response_model=SearchTokenkeyResponse,
            params=request_model.as_params_dict)

    def system_information(self, pretty_print=False):
        args = {'PrettyPrint': pretty_print} if pretty_print else None
        return self.get(resource_endpoint=ApiEndpoints.SYSTEM_INFORMATION, response_model=SystemInformationResponse,
            params=args)

    def change_portal_password(self, loan_number_id, borrower_id, new_password, session_id=None, nonce=None,
            pretty_print=False):
        request_model = ChangePortalPasswordRequest(loan_number_id=loan_number_id, borrower_id=borrower_id,
            new_password=new_password, session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
            pretty_print=pretty_print)
        return self.post(resource_endpoint=ApiEndpoints.CHANGE_PORTAL_PASSWORD, response_model=CommonResponse,
            params=request_model.as_params_dict, data=request_model.payload)
