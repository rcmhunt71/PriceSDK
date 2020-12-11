from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class AddConversationLogRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    CONVERSATION_TYPE: str = "ConversationType"
    IS_CONVERSATION_PUBLIC: str = "IsConversationPublic"
    CONTACT: str = "Contact"
    RELATED_TO_MEMO_ID: str = "RelatedToMemoID"
    SUBJECT: str = "Subject"
    MEMO: str = "Memo"


class AddConversationLogRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, conversation_type, is_conversation_public, contact, related_to_memo_id, subject,
            memo, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.conversation_type = conversation_type
        self.is_conversation_public = is_conversation_public
        self.contact = contact
        self.related_to_memo_id = related_to_memo_id
        self.subject = subject
        self.memo = memo
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[AddConversationLogRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[AddConversationLogRequestParams.CONVERSATION_TYPE] = self.conversation_type
        args[AddConversationLogRequestParams.IS_CONVERSATION_PUBLIC] = self.is_conversation_public
        args[AddConversationLogRequestParams.CONTACT] = self.contact
        args[AddConversationLogRequestParams.RELATED_TO_MEMO_ID] = self.related_to_memo_id
        args[AddConversationLogRequestParams.SUBJECT] = self.subject
        args[AddConversationLogRequestParams.MEMO] = self.memo
        return args
