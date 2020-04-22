from APIs.notification.models.email import EmailMergeKeys
from base.common.response import CommonResponse


class MergeEmailTemplate(CommonResponse):
    _ADD_KEYS = [EmailMergeKeys.SUBJECT, EmailMergeKeys.BODY]
    _SUB_MODELS = [None, None]
