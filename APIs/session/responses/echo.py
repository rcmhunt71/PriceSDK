from base.common.response import CommonResponse
from APIs.session.models.session import EchoKeys


class EchoResponse(CommonResponse):
    _ADD_KEYS = [EchoKeys.MESSAGE]
    _SUB_MODELS = [None]
