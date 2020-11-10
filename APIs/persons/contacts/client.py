from dataclasses import dataclass
from APIs.persons.contacts.requests.get_contact_ids import GetContactIDsRequest
from APIs.persons.contacts.requests.get_contact_group_member_list import GetContactGroupMemberListRequest
from APIs.persons.contacts.requests.get_contact_interface_credentials import GetContactInterfaceCredentialsRequest
from APIs.persons.contacts.requests.get_contact_user_groups import GetContactUserGroupsRequest
from APIs.persons.contacts.requests.get_contacts import GetContactsRequest
from APIs.persons.contacts.responses.get_contact_group_member_list import GetContactGroupMemberListResponse
from APIs.persons.contacts.responses.get_contact_ids import GetContactIDsResponse
from APIs.persons.contacts.responses.get_contact_interface_credentials import GetContactInterfaceCredentialsResponse
from APIs.persons.contacts.responses.get_contact_user_groups import GetContactUserGroupsResponse
from APIs.persons.contacts.responses.get_contacts import GetContactsResponse
from APIs.persons.contacts.responses.get_contacts_grid import GetContactsGridResponse
from base.common.models.request import LoanNumberIdRequestModel
from base.clients.base_client import BaseClient
from base.common.response import CommonResponse


@dataclass
class ApiEndpoints:
    GET_CONTACTS: str = "get_contacts"
    GET_CONTACTS_GRID: str = "get_contacts_grid"
    GET_CONTACT_IDS: str = "get_contact_ids"
    GET_CONTACT_USER_GROUPS: str = "get_contact_user_groups"
    GET_CONTACT_GROUP_MEMBER_LIST: str = "get_contact_group_member_list"
    GET_CONTACT_INTERFACE_CREDENTIALS: str = "get_contact_interface_credentials"


class ContactsClient(BaseClient):
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"
    json_headers = {CONTENT_TYPE: APPLICATION_JSON}

    def get_contacts(self, contact_id_list, session_id=None, nonce=None, pretty_print=False):
        request_model = GetContactsRequest(contact_id_list=contact_id_list, session_id=self._get_session_id(session_id),
            nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_CONTACTS, response_model=GetContactsResponse,
            params=request_model.as_params_dict)

    def get_contacts_grid(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_CONTACTS_GRID, response_model=GetContactsGridResponse,
            params=request_model.as_params_dict)

    def get_contact_ids(self, company_status, contact_type, contact_name, contact_state, session_id=None, nonce=None,
            pretty_print=False):
        request_model = GetContactIDsRequest(company_status=company_status, contact_type=contact_type,
            contact_name=contact_name, contact_state=contact_state, session_id=self._get_session_id(session_id),
            nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_CONTACT_IDS, response_model=GetContactIDsResponse,
            params=request_model.as_params_dict)

    def get_contact_user_groups(self, contact_id, session_id=None, nonce=None, pretty_print=False):
        request_model = GetContactUserGroupsRequest(contact_id=contact_id, session_id=self._get_session_id(session_id),
            nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_CONTACT_USER_GROUPS,
            response_model=GetContactUserGroupsResponse, params=request_model.as_params_dict)

    def get_contact_group_member_list(self, contact_id, session_id=None, nonce=None, pretty_print=False):
        request_model = GetContactGroupMemberListRequest(contact_id=contact_id,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_CONTACT_GROUP_MEMBER_LIST,
            response_model=GetContactGroupMemberListResponse, params=request_model.as_params_dict)

    def get_contact_interface_credentials(self, company_id, contact_id, session_id=None, nonce=None,
            pretty_print=False):
        request_model = GetContactInterfaceCredentialsRequest(company_id=company_id, contact_id=contact_id,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_CONTACT_INTERFACE_CREDENTIALS,
            response_model=GetContactInterfaceCredentialsResponse, params=request_model.as_params_dict)
