from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class CheckLoanPrivilegeMultipleInfoKeys:
    FEE_NUMBER: str = "FeeNumber"
    FEE_ITEM: str = "FeeItem"
    HAS_ACCESS: str = "HasAccess"


@dataclass
class CheckLoanPrivilegeMultipleKeys:
    FEE_RIGHTS: str = "FeeRights"


class CheckLoanPrivilegeMultiple(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(CheckLoanPrivilegeMultipleInfoKeys)]


class CheckLoanPrivilegeMultipleList(BaseListResponse):
    _SUB_MODEL = CheckLoanPrivilegeMultiple
