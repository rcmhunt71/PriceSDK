from APIs.assets.models.assets import AssetsKeys, Assets
from base.common.response import CommonResponse


class AssetsResponse(CommonResponse):
    ADD_KEYS = [AssetsKeys.ASSETS]
    SUB_MODELS = [Assets]
