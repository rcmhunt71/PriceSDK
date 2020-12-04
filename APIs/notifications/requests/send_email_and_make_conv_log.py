from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class SendEmailAndMakeConvLogRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    CONVERSATION_IS_PUBLIC: str = "ConversationIsPublic"
    TO_EMAIL_LIST: str = "ToEmailList"
    FROM_EMAIL_ADDRESS: str = "FromEmailAddress"
    CC_EMAIL_LIST: str = "CCEmailList"
    BCC_EMAIL_LIST: str = "BCCEmailList"
    SUBJECT: str = "Subject"
    EMAIL_BODY: str = "EmailBody"
    USE_PORTAL: str = "UsePortal"
    USE_QUIET_PORTAL: str = "UseQuietPortal"
    LOAN_DISCLOSURE_HISTORY_TIE_BREAKER: str = "LoanDisclosureHistoryTieBreaker"
    RELATED_TO_MEMO_ID: str = "RelatedToMemoID"
    CONTACT_OVERRIDE: str = "ContactOverride"
    CONVERSATION_LOG_HEADER: str = "ConversationLogHeader"
    CONVERSATION_LOG_FOOTER: str = "ConversationLogFooter"
    INCLUDE_SNAP_SHOT: str = "IncludeSnapShot"


class SendEmailAndMakeConvLogRequest(SimpleRequestModel):

    def __init__(self, loan_number_id, conversation_is_public, to_email_list, from_email_address, cc_email_list,
            bcc_email_list, subject, email_body, use_portal, use_quiet_portal, loan_disclosure_history_tie_breaker,
            related_to_memo_id, contact_override, conversation_log_header, conversation_log_footer, include_snap_shot,
            payload_dict, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.conversation_is_public = conversation_is_public
        self.to_email_list = to_email_list
        self.from_email_address = from_email_address
        self.cc_email_list = cc_email_list
        self.bcc_email_list = bcc_email_list
        self.subject = subject
        self.email_body = email_body
        self.use_portal = use_portal
        self.use_quiet_portal = use_quiet_portal
        self.loan_disclosure_history_tie_breaker = loan_disclosure_history_tie_breaker
        self.related_to_memo_id = related_to_memo_id
        self.contact_override = contact_override
        self.conversation_log_header = conversation_log_header
        self.conversation_log_footer = conversation_log_footer
        self.include_snap_shot = include_snap_shot
        super().__init__(payload=payload_dict, session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[SendEmailAndMakeConvLogRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[SendEmailAndMakeConvLogRequestParams.CONVERSATION_IS_PUBLIC] = self.conversation_is_public
        args[SendEmailAndMakeConvLogRequestParams.TO_EMAIL_LIST] = self.to_email_list
        args[SendEmailAndMakeConvLogRequestParams.FROM_EMAIL_ADDRESS] = self.from_email_address
        args[SendEmailAndMakeConvLogRequestParams.CC_EMAIL_LIST] = self.cc_email_list
        args[SendEmailAndMakeConvLogRequestParams.BCC_EMAIL_LIST] = self.bcc_email_list
        args[SendEmailAndMakeConvLogRequestParams.SUBJECT] = self.subject
        args[SendEmailAndMakeConvLogRequestParams.EMAIL_BODY] = self.email_body
        args[SendEmailAndMakeConvLogRequestParams.USE_PORTAL] = self.use_portal
        args[SendEmailAndMakeConvLogRequestParams.USE_QUIET_PORTAL] = self.use_quiet_portal
        args[SendEmailAndMakeConvLogRequestParams.LOAN_DISCLOSURE_HISTORY_TIE_BREAKER] = self.loan_disclosure_history_tie_breaker
        args[SendEmailAndMakeConvLogRequestParams.RELATED_TO_MEMO_ID] = self.related_to_memo_id
        args[SendEmailAndMakeConvLogRequestParams.CONTACT_OVERRIDE] = self.contact_override
        args[SendEmailAndMakeConvLogRequestParams.CONVERSATION_LOG_HEADER] = self.conversation_log_header
        args[SendEmailAndMakeConvLogRequestParams.CONVERSATION_LOG_FOOTER] = self.conversation_log_footer
        args[SendEmailAndMakeConvLogRequestParams.INCLUDE_SNAP_SHOT] = self.include_snap_shot
        return args
