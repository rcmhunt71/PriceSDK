from dataclasses import dataclass
from APIs.persons.employees.requests.get_employee_group_and_member_list import GetEmployeeGroupAndMemberListRequest
from APIs.persons.employees.requests.get_employee_id import GetEmployeeIDRequest
from APIs.persons.employees.requests.get_employee_list_by_group_member import GetEmployeeListByGroupMemberRequest
from APIs.persons.employees.responses.get_employee_group_and_member_list import GetEmployeeGroupAndMemberListResponse
from APIs.persons.employees.responses.get_employee_id import GetEmployeeIDResponse
from APIs.persons.employees.responses.get_employee_list_by_group_member import GetEmployeeListByGroupMemberResponse
from base.clients.base_client import BaseClient


@dataclass
class ApiEndpoints:
    GET_EMPLOYEE_GROUP_AND_MEMBER_LIST: str = "get_employee_group_and_member_list"
    GET_EMPLOYEE_ID: str = "get_employee_id"
    GET_EMPLOYEE_LIST_BY_GROUP_MEMBER: str = "get_employee_list_by_group_member"


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

