from base.common.response import CommonResponse
from APIs.properties.models.get_counties import GetCountiesKeys, GetCountiesList


class GetCountiesResponse(CommonResponse):
    _ADD_KEYS = [GetCountiesKeys.COUNTIES]
    _SUB_MODELS = [GetCountiesList]
