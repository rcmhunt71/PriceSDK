from dataclasses import dataclass

from APIs.security.requests.check_fee_system_privilege import CheckFeeSystemPrivilegeRequest
from APIs.security.requests.check_loan_privilege_multiple import CheckLoanPrivilegeMultipleRequest
from APIs.security.requests.check_system_privilege import CheckSystemPrivilegeRequest
from APIs.security.responses.check_loan_privilege_multiple import CheckLoanPrivilegeMultipleResponse
from APIs.security.responses.check_system_privilege import CheckSystemPrivilegeResponse, CheckFeeSystemPrivilegeResponse
from base.common.models.request import LoanNumberIdRequestModel
from base.clients.base_client import BaseClient

from APIs.security.responses.get_loan_privilege import GetLoanPrivilegeResponse


@dataclass
class ApiEndpoints:
    GET_LOAN_PRIVILEGE: str = "get_loan_privilege"
    CHECK_FEE_SYSTEM_PRIVILEGE: str = "check_fee_system_privilege"
    CHECK_LOAN_PRIVILEGE_MULTIPLE: str = "check_loan_privilege_multiple"
    CHECK_SYSTEM_PRIVILEGE: str = "check_system_privilege"


class SecurityClient(BaseClient):

    def get_loan_privilege(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
                                                 session_id=self._get_session_id(session_id),
                                                 nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_LOAN_PRIVILEGE, response_model=GetLoanPrivilegeResponse,
                        params=request_model.as_params_dict)

    def check_fee_system_privilege(self, fee_number, fee_item, requested_right, session_id=None, nonce=None,
            pretty_print=False):
        request_model = CheckFeeSystemPrivilegeRequest(fee_number=fee_number, fee_item=fee_item,
            requested_right=requested_right, session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
            pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.CHECK_FEE_SYSTEM_PRIVILEGE,
            response_model=CheckFeeSystemPrivilegeResponse, params=request_model.as_params_dict)

    def check_loan_privilege_multiple(self, fee_numbers, fee_items, requested_rights, session_id=None, nonce=None,
            pretty_print=False):
        request_model = CheckLoanPrivilegeMultipleRequest(fee_numbers=fee_numbers, fee_items=fee_items,
            requested_rights=requested_rights, session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
            pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.CHECK_LOAN_PRIVILEGE_MULTIPLE,
            response_model=CheckLoanPrivilegeMultipleResponse, params=request_model.as_params_dict)

    def check_system_privilege(self, loan_number_id, screen, requested_right, field_name=None, session_id=None,
            nonce=None, pretty_print=False):
        request_model = CheckSystemPrivilegeRequest(loan_number_id=loan_number_id, screen=screen, field_name=field_name,
            requested_right=requested_right, session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
            pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.CHECK_SYSTEM_PRIVILEGE,
            response_model=CheckSystemPrivilegeResponse, params=request_model.as_params_dict)
