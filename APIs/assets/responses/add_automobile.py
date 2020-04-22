from APIs.assets.models.automobile import AutomobileKeys
from base.common.response import CommonResponse


class AddAutomobileResponse(CommonResponse):
    _ADD_KEYS = [AutomobileKeys.AUTOMOBILE_ID]
    _SUB_MODELS = [None]

