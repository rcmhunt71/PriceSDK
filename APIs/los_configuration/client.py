from dataclasses import dataclass

from APIs.los_configuration.requests.get_loan_search_id_list import GetLoanSearchIdListRequest
from APIs.los_configuration.responses.get_configuration_list import GetConfigurationListResponse
from APIs.los_configuration.requests.get_configuration_list import GetConfigurationListRequest, \
    GetConfigurationListMultipleRequest
from APIs.los_configuration.requests.get_loan_pipeline import GetLoanPipelineRequest
from APIs.los_configuration.requests.get_program import GetProgramRequest
from APIs.los_configuration.requests.run_query import RunQueryRequest
from APIs.los_configuration.requests.run_query_grid_fields import RunQueryGridFieldsRequest
from APIs.los_configuration.responses.get_configuration_list_multiple import GetConfigurationListMultipleResponse
from APIs.los_configuration.responses.get_fees import GetFeesResponse
from APIs.los_configuration.responses.get_loan_pipeline import GetLoanPipelineResponse
from APIs.los_configuration.responses.get_loan_search_id_list import GetLoanSearchIdListResponse
from APIs.los_configuration.responses.get_loan_status_config import GetLoanStatusConfigResponse
from APIs.los_configuration.responses.get_program import GetProgramResponse
from APIs.los_configuration.responses.get_property_types import GetPropertyTypesResponse
from APIs.los_configuration.responses.run_query import RunQueryResponse
from APIs.los_configuration.responses.run_query_grid_fields import RunQueryGridFieldsResponse
from base.common.models.request import SimpleRequestModel
from base.clients.base_client import BaseClient


@dataclass
class ApiEndpoints:
    GET_CONFIGURATION_LIST: str = "get_configuration_list"
    GET_CONFIGURATION_LIST_MULTIPLE: str = "get_configuration_list_multiple"
    GET_FEES: str = "get_fees"
    GET_LOAN_PIPELINE: str = "get_loan_pipeline"
    GET_LOAN_SEARCH_ID_LIST: str = "get_loan_search_id_list"
    GET_LOAN_STATUS_CONFIG: str = "get_loan_status_config"
    GET_PROGRAM: str = "get_program"
    GET_PROPERTY_TYPES: str = "get_property_types"
    RUN_QUERY: str = "run_query"
    RUN_QUERY_GRID_FIELDS: str = "run_query_grid_fields"


class LOSConfigurationClient(BaseClient):
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"
    json_headers = {CONTENT_TYPE: APPLICATION_JSON}

    def get_configuration_list(self, list_name, session_id=None, nonce=None, pretty_print=False):
        request_model = GetConfigurationListRequest(list_name=list_name, session_id=self._get_session_id(session_id),
            nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_CONFIGURATION_LIST,
            response_model=GetConfigurationListResponse, params=request_model.as_params_dict)

    def get_configuration_list_multiple(self, list_name, session_id=None, nonce=None, pretty_print=False):
        request_model = GetConfigurationListMultipleRequest(list_name=list_name,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_CONFIGURATION_LIST_MULTIPLE,
            response_model=GetConfigurationListMultipleResponse, params=request_model.as_params_dict)

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

    def get_loan_search_id_list(self, query_id, other_params, field_to_search, condition_code, search_data,
                                check_security_privilege=None, session_id=None, nonce=None, pretty_print=False):
        request_model = GetLoanSearchIdListRequest(query_id=query_id, other_params=other_params,
                                                   field_to_search=field_to_search, condition_code=condition_code,
                                                   search_data=search_data,
                                                   check_security_privilege=check_security_privilege,
                                                   session_id=self._get_session_id(session_id),
                                                   nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_LOAN_SEARCH_ID_LIST,
                        response_model=GetLoanSearchIdListResponse, params=request_model.as_params_dict)

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

    def run_query(self, loan_id_list, loan_query_id, sort_field, sort_ascending, session_id=None, nonce=None,
            pretty_print=False):
        request_model = RunQueryRequest(loan_id_list=loan_id_list, loan_query_id=loan_query_id, sort_field=sort_field,
            sort_ascending=sort_ascending, session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
            pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.RUN_QUERY, response_model=RunQueryResponse,
            params=request_model.as_params_dict)

    def run_query_grid_fields(self, loan_query_id, sort_fields, sort_ascending, session_id=None, nonce=None,
            pretty_print=False):
        request_model = RunQueryGridFieldsRequest(loan_query_id=loan_query_id, sort_fields=sort_fields,
            sort_ascending=sort_ascending, session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
            pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.RUN_QUERY_GRID_FIELDS, response_model=RunQueryGridFieldsResponse,
            params=request_model.as_params_dict)
