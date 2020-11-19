from dataclasses import dataclass

from base.clients.base_client import BaseClient
from base.common.models.request import LoanNumberIdRequestModel
from base.common.response import CommonResponse

from APIs.fees.requests.add_loan_fee import AddLoanFeeRequest
from APIs.fees.requests.delete_loan_fee import DeleteLoanFeeRequest
from APIs.fees.requests.set_loan_fees import SetLoanFeesRequest
from APIs.fees.responses.add_loan_fee import AddLoanFeeResponse
from APIs.fees.responses.get_loan_fees import GetLoanFeesResponse


@dataclass
class ApiEndpoints:
    ADD_LOAN_FEE: str = "add_loan_fee"
    DELETE_LOAN_FEE: str = "delete_loan_fee"
    SET_LOAN_FEES: str = "set_loan_fees"
    GET_LOAN_FEES: str = "get_loan_fees"


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

    def set_loan_fees(self, loan_number_id, payload_dict=None, session_id=None, nonce=None, pretty_print=False, **kwargs):
        request_model = SetLoanFeesRequest(loan_number_id=loan_number_id, payload_dict=payload_dict,
                                           session_id=self._get_session_id(session_id),
                                           nonce=self._get_nonce(nonce), pretty_print=pretty_print, **kwargs)

        return self.post(resource_endpoint=ApiEndpoints.SET_LOAN_FEES, response_model=CommonResponse,
                         headers=self.json_headers, params=request_model.as_params_dict, data=request_model.payload)

    def get_loan_fees(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
                                                 session_id=self._get_session_id(session_id),
                                                 nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_LOAN_FEES, response_model=GetLoanFeesResponse,
                        params=request_model.as_params_dict)
