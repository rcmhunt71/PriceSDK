from dataclasses import dataclass

from base.clients.base_client import BaseClient
from base.common.models.request import SimpleRequestModel
from base.common.response import CommonResponse

from APIs.passwords.requests.set_lockout import SetLockoutRequest

from APIs.passwords.responses.check_for_force_change_password import CheckForForceChangePasswordResponse
from APIs.passwords.responses.get_employee_password_age import GetEmployeePasswordAgeResponse


@dataclass
class ApiEndpoints:
    CHECK_FOR_FORCE_CHANGE_PASSWORD: str = "check_for_force_change_password"
    GET_EMPLOYEE_PASSWORD_AGE: str = "get_employee_password_age"
    SET_LOCKOUT: str = "set_lockout"


class PasswordsClient(BaseClient):

    def check_for_force_change_password(self, session_id=None, nonce=None, pretty_print=False):
        request_model = SimpleRequestModel(session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
                                           pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.CHECK_FOR_FORCE_CHANGE_PASSWORD,
                        response_model=CheckForForceChangePasswordResponse, params=request_model.as_params_dict)

    def get_employee_password_age(self, session_id=None, nonce=None, pretty_print=False):
        request_model = SimpleRequestModel(session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
                                           pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_EMPLOYEE_PASSWORD_AGE,
                        response_model=GetEmployeePasswordAgeResponse, params=request_model.as_params_dict)

    def set_lockout(self, employee_id, lockout, session_id=None, nonce=None, pretty_print=False):
        request_model = SetLockoutRequest(employee_id=employee_id, lockout=lockout,
                                          session_id=self._get_session_id(session_id),
                                          nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.SET_LOCKOUT, response_model=CommonResponse,
                         params=request_model.as_params_dict, data=request_model.payload)
