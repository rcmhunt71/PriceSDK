from dataclasses import dataclass
from APIs.los_configuration.requests.get_configuration_list import GetConfigurationListRequest
from APIs.los_configuration.requests.get_loan_pipeline import GetLoanPipelineRequest
from APIs.los_configuration.requests.get_program import GetProgramRequest
from APIs.los_configuration.responses.get_configuration_list import GetConfigurationListResponse
from APIs.los_configuration.responses.get_fees import GetFeesResponse
from APIs.los_configuration.responses.get_loan_pipeline import GetLoanPipelineResponse
from APIs.los_configuration.responses.get_loan_status_config import GetLoanStatusConfigResponse
from APIs.los_configuration.responses.get_program import GetProgramResponse
from APIs.los_configuration.responses.get_property_types import GetPropertyTypesResponse
from base.common.models.request import SimpleRequestModel
from base.clients.base_client import BaseClient


@dataclass
class ApiEndpoints:
    GET_CONFIGURATION_LIST: str = "get_configuration_list"
    GET_FEES: str = "get_fees"
    GET_LOAN_PIPELINE: str = "get_loan_pipeline"
    GET_LOAN_STATUS_CONFIG: str = "get_loan_status_config"
    GET_PROGRAM: str = "get_program"
    GET_PROPERTY_TYPES: str = "get_property_types"


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

    def get_loan_status_config(self, session_id=None, nonce=None, pretty_print=False):
        request_model = SimpleRequestModel(session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
            pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_LOAN_STATUS_CONFIG,
            response_model=GetLoanStatusConfigResponse, params=request_model.as_params_dict)

    def get_program(self, other_params=None, program_category=None, finance_method=None, prepay_penalty=None,
            loan_term_from=None, loan_term_to=None, investor_id=None, session_id=None, nonce=None, pretty_print=False):
        request_model = GetProgramRequest(other_params=other_params, program_category=program_category,
            finance_method=finance_method, prepay_penalty=prepay_penalty, loan_term_from=loan_term_from,
            loan_term_to=loan_term_to, investor_id=investor_id, session_id=self._get_session_id(session_id),
            nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_PROGRAM, response_model=GetProgramResponse,
            params=request_model.as_params_dict)

    def get_property_types(self, session_id=None, nonce=None, pretty_print=False):
        request_model = SimpleRequestModel(session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
            pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_PROPERTY_TYPES, response_model=GetPropertyTypesResponse,
            params=request_model.as_params_dict)
