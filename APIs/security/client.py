from dataclasses import dataclass

from base.common.models.request import LoanNumberIdRequestModel
from base.clients.base_client import BaseClient

from APIs.security.responses.get_loan_privilege import GetLoanPrivilegeResponse


@dataclass
class ApiEndpoints:
    GET_LOAN_PRIVILEGE: str = "get_loan_privilege"


class SecurityClient(BaseClient):

    def get_loan_privilege(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
                                                 session_id=self._get_session_id(session_id),
                                                 nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_LOAN_PRIVILEGE, response_model=GetLoanPrivilegeResponse,
                        params=request_model.as_params_dict)
