from dataclasses import dataclass
from base.clients.base_client import BaseClient
from base.common.models.request import LoanNumberIdRequestModel
from base.common.response import CommonResponse

from APIs.loans.responses.get_loan import GetLoanResponse, GetLoanDetailResponse
from APIs.loans.responses.get_final_value_tags import GetFinalValueTagsResponse
from APIs.loans.responses.get_loan_license_data import GetLoanLicenseDataResponse
from APIs.loans.responses.get_loan_rate_quote_details import GetLoanRateQuoteDetailsResponse
from APIs.loans.responses.get_loan_statuses import GetLoanStatusesResponse
from APIs.loans.responses.get_loan_status_vendor_types import GetLoanStatusVendorTypesResponse
from APIs.loans.responses.get_loan_mi_detail import GetLoanMIDetailsResponse
from APIs.loans.responses.get_loan_sellers import GetLoanSellersResponse
from APIs.loans.responses.search_loan_unique_id import SearchLoanUniqueIdResponse
from APIs.loans.responses.export_loan import ExportLoanResponse

from APIs.loans.requests.merge_loan_change_table import MergeLoanChangeTableRequest
from APIs.loans.requests.get_loan import GetLoanRequest, GetLoanDetailRequest, GetFinalValueTagsRequest, \
                                         GetLoanRateQuoteDetailsRequest, GetLoanMIDetailRequest
from APIs.loans.requests.get_loan_license_data import GetLoanLicenseDataRequest
from APIs.loans.requests.get_loan_statuses import GetLoanStatusesRequest
from APIs.loans.requests.search_loan_unique_id import SearchLoanUniqueIdRequest
from APIs.loans.requests.set_anti_steering_data import SetAntiSteeringDataRequest
from APIs.loans.requests.set_loan_correspondent_adjustment import SetLoanCorrespondentAdjustmentRequest
from APIs.loans.requests.set_loan_data import SetLoanDataRequest
from APIs.loans.requests.set_loan_hmda import SetLoanHMDARequest
from APIs.loans.requests.set_loan_license_data import SetLoanLicenseDataRequest
from APIs.loans.requests.set_loan_rate_quote_details import SetLoanRateQuoteDetailsRequest
from APIs.loans.requests.set_loan_servicing_data import SetLoanServicingDataRequest
from APIs.loans.requests.add_or_update_loan_sellers import AddOrUpdateLoanSellersRequest
from APIs.loans.requests.set_loan_mi_grid_detail import SetLoanMIGridDetailRequest


@dataclass
class ApiEndpoints:
    ADD_OR_UPDATE_LOAN_SELLERS: str = "add_or_update_loan_sellers"
    EXPORT_LOAN: str = "export_loan"
    GET_FINAL_VALUE_TAG: str = "get_final_value_tags"
    GET_LOAN: str = "get_loan"
    GET_LOAN_DETAIL: str = "get_loan_detail"
    GET_LOAN_LICENSE_DATA: str = "get_loan_license_data"
    GET_LOAN_RATE_QUOTE_DETAILS: str = "get_loan_rate_quote_details"
    GET_LOAN_MI_DETAILS: str = "get_loan_mi_detail"
    GET_LOAN_STATUSES: str = "get_loan_statuses"
    GET_LOAN_STATUS_VENDOR_TYPES: str = "get_loan_status_vendor_types"
    GET_LOAN_SELLERS: str = "get_loan_sellers"
    MERGE_LOAN_CHANGE_TABLE: str = "merge_loan_change_table"
    SEARCH_LOAN_UNIQUE_ID: str = "search_loan_unique_id"
    SET_ANTI_STEERING_DATA: str = "set_anti_steering_data"
    SET_LOAN_CORRESPONDENT_ADJUSTMENT: str = "set_loan_correspondent_adjustment"
    SET_LOAN_DATA: str = "set_loan_data"
    SET_LOAN_HMDA: str = "set_loan_hmda"
    SET_LOAN_LICENSE_DATA: str = "set_loan_license_data"
    SET_LOAN_RATE_QUOTE_DETAILS: str = "set_loan_rate_quote_details"
    SET_LOAN_SERVICING_DATA: str = "set_loan_servicing_data"
    SET_LOAN_MI_GRID_DETAIL: str = "set_loan_mi_grid_detail"


