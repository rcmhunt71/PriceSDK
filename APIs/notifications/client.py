from dataclasses import dataclass

from APIs.notifications.requests.merge_email_template import MergeEmailTemplateRequest
from APIs.notifications.requests.send_email_and_make_conv_log import SendEmailAndMakeConvLogRequest
from APIs.notifications.responses.merge_email_template import MergeEmailTemplateResponse
from APIs.notifications.responses.send_email_and_make_conv_log import SendEmailAndMakeConvLogResponse
from base.clients.base_client import BaseClient


@dataclass
class ApiEndpoints:
    MERGE_EMAIL_TEMPLATE: str = "merge_email_template"
    SEND_EMAIL_AND_MAKE_CONV_LOG: str = "send_email_and_make_conv_log"


class NotificationsClient(BaseClient):
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"
    json_headers = {CONTENT_TYPE: APPLICATION_JSON}

    def merge_email_template(self, loan_number_id, to_email_list, cc_email_list, bcc_email_list, email_template_id,
            session_id=None, nonce=None, pretty_print=False):
        request_model = MergeEmailTemplateRequest(loan_number_id=loan_number_id, to_email_list=to_email_list,
            cc_email_list=cc_email_list, bcc_email_list=bcc_email_list, email_template_id=email_template_id,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.MERGE_EMAIL_TEMPLATE, response_model=MergeEmailTemplateResponse,
            params=request_model.as_params_dict)

    def send_email_and_make_conv_log(self, loan_number_id, conversation_is_public, to_email_list, from_email_address,
            subject, email_body, cc_email_list=None, bcc_email_list=None, use_portal=None, use_quiet_portal=None,
            loan_disclosure_history_tie_breaker=None, related_to_memo_id=None, contact_override=None,
            conversation_log_header=None, conversation_log_footer=None, include_snap_shot=None, payload_dict=None,
            session_id=None, nonce=None, pretty_print=False):
        request_model = SendEmailAndMakeConvLogRequest(loan_number_id=loan_number_id,
            conversation_is_public=conversation_is_public, to_email_list=to_email_list, from_email_address=from_email_address,
            cc_email_list=cc_email_list, bcc_email_list=bcc_email_list, subject=subject, email_body=email_body,
            use_portal=use_portal, use_quiet_portal=use_quiet_portal,
            loan_disclosure_history_tie_breaker=loan_disclosure_history_tie_breaker,
            related_to_memo_id=related_to_memo_id, contact_override=contact_override,
            conversation_log_header=conversation_log_header, conversation_log_footer=conversation_log_footer,
            include_snap_shot=include_snap_shot, payload_dict=payload_dict, session_id=self._get_session_id(session_id),
            nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.SEND_EMAIL_AND_MAKE_CONV_LOG,
            response_model=SendEmailAndMakeConvLogResponse, params=request_model.as_params_dict,
            data=request_model.as_json, headers=self.json_headers)
