from dataclasses import dataclass
from enum import Enum

from APIs.assets.requests.delete_automobile import DeleteAutomobileRequest

from APIs.assets.responses.delete_automobile import DeleteAutomobileResponse

from APIs.assets.responses.set_assets import SetAssetsResponse

from APIs.assets.requests.add_automobile import AddAutomobileRequest
from APIs.assets.requests.get_assets import GetAssetsRequest
from APIs.assets.requests.set_assets import SetAssetsRequest
from APIs.assets.responses.add_automobile import AddAutomobileResponse
from APIs.assets.responses.get_assets import GetAssetsResponse
from APIs.loans.requests.set_loan_servicing_data import SetLoanServicingDataRequest
from APIs.loans.responses.get_loan_mi_detail import GetLoanMIDetailsResponse
from APIs.loans.responses.set_loan_servicing_data import SetLoanServicingDataResponse

from base.clients.base_client import BaseClient
from base.common.models.request import SimpleRequestModel

from APIs.loans.responses.add_loan import AddALoanResponse, ImportFromFileResponse, ImportFromFileWithDateResponse
from APIs.loans.responses.get_loan import GetLoanResponse, GetLoanDetailResponse
from APIs.loans.responses.get_final_value_tags import GetFinalValueTagsResponse
from APIs.loans.responses.get_loan_license_data import GetLoanLicenseDataResponse
from APIs.loans.responses.get_loan_rate_quote_details import GetLoanRateQuoteDetailsResponse
from APIs.loans.responses.get_loan_statuses import GetLoanStatusesResponse
from APIs.loans.responses.set_anti_steering_data import SetAntiSteeringDataResponse
from APIs.loans.responses.set_loan_data import SetLoanDataResponse
from APIs.loans.responses.set_loan_hdma import SetLoanHMDAResponse
from APIs.loans.responses.set_loan_license_data import SetLoanLicenseDataResponse
from APIs.loans.responses.set_loan_rate_quote_details import SetLoanQuoteRateDetailsResponse

from APIs.loans.requests.add_loan import ImportFromFileRequest, ImportFromFileWithDateRequest
from APIs.loans.requests.get_loan import GetLoanRequest, GetLoanDetailRequest, GetFinalValueTagsRequest, \
    GetLoanRateQuoteDetailsRequest, GetLoanMIDetailRequest
from APIs.loans.requests.get_loan_license_data import GetLoanLicenseDataRequest
from APIs.loans.requests.get_loan_statuses import GetLoanStatusesRequest
from APIs.loans.requests.set_anti_steering_data import SetAntiSteeringDataRequest
from APIs.loans.requests.set_loan_data import SetLoanDataRequest
from APIs.loans.requests.set_loan_hmda import SetLoanHMDARequest
from APIs.loans.requests.set_loan_license_details import SetLoanLicenseDataRequest
from APIs.loans.requests.set_loan_rate_quote_details import SetLoanRateQuoteDetailsRequest


class ImportFromFileFileTypes(Enum):
    LOSFILE = 0
    FANNIE_MAE = 1
    MISMO_AUS = 2
    IHM = 3
    MISMO_NYLX = 4


@dataclass
class ApiEndpoints:
    ADD_AUTOMOBILE: str = "add_automobile"
    DELETE_AUTOMOBILE: str = "delete_automobile"
    GET_ASSETS: str = "get_assets"
    SET_ASSETS: str = "set_assets"


class AssetsClient(BaseClient):
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"
    json_headers = {
        CONTENT_TYPE: APPLICATION_JSON
    }

    def get_assets(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = GetAssetsRequest(loan_number_id=loan_number_id,
                                       session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
                                       pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_ASSETS, response_model=GetAssetsResponse,
                        params=request_model.as_params_dict)

    def add_automobile(self, loan_number_id, customer_id, session_id=None, nonce=None, pretty_print=False):
        request_model = AddAutomobileRequest(loan_number_id=loan_number_id, customer_id=customer_id,
                                       session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
                                       pretty_print=pretty_print)
        return self.post(resource_endpoint=ApiEndpoints.ADD_AUTOMOBILE, response_model=AddAutomobileResponse,
                        params=request_model.as_params_dict, data=request_model.payload)


    def set_assets(self, loan_number_id, payload_dict=None, session_id=None, nonce=None, pretty_print=False, **kwargs):
        # For valid arguments, use lowercase name of attributes listed in API.assets.requests.set_assets.SetAssetsRequests

        request_model = SetAssetsRequest(loan_number_id=loan_number_id, payload_dict=payload_dict,
                                           session_id=self._get_session_id(session_id),
                                           nonce=self._get_nonce(nonce), pretty_print=pretty_print, **kwargs)

        return self.post(resource_endpoint=ApiEndpoints.SET_ASSETS, response_model=SetAssetsResponse,
                        params=request_model.as_params_dict, data=request_model.payload)

    def delete_automobile(self, loan_number_id=None, customer_id=None, asset_id=None,
                      session_id=None, nonce=None, pretty_print=False):
        # For valid arguments, use lowercase name of attributes listed in API.loans.request.set_loan_hdma.SetLoanHMDAPayload

        request_model = DeleteAutomobileRequest(loan_number_id=loan_number_id, customer_id=customer_id, asset_id=asset_id,
                                           session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
                                           pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.DELETE_AUTOMOBILE, response_model=DeleteAutomobileResponse,
                         params=request_model.as_params_dict, data=request_model.payload)
