from APIs.assets.models.assets import AssetsKeys, Assets
from base.common.response import CommonResponse


class GetAssetsResponse(CommonResponse):
    _ADD_KEYS = [AssetsKeys.ASSETS]
    _SUB_MODELS = [Assets]
