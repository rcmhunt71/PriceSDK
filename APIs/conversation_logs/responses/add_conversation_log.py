from dataclasses import dataclass
from base.common.response import CommonResponse


@dataclass
class AddConversationLogKeys:
    MEMO_ID: str = "MemoID"


class AddConversationLogResponse(CommonResponse):
    _ADD_KEYS = [AddConversationLogKeys.MEMO_ID]
    _SUB_MODELS = [None]
