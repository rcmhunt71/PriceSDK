from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class GetConversationLogAttachmentRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    MEMO_ID: str = "MemoID"


class GetConversationLogAttachmentRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, memo_id, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.memo_id = memo_id
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetConversationLogAttachmentRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[GetConversationLogAttachmentRequestParams.MEMO_ID] = self.memo_id
        return args
