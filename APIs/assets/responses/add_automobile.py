from APIs.assets.models.automobile import AutomobileKeys
from base.common.response import CommonResponse


class AddAutomobileResponse(CommonResponse):
    ADD_KEYS = [AutomobileKeys.AUTOMOBILE_ID]
    SUB_MODELS = [None]

