from APIs.notifications.models.notifications import MergeEmailTemplateKeys
from base.common.response import CommonResponse


class MergeEmailTemplateResponse(CommonResponse):
    _ADD_KEYS = [MergeEmailTemplateKeys.SUBJECT, MergeEmailTemplateKeys.EMAIL_BODY]
    _SUB_MODELS = [None, None]
