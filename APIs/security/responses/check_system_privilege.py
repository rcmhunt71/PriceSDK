from dataclasses import dataclass
from base.common.response import CommonResponse


@dataclass
class CheckSystemPrivilegeKeys:
    HAS_ACCESS: str = "HasAccess"


class CheckSystemPrivilegeResponse(CommonResponse):
    _ADD_KEYS = [CheckSystemPrivilegeKeys.HAS_ACCESS]
    _SUB_MODELS = [None]


class CheckFeeSystemPrivilegeResponse(CheckSystemPrivilegeResponse):
    pass
