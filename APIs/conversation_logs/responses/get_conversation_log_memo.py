from dataclasses import dataclass
from base.common.response import CommonResponse


@dataclass
class GetConversationLogMemoKeys:
    CONVERSATION_LOG_MEMO: str = "ConversationLogMemo"


class GetConversationLogMemoResponse(CommonResponse):
    _ADD_KEYS = [GetConversationLogMemoKeys.CONVERSATION_LOG_MEMO]
    _SUB_MODELS = [None]
