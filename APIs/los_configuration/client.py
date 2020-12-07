from dataclasses import dataclass
from APIs.los_configuration.requests.get_configuration_list import GetConfigurationListRequest
from APIs.los_configuration.requests.get_loan_pipeline import GetLoanPipelineRequest
from APIs.los_configuration.responses.get_configuration_list import GetConfigurationListResponse
from APIs.los_configuration.responses.get_fees import GetFeesResponse
from APIs.los_configuration.responses.get_loan_pipeline import GetLoanPipelineResponse
from base.common.models.request import SimpleRequestModel
from base.clients.base_client import BaseClient


@dataclass
class ApiEndpoints:
    GET_CONFIGURATION_LIST: str = "get_configuration_list"
    GET_FEES: str = "get_fees"
    GET_LOAN_PIPELINE: str = "get_loan_pipeline"


class LOSConfigurationClient(BaseClient):
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"
    json_headers = {CONTENT_TYPE: APPLICATION_JSON}

    def get_configuration_list(self, list_name, session_id=None, nonce=None, pretty_print=False):
        request_model = GetConfigurationListRequest(list_name=list_name, session_id=self._get_session_id(session_id),
            nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_CONFIGURATION_LIST,
            response_model=GetConfigurationListResponse, params=request_model.as_params_dict)

    def get_fees(self, session_id=None, nonce=None, pretty_print=False):
        request_model = SimpleRequestModel(session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
            pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_FEES, response_model=GetFeesResponse,
            params=request_model.as_params_dict)

    def get_loan_pipeline(self, loan_query_id, sort_ascending, sort_fields, session_id=None, nonce=None,
            pretty_print=False):
        request_model = GetLoanPipelineRequest(loan_query_id=loan_query_id, sort_ascending=sort_ascending,
            sort_fields=sort_fields, session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
            pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_LOAN_PIPELINE, response_model=GetLoanPipelineResponse,
            params=request_model.as_params_dict)
