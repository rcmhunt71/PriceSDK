from dataclasses import dataclass
from enum import Enum

from APIs.loans.responses.get_loan_mi_detail import GetLoanMIDetailsResponse

from base.clients.base_client import BaseClient
from base.common.models.request import BaseRequestModel

from APIs.loans.responses.add_loan import AddALoanResponse, ImportFromFileResponse, ImportFromFileWithDateResponse
from APIs.loans.responses.get_loan import GetLoanResponse, GetLoanDetailResponse
from APIs.loans.responses.get_final_value_tags import GetFinalValueTagsResponse
from APIs.loans.responses.get_loan_license_data import GetLoanLicenseDataResponse
from APIs.loans.responses.get_loan_rate_quote_details import GetLoanRateQuoteDetailsResponse
from APIs.loans.responses.get_loan_statuses import GetLoanStatusesResponse
from APIs.loans.responses.set_anti_steering_data import SetAntiSteeringDataResponse
from APIs.loans.responses.set_loan_data import SetLoanDataResponse
from APIs.loans.responses.set_loan_hdma import SetLoanHDMAResponse
from APIs.loans.responses.set_loan_license_data import SetLoanLicenseDataResponse
from APIs.loans.responses.set_loan_rate_quote_details import SetLoanQuoteRateDetailsResponse

from APIs.loans.requests.add_loan import ImportFromFileRequest, ImportFromFileWithDateRequest
from APIs.loans.requests.get_loan import GetLoanRequest, GetLoanDetailRequest, GetFinalValueTagsRequest, \
    GetLoanRateQuoteDetailsRequest, GetLoanMIDetailRequest
from APIs.loans.requests.get_loan_license_data import GetLoanLicenseDataRequest
from APIs.loans.requests.get_loan_statuses import GetLoanStatusesRequest
from APIs.loans.requests.set_anti_steering_data import SetAntiSteeringDataRequest
from APIs.loans.requests.set_loan_data import SetLoanDataRequest
from APIs.loans.requests.set_loan_hmda import SetLoanHDMARequest
from APIs.loans.requests.set_loan_license_data import SetLoanLicenseDataRequest
from APIs.loans.requests.set_loan_rate_quote_data import SetLoanQuoteRateDataRequest


class ImportFromFileFileTypes(Enum):
    LOSFILE = 0
    FANNIE_MAE = 1
    MISMO_AUS = 2
    IHM = 3
    MISMO_NYLX = 4


@dataclass
class ApiEndpoints:
    ADD_A_LOAN: str = "add_a_loan"
    GET_FINAL_VALUE_TAG: str = "get_final_value_tags"
    GET_LOAN: str = "get_loan"
    GET_LOAN_DETAIL: str = "get_loan_detail"
    GET_LOAN_LICENSE_DATA: str = "get_loan_license_data"
    GET_LOAN_RATE_QUOTE_DETAILS: str = "get_loan_rate_quote_details"
    GET_LOAN_MI_DETAILS: str = "get_loan_mi_detail"
    GET_LOAN_STATUSES: str = "get_loan_statuses"
    IMPORT_FROM_FILE: str = "import_from_file"
    IMPORT_FROM_FILE_WITH_DATE: str = "import_from_file_with_date"
    SET_ANTI_STEERING_DATA: str = "set_anti_steering_data"
    SET_LOAN_DATA: str = "set_loan_data"
    SET_LOAN_HDMA: str = "set_loan_hdma"
    SET_LOAN_LICENSE_DATA: str = "set_loan_license_data"
    SET_LOAN_RATE_QUOTE_DETAILS: str = "set_loan_rate_quote_details"


