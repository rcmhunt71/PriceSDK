from dataclasses import dataclass

from APIs.assets.requests.delete_automobile import DeleteAutomobileRequest
from APIs.assets.requests.add_automobile import AddAutomobileRequest
from APIs.assets.requests.get_assets import GetAssetsRequest
from APIs.assets.requests.set_assets import SetAssetsRequest
from APIs.assets.responses.add_automobile import AddAutomobileResponse
from APIs.assets.responses.get_assets import GetAssetsResponse

from base.clients.base_client import BaseClient
from base.common.response import CommonResponse


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
        request_model = SetAssetsRequest(loan_number_id=loan_number_id, payload_dict=payload_dict,
                                         session_id=self._get_session_id(session_id),
                                         nonce=self._get_nonce(nonce), pretty_print=pretty_print, **kwargs)

        return self.post(resource_endpoint=ApiEndpoints.SET_ASSETS, response_model=CommonResponse,
                         params=request_model.as_params_dict, data=request_model.as_json, headers=self.json_headers)

    def delete_automobile(self, loan_number_id=None, customer_id=None, asset_id=None,
                          session_id=None, nonce=None, pretty_print=False):
        request_model = DeleteAutomobileRequest(loan_number_id=loan_number_id, customer_id=customer_id,
                                                asset_id=asset_id,
                                                session_id=self._get_session_id(session_id),
                                                nonce=self._get_nonce(nonce),
                                                pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.DELETE_AUTOMOBILE, response_model=CommonResponse,
                         params=request_model.as_params_dict, data=request_model.payload)
