from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class EmployeeListByGroupMemberListInfoKeys:
    EMPLOYEE_ID: str = "EmployeeID"
    FIRST_NAME: str = "FirstName"
    MIDDLE_NAME: str = "MiddleName"
    LAST_NAME: str = "LastName"


@dataclass
class EmployeeListByGroupMemberListKeys:
    EMPLOYEES: str = "Employees"


class EmployeeListByGroupMemberList(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(EmployeeListByGroupMemberListInfoKeys)]


class EmployeeListByGroupMemberLists(BaseListResponse):
    _SUB_MODEL = EmployeeListByGroupMemberList
