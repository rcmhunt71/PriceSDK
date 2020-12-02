from base.common.response import CommonResponse
from APIs.session.models.session import VersionKeys, Version


class VersionResponse(CommonResponse):
    _ADD_KEYS = [VersionKeys.PRICE_VERSION, VersionKeys.LOS_VERSION]
    _SUB_MODELS = [Version, Version]
