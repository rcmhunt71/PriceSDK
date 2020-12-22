from dataclasses import dataclass

from base.common.response import CommonResponse

from APIs.persons.employees.requests.add_or_update_employee import AddOrUpdateEmployeeRequest
from APIs.persons.employees.requests.get_employee_group_and_member_list import GetEmployeeGroupAndMemberListRequest
from APIs.persons.employees.requests.get_employee_id import GetEmployeeIDRequest
from APIs.persons.employees.requests.get_employee_list_by_group_member import GetEmployeeListByGroupMemberRequest
from APIs.persons.employees.requests.get_employees import GetEmployeesRequest
from APIs.persons.employees.requests.get_employees_with_param import GetEmployeesWithParamRequest
from APIs.persons.employees.responses.get_employee_group_and_member_list import GetEmployeeGroupAndMemberListResponse
from APIs.persons.employees.responses.get_employee_id import GetEmployeeIDResponse
from APIs.persons.employees.responses.get_employee_list_by_group_member import GetEmployeeListByGroupMemberResponse
from APIs.persons.employees.responses.get_employees import GetEmployeesResponse
from APIs.persons.employees.responses.get_employees_with_param import GetEmployeesWithParamResponse
from base.clients.base_client import BaseClient


@dataclass
class ApiEndpoints:
    GET_EMPLOYEE_GROUP_AND_MEMBER_LIST: str = "get_employee_group_and_member_list"
    GET_EMPLOYEE_ID: str = "get_employee_id"
    GET_EMPLOYEE_LIST_BY_GROUP_MEMBER: str = "get_employee_list_by_group_member"
    GET_EMPLOYEES: str = "get_employees"
    GET_EMPLOYEES_WITH_PARAM: str = "get_employees_with_param"
    ADD_OR_UPDATE_EMPLOYEE: str = "add_or_update_employee"


class EmployeesClient(BaseClient):
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"
    json_headers = {CONTENT_TYPE: APPLICATION_JSON
    }

    def get_employee_group_and_member_list(self, employee_id, session_id=None, nonce=None, pretty_print=False):
        request_model = GetEmployeeGroupAndMemberListRequest(employee_id=employee_id,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_EMPLOYEE_GROUP_AND_MEMBER_LIST,
            response_model=GetEmployeeGroupAndMemberListResponse, params=request_model.as_params_dict)

    def get_employee_id(self, employee_number, session_id=None, nonce=None, pretty_print=False):
        request_model = GetEmployeeIDRequest(employee_number=employee_number,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_EMPLOYEE_ID, response_model=GetEmployeeIDResponse,
            params=request_model.as_params_dict)

    def get_employee_list_by_group_member(self, member_ids, group_ids, session_id=None, nonce=None, pretty_print=False):
        request_model = GetEmployeeListByGroupMemberRequest(member_ids=member_ids, group_ids=group_ids,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_EMPLOYEE_LIST_BY_GROUP_MEMBER,
            response_model=GetEmployeeListByGroupMemberResponse, params=request_model.as_params_dict)

    def get_employees(self, employee_id_lists, session_id=None, nonce=None, pretty_print=False):
        request_model = GetEmployeesRequest(employee_id_lists=employee_id_lists,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_EMPLOYEES,
            response_model=GetEmployeesResponse, params=request_model.as_params_dict)

    def get_employees_with_param(self, last_name, employee_type, session_id=None, nonce=None, pretty_print=False):
        request_model = GetEmployeesWithParamRequest(last_name=last_name, employee_type=employee_type,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_EMPLOYEES_WITH_PARAM,
            response_model=GetEmployeesWithParamResponse, params=request_model.as_params_dict)

    def add_or_update_employee(self, payload_dict=None, session_id=None, nonce=None, pretty_print=False, **kwargs):
        request_model = AddOrUpdateEmployeeRequest(payload_dict=payload_dict, session_id=self._get_session_id(session_id),
            nonce=self._get_nonce(nonce), pretty_print=pretty_print, **kwargs)
        return self.post(resource_endpoint=ApiEndpoints.ADD_OR_UPDATE_EMPLOYEE, response_model=CommonResponse,
            params=request_model.as_params_dict, data=request_model.as_json, headers=self.json_headers)
