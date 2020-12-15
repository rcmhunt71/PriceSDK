from dataclasses import dataclass
from APIs.tpo.responses.get_tpo_roles import GetTPORolesResponse
from APIs.tpo.requests.set_tpo_approval_queue_data import SetTPOApprovalQueueDataRequest
from base.common.response import CommonResponse
from base.common.models.request import SimpleRequestModel
from APIs.tpo.requests.get_tpo_configurations import GetTPOConfigurationsRequest
from APIs.tpo.requests.get_tpo_queue_data import GetTPOQueueDataRequest
from APIs.tpo.responses.get_tpo_configurations import GetTPOConfigurationsResponse
from APIs.tpo.responses.get_tpo_queue_data import GetTPOQueueDataResponse
from base.clients.base_client import BaseClient


@dataclass
class ApiEndpoints:
    GET_TPO_CONFIGURATIONS: str = "get_tpo_configurations"
    GET_TPO_QUEUE_DATA: str = "get_tpo_queue_data"
    GET_TPO_ROLES: str = "get_tpo_roles"
    SET_TPO_APPROVAL_QUEUE_DATA: str = "set_tpo_approval_queue_data"


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

    def get_tpo_roles(self, session_id=None, nonce=None, pretty_print=False):
        request_model = SimpleRequestModel(session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
            pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_TPO_ROLES, response_model=GetTPORolesResponse,
            params=request_model.as_params_dict)

    def set_tpo_approval_queue_data(self, company_id, contact_id, edited_by_id, action_flag, mac_address,
            reset_link, payload_dict=None, session_id=None, nonce=None, pretty_print=False, **kwargs):
        request_model = SetTPOApprovalQueueDataRequest(company_id=company_id, contact_id=contact_id,
            edited_by_id=edited_by_id, action_flag=action_flag, mac_address=mac_address, reset_link=reset_link,
            payload_dict=payload_dict, session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
            pretty_print=pretty_print, **kwargs)
        return self.post(resource_endpoint=ApiEndpoints.SET_TPO_APPROVAL_QUEUE_DATA, response_model=CommonResponse,
            params=request_model.as_params_dict, data=request_model.payload, headers=self.json_headers)
