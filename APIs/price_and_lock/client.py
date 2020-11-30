from dataclasses import dataclass

from base.clients.base_client import BaseClient
from base.common.models.request import SimpleRequestModel, LoanNumberIdRequestModel
from base.common.response import CommonResponse

from APIs.price_and_lock.requests.delete_pricing_adjustment import DeletePricingAdjustmentRequest
from APIs.price_and_lock.requests.make_commitment import MakeCommitmentRequest
from APIs.price_and_lock.requests.request_lock import RequestLockRequest


@dataclass
class ApiEndpoints:
    BREAK_LOCK: str = "break_lock"
    CONFIRM_LOCK: str = "confirm_lock"
    DELETE_PRICING_ADJUSTMENT: str = "delete_pricing_adjustment"
    MAKE_COMMITMENT: str = "make_commitment"
    PROCESS_LOCK: str = "process_lock"
    REQUEST_LOCK: str = "request_lock"


class PriceAndLockClient(BaseClient):
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"
    json_headers = {
        CONTENT_TYPE: APPLICATION_JSON
    }

    def break_lock(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
                                                 session_id=self._get_session_id(session_id),
                                                 nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.BREAK_LOCK, response_model=CommonResponse,
                         params=request_model.as_params_dict, data=request_model.payload)

    def confirm_lock(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
                                                 session_id=self._get_session_id(session_id),
                                                 nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.CONFIRM_LOCK, response_model=CommonResponse,
                         params=request_model.as_params_dict, data=request_model.payload)

    def delete_pricing_adjustment(self, loan_number_id, section_data, session_id=None, nonce=None, pretty_print=False):
        request_model = DeletePricingAdjustmentRequest(loan_number_id=loan_number_id, section_data=section_data,
                                                       session_id=self._get_session_id(session_id),
                                                       nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.DELETE_PRICING_ADJUSTMENT, response_model=CommonResponse,
                         params=request_model.as_params_dict, data=request_model.payload)

    def make_commitment(self, loan_number_id, investor_lock_date, investor_lock_expiration_date, investor_loan_number,
                        commitment_number, session_id=None, nonce=None, pretty_print=False):
        request_model = MakeCommitmentRequest(loan_number_id=loan_number_id, investor_lock_date=investor_lock_date,
                                              investor_lock_expiration_date=investor_lock_expiration_date,
                                              investor_loan_number=investor_loan_number,
                                              commitment_number=commitment_number,
                                              session_id=self._get_session_id(session_id),
                                              nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.MAKE_COMMITMENT, response_model=CommonResponse,
                         params=request_model.as_params_dict, data=request_model.payload)

    def process_lock(self, payload_dict=None, session_id=None, nonce=None, pretty_print=False):
        request_model = SimpleRequestModel(payload=payload_dict, session_id=self._get_session_id(session_id),
                                           nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.PROCESS_LOCK, response_model=CommonResponse,
                         headers=self.json_headers, params=request_model.as_params_dict, data=request_model.payload)

    def request_lock(self, loan_number_id, base_price, session_id=None, nonce=None, pretty_print=False):
        request_model = RequestLockRequest(loan_number_id=loan_number_id, base_price=base_price,
                                           session_id=self._get_session_id(session_id),
                                           nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.REQUEST_LOCK, response_model=CommonResponse,
                         params=request_model.as_params_dict, data=request_model.payload)
