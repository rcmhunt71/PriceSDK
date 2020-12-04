from APIs.notifications.models.notifications import SendEmailAndMakeConvLogKeys
from base.common.response import CommonResponse


class SendEmailAndMakeConvLogResponse(CommonResponse):
    _ADD_KEYS = [SendEmailAndMakeConvLogKeys.MEMO_ID]
    _SUB_MODELS = [None]
