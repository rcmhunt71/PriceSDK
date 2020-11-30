from dataclasses import dataclass

from base.clients.base_client import BaseClient
from base.common.models.request import SimpleRequestModel
from base.common.response import CommonResponse

from APIs.price_and_lock.requests.request_lock import RequestLockRequest


@dataclass
class ApiEndpoints:
    PROCESS_LOCK: str = "process_lock"
    REQUEST_LOCK: str = "request_lock"


class LockClient(BaseClient):
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"
    json_headers = {
        CONTENT_TYPE: APPLICATION_JSON
    }

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
