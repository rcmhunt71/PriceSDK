from dataclasses import dataclass

from base.clients.base_client import BaseClient

from APIs.fees.requests.add_loan_fee import AddLoanFeeRequest
from APIs.fees.responses.add_loan_fee import AddLoanFeeResponse


@dataclass
class ApiEndpoints:
    ADD_LOAN_FEE: str = "add_loan_fee"


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
