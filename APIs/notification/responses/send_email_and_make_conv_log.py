from APIs.notification.models.email import EmailConvLogKeys
from base.common.response import CommonResponse


class SendEmailAndMakeConvLog(CommonResponse):
    _ADD_KEYS = [EmailConvLogKeys.MEMO_ID]
    _SUB_MODELS = [None]