class LoanClient(BaseClient):
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"
    headers = {
        CONTENT_TYPE: APPLICATION_JSON
    }

    def add_loan(self, session_id=None, nonce=None):
        request_model = BaseRequestModel(session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce))
        response_model = AddALoanResponse
        endpoint = ApiEndpoints.ADD_A_LOAN
        headers = {}

        response = self.post(resource_endpoint=endpoint, response_model=response_model, data={}, headers=headers,
                             params=request_model.as_params_dict)
        return response

    def import_from_file(self, loan_number, file_type, date_name, base64_file_data, session_id=None, nonce=None):
        request_model = ImportFromFileRequest(session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
                                              loan_number=loan_number, file_type=file_type, date_name=date_name,
                                              base64_file_data=base64_file_data)
        response_model = ImportFromFileResponse
        endpoint = ApiEndpoints.IMPORT_FROM_FILE
        headers = {}

        response = self.post(resource_endpoint=endpoint, response_model=response_model, data={}, headers=headers,
                             params=request_model.as_params_dict, binary_data=base64_file_data)
        return response

    def import_from_file_with_date(self, upload_token, file_type, loan_number, b2b_flag, date_name,
                                   session_id=None, nonce=None):
        request_model = ImportFromFileWithDateRequest(session_id=session_id or self.session_id,
                                                      nonce=nonce or self.nonce, loan_number=loan_number,
                                                      file_type=file_type, date_name=date_name, b2b_flag=b2b_flag,
                                                      upload_token=upload_token)
        response_model = ImportFromFileWithDateResponse
        endpoint = ApiEndpoints.IMPORT_FROM_FILE_WITH_DATE
        headers = {}

        response = self.post(resource_endpoint=endpoint, response_model=response_model, data={}, headers=headers,
                             params=request_model.as_params_dict)
        return response

    def get_loan(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = GetLoanRequest(loan_number_id=loan_number_id,
                                       session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
                                       pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_LOAN, response_model=GetLoanResponse,
                        params=request_model.as_params_dict)

    def get_loan_detail(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = GetLoanDetailRequest(loan_number_id=loan_number_id,
                                       session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
                                       pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_LOAN_DETAIL, response_model=GetLoanDetailResponse,
                        params=request_model.as_params_dict)

    def get_final_value_tags(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = GetFinalValueTagsRequest(loan_number_id=loan_number_id,
                                       session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
                                       pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_FINAL_VALUE_TAG,
                        response_model=GetFinalValueTagsResponse, params=request_model.as_params_dict)

    def get_loan_license_data(self, loan_number_ids, data_from, data_id,
                              session_id=None, nonce=None, pretty_print=False):
        request_model = GetLoanLicenseDataRequest(loan_number_ids=loan_number_ids, data_from=data_from, data_id=data_id,
                                                  session_id=self._get_session_id(session_id),
                                                  nonce=self._get_nonce(nonce),
                                                  pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_LOAN_LICENSE_DATA,
                            response_model=GetLoanLicenseDataResponse, params=request_model.as_params_dict)

    def get_loan_rate_quote_details(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = GetLoanRateQuoteDetailsRequest(loan_number_id=loan_number_id,
                                       session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
                                       pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_LOAN_RATE_QUOTE_DETAILS,
                            response_model=GetLoanRateQuoteDetailsResponse, params=request_model.as_params_dict)

    def get_loan_mi_detail(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = GetLoanMIDetailRequest(loan_number_id=loan_number_id,
                                       session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
                                       pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_LOAN_MI_DETAILS, response_model=GetLoanMIDetailsResponse,
                        params=request_model.as_params_dict)

    def get_loan_statuses(self, loan_number_ids, session_id=None, nonce=None, pretty_print=False):
        request_model = GetLoanStatusesRequest(loan_number_ids=loan_number_ids,
                                               session_id=self._get_session_id(session_id),
                                               nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_LOAN_STATUSES, response_model=GetLoanStatusesResponse,
                            params=request_model.as_params_dict)

    def set_anti_steering_data(self, loan_number_ids, index=None, program_id=None, rate=None, loan_origination=None,
                               loan_discount=None, sales_price=None, value=None, base_loan_amount=None,
                               other_financing=None, payload_dict=None, session_id=None, nonce=None):

        request_model = SetAntiSteeringDataRequest(session_id=self._get_session_id(session_id),
                                                   nonce=self._get_nonce(nonce),
                                                   loan_number_ids=loan_number_ids, index=index, program_id=program_id,
                                                   rate=rate, value=value, loan_discount=loan_discount,
                                                   loan_origination=loan_origination, base_loan_amount=base_loan_amount,
                                                   other_financing=other_financing, sales_price=sales_price,
                                                   payload_dict=payload_dict)
        response_model = SetAntiSteeringDataResponse
        endpoint = ApiEndpoints.SET_ANTI_STEERING_DATA

        response = self.post(resource_endpoint=endpoint, response_model=response_model, headers=self.headers,
                             params=request_model.as_params_dict, data=request_model.payload)
        return response

    def set_loan_data(self, loan_number_id, payload_dict=None, session_id=None, nonce=None, pretty_print=False, **kwargs):
        # For valid arguments, use lowercase name of attributes listed in API.loans.request.set_loan.SetLoanDataPayload

        request_model = SetLoanDataRequest(loan_number_id=loan_number_id, payload_dict=payload_dict,
                                           session_id=self._get_session_id(session_id),
                                           nonce=self._get_nonce(nonce), pretty_print=pretty_print, **kwargs)

        return self.post(resource_endpoint=ApiEndpoints.SET_LOAN_DATA, response_model=SetLoanDataResponse,
                         headers=self.headers, params=request_model.as_params_dict, data=request_model.payload)

    def set_loan_hdma(self, loan_number_ids=None, payload_dict=None, session_id=None, nonce=None, **kwargs):
        # For valid arguments, use lowercase name of attributes listed in API.loans.request.set_loan.SetLoanHDMARequest

        request_model = SetLoanHDMARequest(session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
                                           loan_number_ids=loan_number_ids, payload_dict=payload_dict, **kwargs)
        response_model = SetLoanHDMAResponse
        endpoint = ApiEndpoints.SET_LOAN_DATA

        response = self.post(resource_endpoint=endpoint, response_model=response_model, headers=self.headers,
                             params=request_model.as_params_dict, data=request_model.payload)
        return response

    def set_loan_license_data(self, loan_number_ids=None, session_id=None, nonce=None, **kwargs):
        # For valid arguments, use lowercase name of attributes listed in
        # API.loans.request.set_loan_license_data.SetLoanLicenseDataParams, provide via kwargs

        request_model = SetLoanLicenseDataRequest(
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
            loan_number_ids=loan_number_ids, **kwargs)
        response_model = SetLoanLicenseDataResponse
        endpoint = ApiEndpoints.SET_LOAN_LICENSE_DATA

        response = self.post(resource_endpoint=endpoint, response_model=response_model,
                             params=request_model.as_params_dict, data=request_model.payload)
        return response

    def set_loan_rate_quote_data(self, vendor_name, loan_number_ids, session_id=None, nonce=None, **kwargs):
        request_model = SetLoanQuoteRateDataRequest(
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
            vendor_name=vendor_name, loan_number_ids=loan_number_ids, **kwargs)
        response_model = SetLoanQuoteRateDetailsResponse
        endpoint = ApiEndpoints.SET_LOAN_RATE_QUOTE_DETAILS

        response = self.post(resource_endpoint=endpoint, response_model=response_model,
                             params=request_model.as_params_dict, data=request_model.payload)
        return response
