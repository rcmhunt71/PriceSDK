from dataclasses import dataclass
from APIs.tpo.requests.get_tpo_configurations import GetTPOConfigurationsRequest
from APIs.tpo.requests.get_tpo_queue_data import GetTPOQueueDataRequest
from APIs.tpo.responses.get_tpo_configurations import GetTPOConfigurationsResponse
from APIs.tpo.responses.get_tpo_queue_data import GetTPOQueueDataResponse
from base.clients.base_client import BaseClient


@dataclass
class ApiEndpoints:
    GET_TPO_CONFIGURATIONS: str = "get_tpo_configurations"
    GET_TPO_QUEUE_DATA: str = "get_tpo_queue_data"


class TPOClient(BaseClient):
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"
    json_headers = {CONTENT_TYPE: APPLICATION_JSON}

    def get_tpo_configurations(self, company_id, session_id=None, nonce=None, pretty_print=False):
        request_model = GetTPOConfigurationsRequest(company_id=company_id, session_id=self._get_session_id(session_id),
            nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_TPO_CONFIGURATIONS,
            response_model=GetTPOConfigurationsResponse, params=request_model.as_params_dict)

    def get_tpo_queue_data(self, company_id, contact_id, session_id=None, nonce=None, pretty_print=False):
        request_model = GetTPOQueueDataRequest(company_id=company_id, contact_id=contact_id,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_TPO_QUEUE_DATA, response_model=GetTPOQueueDataResponse,
            params=request_model.as_params_dict)
