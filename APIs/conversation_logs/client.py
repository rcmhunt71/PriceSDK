from dataclasses import dataclass
from APIs.conversation_logs.requests.add_conversation_log import AddConversationLogRequest
from APIs.conversation_logs.requests.get_conversation_log_alert import GetConversationLogAlertRequest
from APIs.conversation_logs.requests.get_conversation_log_attachment import GetConversationLogAttachmentRequest
from APIs.conversation_logs.requests.get_conversation_log_person import GetConversationLogPersonRequest
from APIs.conversation_logs.requests.set_conversation_log_person import SetConversationLogPersonRequest
from APIs.conversation_logs.responses.add_conversation_log import AddConversationLogResponse
from APIs.conversation_logs.responses.get_conversation_log import GetConversationLogResponse
from APIs.conversation_logs.responses.get_conversation_log_alert import GetConversationLogAlertResponse
from APIs.conversation_logs.responses.get_conversation_log_person import GetConversationLogPersonResponse
from base.clients.base_client import BaseClient
from base.common.models.request import LoanNumberIdRequestModel
from base.common.response import CommonResponse


@dataclass
class ApiEndpoints:
    GET_CONVERSATION_LOG: str = "get_conversation_log"
    GET_CONVERSATION_LOG_ALERT: str = "get_conversation_log_alert"
    GET_CONVERSATION_LOG_PERSON: str = "get_conversation_log_person"
    ADD_CONVERSATION_LOG: str = "add_conversation_log"
    GET_CONVERSATION_LOG_ATTACHMENT: str = "get_conversation_log_attachment"
    SET_CONVERSATION_LOG_PERSON: str = "set_conversation_log_person"


class ConversationLogsClient(BaseClient):
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"
    json_headers = {CONTENT_TYPE: APPLICATION_JSON}

    def get_conversation_log(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_CONVERSATION_LOG, response_model=GetConversationLogResponse,
            params=request_model.as_params_dict)

    def get_conversation_log_alert(self, loan_number_id, just_current_person=False, session_id=None, nonce=None,
            pretty_print=False):
        request_model = GetConversationLogAlertRequest(loan_number_id=loan_number_id,
            just_current_person=just_current_person, session_id=self._get_session_id(session_id),
            nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_CONVERSATION_LOG_ALERT,
            response_model=GetConversationLogAlertResponse, params=request_model.as_params_dict)

    def get_conversation_log_person(self, loan_number_id, just_current_person=False, session_id=None, nonce=None,
            pretty_print=False):
        request_model = GetConversationLogPersonRequest(loan_number_id=loan_number_id,
            just_current_person=just_current_person, session_id=self._get_session_id(session_id),
            nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_CONVERSATION_LOG_PERSON,
            response_model=GetConversationLogPersonResponse, params=request_model.as_params_dict)

    def add_conversation_log(self, loan_number_id, conversation_type, is_conversation_public, contact,
            related_to_memo_id, subject, memo, session_id=None, nonce=None, pretty_print=False):
        request_model = AddConversationLogRequest(loan_number_id=loan_number_id, conversation_type=conversation_type,
            is_conversation_public=is_conversation_public, contact=contact, related_to_memo_id=related_to_memo_id,
            subject=subject, memo=memo, session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
            pretty_print=pretty_print)
        return self.post(resource_endpoint=ApiEndpoints.ADD_CONVERSATION_LOG, response_model=AddConversationLogResponse,
            params=request_model.as_params_dict, data=request_model.payload)

    def get_conversation_log_attachment(self, loan_number_id, memo_id, session_id=None, nonce=None,
            pretty_print=False):
        request_model = GetConversationLogAttachmentRequest(loan_number_id=loan_number_id, memo_id=memo_id,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_CONVERSATION_LOG_ATTACHMENT, response_model=CommonResponse,
            params=request_model.as_params_dict)

    def set_conversation_log_person(self, payload_dict=None, session_id=None, nonce=None, pretty_print=False, **kwargs):
        request_model = SetConversationLogPersonRequest(payload_dict=payload_dict,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print,
            **kwargs)
        return self.post(resource_endpoint=ApiEndpoints.SET_CONVERSATION_LOG_PERSON, response_model=CommonResponse,
            params=request_model.as_params_dict, data=request_model.as_json, headers=self.json_headers)
