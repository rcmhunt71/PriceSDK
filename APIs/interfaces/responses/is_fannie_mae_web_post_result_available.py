from APIs.interfaces.models.is_fannie_mae_web_post_result_available import IsFannieMaeWebPostResultAvailableKeys
from base.common.response import CommonResponse


class IsFannieMaeWebPostResultAvailableResponse(CommonResponse):
    _ADD_KEYS = [IsFannieMaeWebPostResultAvailableKeys.IS_AVAILABLE,
                IsFannieMaeWebPostResultAvailableKeys.WEB_POST_RESULT]
    _SUB_MODELS = [None, None]
