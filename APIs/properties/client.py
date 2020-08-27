from dataclasses import dataclass
from enum import Enum

from APIs.properties.requests.add_property import AddPropertyRequest
from APIs.properties.responses.add_property import AddPropertyResponse
from APIs.properties.responses.get_property_liens import GetPropertyLiensResponse

from APIs.properties.requests.get_properties import GetPropertiesRequest, GetPropertyLiensRequest, \
    IsPresentAddressAndSubjectPropertyLinkedRequest
from APIs.properties.responses.get_properties import GetPropertiesResponse
from APIs.properties.responses.is_present_address_and_subject_property_linked import \
    IsPresentAddressAndSubjectPropertyLinkedResponse
from base.clients.base_client import BaseClient


@dataclass
class ApiEndpoints:
    GET_PROPERTIES: str = "get_properties"
    GET_PROPERTY_LIENS: str = "get_property_liens"
    IS_PRESENT_ADDRESS_AND_SUBJECT_PROPERTY_LINKED: str = "is_present_address_and_subject_property_linked"
    ADD_PROPERTY: str = "add_property"
    ADD_PROPERTY_LIEN: str = "add_property_lien"
    DELETE_PROPERTY: str = "delete_property"
    DELETE_PROPERTY_LIEN: str = "delete_property_lien"
    LINK_OR_UNLINK_PRESENT_ADDRESS_AND_SUBJECT_PROPERTY: str = "link_or_unlink_present_address_and_subject_property"
    SET_PROPERTY_DATA: str = "set_property_data"
    SET_PROPERTY_LIENS: str = "set_property_liens"


class PropertiesClient(BaseClient):
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"
    json_headers = {
        CONTENT_TYPE: APPLICATION_JSON
    }

    def get_properties(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = GetPropertiesRequest(loan_number_id=loan_number_id,
                                         session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
                                         pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_PROPERTIES, response_model=GetPropertiesResponse,
                        params=request_model.as_params_dict)


    def get_property_liens(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = GetPropertyLiensRequest(loan_number_id=loan_number_id,
                                         session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
                                         pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_PROPERTY_LIENS, response_model=GetPropertyLiensResponse,
                        params=request_model.as_params_dict)


    def is_present_address_and_subject_property_linked(self, loan_number_id,
                                                       session_id=None, nonce=None, pretty_print=False):
        request_model = IsPresentAddressAndSubjectPropertyLinkedRequest(loan_number_id=loan_number_id,
                                         session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
                                         pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.IS_PRESENT_ADDRESS_AND_SUBJECT_PROPERTY_LINKED,
                        response_model=IsPresentAddressAndSubjectPropertyLinkedResponse, params=request_model.as_params_dict)


    def add_property(self, loan_number_id, customer_id, session_id=None, nonce=None, pretty_print=False):
        request_model = AddPropertyRequest(loan_number_id=loan_number_id, customer_id=customer_id,
                                           session_id=self._get_session_id(session_id),
                                           nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.ADD_PROPERTY, response_model=AddPropertyResponse,
                         headers=self.json_headers, params=request_model.as_params_dict, data=request_model.payload)


    # POST
    # add_property_lien
    # POST
    # delete_property
    # POST
    # delete_property_lien
    # POST
    # link_or_unlink_present_address_and_subject_property
    # POST
    # set_property_data
    # POST
    # set_property_liens