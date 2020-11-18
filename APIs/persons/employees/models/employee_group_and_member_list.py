from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class EmployeeGroupAndMemberListInfoKeys:
    ID: str = "ID"
    NAME: str = "Name"


@dataclass
class EmployeeGroupAndMemberListKeys:
    GROUPS: str = "Groups"
    MEMBERS: str = "Members"


class EmployeeGroupsAndMemberList(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(EmployeeGroupAndMemberListInfoKeys)]


class EmployeeGroupAndMemberLists(BaseListResponse):
    _SUB_MODEL = EmployeeGroupsAndMemberList

