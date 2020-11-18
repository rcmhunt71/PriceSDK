from APIs.persons.employees.models.employee_group_and_member_list import EmployeeGroupAndMemberLists, \
    EmployeeGroupAndMemberListKeys
from base.common.response import CommonResponse


class GetEmployeeGroupAndMemberListResponse(CommonResponse):
    _ADD_KEYS = [EmployeeGroupAndMemberListKeys.GROUPS, EmployeeGroupAndMemberListKeys.MEMBERS]
    _SUB_MODELS = [EmployeeGroupAndMemberLists, EmployeeGroupAndMemberLists]

