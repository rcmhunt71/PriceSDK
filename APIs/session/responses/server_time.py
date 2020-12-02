from base.common.response import CommonResponse
from APIs.session.models.session import ServerTimeKeys


class ServerTimeResponse(CommonResponse):
    _ADD_KEYS = [ServerTimeKeys.API_SERVER_TIME]
    _SUB_MODELS = [None]
