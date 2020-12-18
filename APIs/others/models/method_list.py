from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class MethodListInfoKeys:
    NAME: str = "Name"
    IDEMPOTENT: str = "Idempotent"
    RESULT_TYPE: str = "ResultType"
    METHOD_ACCESS_CHECKED: str = "MethodAccessChecked"


@dataclass
class MethodListKeys:
    METHOD_LIST: str = "MethodList"


class MethodList(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(MethodListInfoKeys)]


class MethodLists(BaseListResponse):
    _SUB_MODEL = MethodList
