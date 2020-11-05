from dataclasses import dataclass

from APIs.fees.requests.delete_loan_fee import DeleteLoanFeeRequest
from base.clients.base_client import BaseClient

from APIs.fees.requests.add_loan_fee import AddLoanFeeRequest
from APIs.fees.responses.add_loan_fee import AddLoanFeeResponse
from base.common.response import CommonResponse


@dataclass
class ApiEndpoints:
    ADD_LOAN_FEE: str = "add_loan_fee"
    DELETE_LOAN_FEE: str = "delete_loan_fee"


class FeesClient(BaseClient):
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"
    json_headers = {
        CONTENT_TYPE: APPLICATION_JSON
    }

    def add_loan_fee(self, loan_number_id, fee_id, session_id=None, nonce=None, pretty_print=False):
        request_model = AddLoanFeeRequest(loan_number_id=loan_number_id, fee_id=fee_id,
                                          session_id=self._get_session_id(session_id),
                                          nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.ADD_LOAN_FEE, response_model=AddLoanFeeResponse,
                         params=request_model.as_params_dict, data=request_model.payload)

    def delete_loan_fee(self, loan_number_id, loan_fee_id, session_id=None, nonce=None, pretty_print=False):
        request_model = DeleteLoanFeeRequest(loan_number_id=loan_number_id, loan_fee_id=loan_fee_id,
                                             session_id=self._get_session_id(session_id),
                                             nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.DELETE_LOAN_FEE, response_model=CommonResponse,
                         params=request_model.as_params_dict, data=request_model.payload)
