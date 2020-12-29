from dataclasses import dataclass
from base.responses.base_response import BaseListResponse, BaseResponse


@dataclass
class GetCountiesInfoKeys:
    COUNTY_NAME: str = "CountyName"


@dataclass
class GetCountiesKeys:
    COUNTIES: str = "Counties"


class GetCounties(BaseResponse):
    _ADD_KEYS = [GetCountiesInfoKeys.COUNTY_NAME]


class GetCountiesList(BaseListResponse):
    _SUB_MODEL = GetCounties
