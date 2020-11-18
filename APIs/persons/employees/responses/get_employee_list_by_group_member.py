from APIs.persons.employees.models.employee_list_by_group_member import EmployeeListByGroupMemberLists, \
    EmployeeListByGroupMemberListKeys
from base.common.response import CommonResponse


class GetEmployeeListByGroupMemberResponse(CommonResponse):
    _ADD_KEYS = [EmployeeListByGroupMemberListKeys.EMPLOYEES]
    _SUB_MODELS = [EmployeeListByGroupMemberLists]