class LoanClient(BaseClient):
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"
    json_headers = {
        CONTENT_TYPE: APPLICATION_JSON
    }

    def add_or_update_loan_sellers(self, loan_number_id=None, payload_dict=None, session_id=None, nonce=None,
                                   pretty_print=False, **kwargs):
        request_model = AddOrUpdateLoanSellersRequest(loan_number_id=loan_number_id, payload_dict=payload_dict,
                                                      session_id=self._get_session_id(session_id),
                                                      nonce=self._get_nonce(nonce), pretty_print=pretty_print, **kwargs)

        return self.post(resource_endpoint=ApiEndpoints.ADD_OR_UPDATE_LOAN_SELLERS, response_model=CommonResponse,
                         headers=self.json_headers, params=request_model.as_params_dict, data=request_model.as_json)

    def export_loan(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
                                                 session_id=self._get_session_id(session_id),
                                                 nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.EXPORT_LOAN, response_model=ExportLoanResponse,
                        params=request_model.as_params_dict)

    def merge_loan_change_table(self, loan_number_id, fannie_file: str, difference_xml: str, session_id=None,
                                nonce=None, pretty_print=False):
        request_model = MergeLoanChangeTableRequest(loan_number_id=loan_number_id, fannie_file=fannie_file,
                                                    difference_xml=difference_xml,
                                                    session_id=self._get_session_id(session_id),
                                                    nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.MERGE_LOAN_CHANGE_TABLE, response_model=CommonResponse,
                         params=request_model.as_params_dict, data=request_model.payload)

    def get_loan(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = GetLoanRequest(loan_number_id=loan_number_id,
                                       session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
                                       pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_LOAN, response_model=GetLoanResponse,
                        params=request_model.as_params_dict)

    def get_loan_detail(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = GetLoanDetailRequest(loan_number_id=loan_number_id, session_id=self._get_session_id(session_id),
                                             nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_LOAN_DETAIL, response_model=GetLoanDetailResponse,
                        params=request_model.as_params_dict)

    def get_final_value_tags(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = GetFinalValueTagsRequest(loan_number_id=loan_number_id,
                                                 session_id=self._get_session_id(session_id),
                                                 nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_FINAL_VALUE_TAG,
                        response_model=GetFinalValueTagsResponse, params=request_model.as_params_dict)

    def get_loan_license_data(self, loan_number_id, data_from, data_id,
                              session_id=None, nonce=None, pretty_print=False):
        request_model = GetLoanLicenseDataRequest(loan_number_id=loan_number_id, data_from=data_from, data_id=data_id,
                                                  session_id=self._get_session_id(session_id),
                                                  nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_LOAN_LICENSE_DATA,
                        response_model=GetLoanLicenseDataResponse, params=request_model.as_params_dict)

    def get_loan_rate_quote_details(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = GetLoanRateQuoteDetailsRequest(loan_number_id=loan_number_id,
                                                       session_id=self._get_session_id(session_id),
                                                       nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_LOAN_RATE_QUOTE_DETAILS,
                        response_model=GetLoanRateQuoteDetailsResponse, params=request_model.as_params_dict)

    def get_loan_mi_detail(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = GetLoanMIDetailRequest(loan_number_id=loan_number_id,
                                               session_id=self._get_session_id(session_id),
                                               nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_LOAN_MI_DETAILS, response_model=GetLoanMIDetailsResponse,
                        params=request_model.as_params_dict)

    def get_loan_statuses(self, loan_number_ids, session_id=None, nonce=None, pretty_print=False):
        request_model = GetLoanStatusesRequest(loan_number_ids=loan_number_ids,
                                               session_id=self._get_session_id(session_id),
                                               nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_LOAN_STATUSES, response_model=GetLoanStatusesResponse,
                        params=request_model.as_params_dict)

    def get_loan_status_vendor_types(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
                                                 session_id=self._get_session_id(session_id),
                                                 nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_LOAN_STATUS_VENDOR_TYPES,
                        response_model=GetLoanStatusVendorTypesResponse, params=request_model.as_params_dict)

    def get_loan_sellers(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
                                                 session_id=self._get_session_id(session_id),
                                                 nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_LOAN_SELLERS, response_model=GetLoanSellersResponse,
                        params=request_model.as_params_dict)

    def search_loan_unique_id(self, loan_number_id, search_mode, session_id=None, nonce=None, pretty_print=False):
        request_model = SearchLoanUniqueIdRequest(loan_number_id=loan_number_id, search_mode=search_mode,
                                                  session_id=self._get_session_id(session_id),
                                                  nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.SEARCH_LOAN_UNIQUE_ID, response_model=SearchLoanUniqueIdResponse,
                        params=request_model.as_params_dict)

    def set_anti_steering_data(self, loan_number_id, index=None, program_id=None, rate=None, loan_origination=None,
                               loan_discount=None, sales_price=None, value=None, base_loan_amount=None,
                               other_financing=None, payload_dict=None, session_id=None, nonce=None):
        request_model = SetAntiSteeringDataRequest(loan_number_id=loan_number_id, index=index, program_id=program_id,
                                                   rate=rate, loan_origination=loan_origination,
                                                   loan_discount=loan_discount, sales_price=sales_price, value=value,
                                                   base_loan_amount=base_loan_amount, other_financing=other_financing,
                                                   payload_dict=payload_dict,
                                                   session_id=self._get_session_id(session_id),
                                                   nonce=self._get_nonce(nonce))

        return self.post(resource_endpoint=ApiEndpoints.SET_ANTI_STEERING_DATA, response_model=CommonResponse,
                         headers=self.json_headers, params=request_model.as_params_dict, data=request_model.as_json)

    def set_loan_correspondent_adjustment(self, loan_number_id, payload_dict=None, session_id=None, nonce=None,
                                          pretty_print=False, **kwargs):
        request_model = SetLoanCorrespondentAdjustmentRequest(loan_number_id=loan_number_id, payload_dict=payload_dict,
                                                              session_id=self._get_session_id(session_id),
                                                              nonce=self._get_nonce(nonce),
                                                              pretty_print=pretty_print, **kwargs)

        return self.post(resource_endpoint=ApiEndpoints.SET_LOAN_CORRESPONDENT_ADJUSTMENT, headers=self.json_headers,
                         response_model=CommonResponse, params=request_model.as_params_dict, data=request_model.as_json)

    def set_loan_data(self, loan_number_id, payload_dict=None, session_id=None, nonce=None,
                      pretty_print=False, **kwargs):
        request_model = SetLoanDataRequest(loan_number_id=loan_number_id, payload_dict=payload_dict,
                                           session_id=self._get_session_id(session_id),
                                           nonce=self._get_nonce(nonce), pretty_print=pretty_print, **kwargs)

        return self.post(resource_endpoint=ApiEndpoints.SET_LOAN_DATA, response_model=CommonResponse,
                         headers=self.json_headers, params=request_model.as_params_dict, data=request_model.as_json)

    def set_loan_hmda(self, loan_number_id=None, payload_dict=None,
                      session_id=None, nonce=None, pretty_print=False, **kwargs):
        request_model = SetLoanHMDARequest(loan_number_id=loan_number_id, payload_dict=payload_dict,
                                           session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
                                           pretty_print=pretty_print, **kwargs)

        return self.post(resource_endpoint=ApiEndpoints.SET_LOAN_HMDA, response_model=CommonResponse,
                         headers=self.json_headers, params=request_model.as_params_dict, data=request_model.as_json)

    def set_loan_license_data(self, loan_number_id=None, session_id=None, nonce=None, pretty_print=False, **kwargs):
        request_model = SetLoanLicenseDataRequest(loan_number_id=loan_number_id,
                                                  session_id=self._get_session_id(session_id),
                                                  nonce=self._get_nonce(nonce), pretty_print=pretty_print, **kwargs)

        return self.post(resource_endpoint=ApiEndpoints.SET_LOAN_LICENSE_DATA, response_model=CommonResponse,
                         params=request_model.as_params_dict, data=request_model.payload)

    def set_loan_rate_quote_details(self, loan_number_id, vendor_name, payload_dict=None,
                                    session_id=None, nonce=None, pretty_print=False, **kwargs):
        request_model = SetLoanRateQuoteDetailsRequest(loan_number_id=loan_number_id,
                                                       vendor_name=vendor_name, payload_dict=payload_dict,
                                                       session_id=self._get_session_id(session_id),
                                                       nonce=self._get_nonce(nonce),
                                                       pretty_print=pretty_print, **kwargs)

        return self.post(resource_endpoint=ApiEndpoints.SET_LOAN_RATE_QUOTE_DETAILS, response_model=CommonResponse,
                         params=request_model.as_params_dict, headers=self.json_headers, data=request_model.as_json)

    def set_loan_servicing_data(self, loan_number_id, payload_dict=None, session_id=None, nonce=None,
                                pretty_print=False, **kwargs):
        # TODO: add tests
        request_model = SetLoanServicingDataRequest(loan_number_id=loan_number_id, payload_dict=payload_dict,
                                                    session_id=self._get_session_id(session_id),
                                                    nonce=self._get_nonce(nonce), pretty_print=pretty_print, **kwargs)

        return self.post(resource_endpoint=ApiEndpoints.SET_LOAN_SERVICING_DATA, response_model=CommonResponse,
                         headers=self.json_headers, params=request_model.as_params_dict, data=request_model.as_json)

    def set_loan_mi_grid_detail(self, loan_number_id, payload_dict=None,
                                session_id=None, nonce=None, pretty_print=False, **kwargs):
        request_model = SetLoanMIGridDetailRequest(loan_number_id=loan_number_id, payload_dict=payload_dict,
                                                   session_id=self._get_session_id(session_id),
                                                   nonce=self._get_nonce(nonce), pretty_print=pretty_print, **kwargs)

        return self.post(resource_endpoint=ApiEndpoints.SET_LOAN_MI_GRID_DETAIL,
                         response_model=CommonResponse,
                         params=request_model.as_params_dict, headers=self.json_headers, data=request_model.as_json)
