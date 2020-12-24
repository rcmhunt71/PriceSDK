from dataclasses import dataclass

from APIs.persons.contacts.requests.add_contact import AddContactRequest
from APIs.persons.contacts.requests.add_contact_license import AddContactLicenseRequest
from APIs.persons.contacts.requests.add_loan_contact import AddLoanContactRequest
from APIs.persons.contacts.requests.get_contact_ids import GetContactIDsRequest
from APIs.persons.contacts.requests.get_contact_group_member_list import GetContactGroupMemberListRequest
from APIs.persons.contacts.requests.get_contact_interface_credentials import GetContactInterfaceCredentialsRequest
from APIs.persons.contacts.requests.get_contact_user_groups import GetContactUserGroupsRequest
from APIs.persons.contacts.requests.get_contacts import GetContactsRequest
from APIs.persons.contacts.requests.set_contacts_grid import SetContactsGridRequest
from APIs.persons.contacts.responses.add_contact import AddContactResponse
from APIs.persons.contacts.requests.set_contact_interface_credential import SetContactInterfaceCredentialRequest
from APIs.persons.contacts.requests.set_contact_lockout import SetContactLockoutRequest
from APIs.persons.contacts.requests.set_contact_no_longer_employed import SetContactNoLongerEmployedRequest
from APIs.persons.contacts.requests.set_contacts import SetContactsRequest
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
    ADD_CONTACT: str = "add_contact"
    ADD_CONTACT_LICENSE: str = "add_contact_license"
    ADD_LOAN_CONTACT: str = "add_loan_contact"
    SET_CONTACT_INTERFACE_CREDENTIAL: str = "set_contact_interface_credential"
    SET_CONTACT_LOCKOUT: str = "set_contact_lockout"
    SET_CONTACTS: str = "set_contacts"
    SET_CONTACT_NO_LONGER_EMPLOYED: str = "set_contact_no_longer_employed"
    SET_CONTACTS_GRID: str = "set_contacts_grid"


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

    def add_contact(self, contact_type, field_name, field_value, session_id=None, nonce=None, pretty_print=False):
        request_model = AddContactRequest(contact_type=contact_type, field_name=field_name, field_value=field_value,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.ADD_CONTACT, response_model=AddContactResponse,
            params=request_model.as_params_dict)

    def add_contact_license(self, contact_id, license_name, license_number, license_start_date, license_end_date,
            license_state, state_default, lien_position, license_type, session_id=None, nonce=None, pretty_print=False):
        request_model = AddContactLicenseRequest(contact_id=contact_id, license_name=license_name,
            license_number=license_number, license_start_date=license_start_date, license_end_date=license_end_date,
            license_state=license_state, state_default=state_default, lien_position=lien_position,
            license_type=license_type, session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
            pretty_print=pretty_print)
        return self.post(resource_endpoint=ApiEndpoints.ADD_CONTACT_LICENSE, response_model=CommonResponse,
            params=request_model.as_params_dict, data=request_model.payload)

    def add_loan_contact(self, loan_number_id, contact_id, company_id, contact_setup_id, session_id=None, nonce=None,
            pretty_print=False):
        request_model = AddLoanContactRequest(loan_number_id=loan_number_id, contact_id=contact_id,
            company_id=company_id, contact_setup_id=contact_setup_id, session_id=self._get_session_id(session_id),
            nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.post(resource_endpoint=ApiEndpoints.ADD_LOAN_CONTACT, response_model=CommonResponse,
            params=request_model.as_params_dict, data=request_model.payload)

    def set_contact_interface_credential(self, company_id, contact_id, interface_type, interface_data_name,
            interface_password, session_id=None, nonce=None, pretty_print=False):
        request_model = SetContactInterfaceCredentialRequest(company_id=company_id, contact_id=contact_id,
            interface_type=interface_type, interface_data_name=interface_data_name, interface_password=interface_password,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
            pretty_print=pretty_print)
        return self.post(resource_endpoint=ApiEndpoints.SET_CONTACT_INTERFACE_CREDENTIAL, response_model=CommonResponse,
            params=request_model.as_params_dict, data=request_model.payload)

    def set_contact_lockout(self, contact_id, locked_out, session_id=None, nonce=None, pretty_print=False):
        request_model = SetContactLockoutRequest(contact_id=contact_id, locked_out=locked_out,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.post(resource_endpoint=ApiEndpoints.SET_CONTACT_LOCKOUT, response_model=CommonResponse,
            params=request_model.as_params_dict, data=request_model.payload)

    def set_contact_no_longer_employed(self, contact_id, no_longer_employed, session_id=None, nonce=None, pretty_print=False):
        request_model = SetContactNoLongerEmployedRequest(contact_id=contact_id, no_longer_employed=no_longer_employed,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.post(resource_endpoint=ApiEndpoints.SET_CONTACT_NO_LONGER_EMPLOYED, response_model=CommonResponse,
            params=request_model.as_params_dict, data=request_model.payload)

    def set_contacts(self, payload_dict=None, session_id=None, nonce=None, pretty_print=False, **kwargs):
        request_model = SetContactsRequest(payload_dict=payload_dict, session_id=self._get_session_id(session_id),
            nonce=self._get_nonce(nonce), pretty_print=pretty_print, **kwargs)
        return self.post(resource_endpoint=ApiEndpoints.SET_CONTACTS, response_model=CommonResponse,
            params=request_model.as_params_dict, data=request_model.as_json, headers=self.json_headers)

    def set_contacts_grid(self, loan_number_id, payload_dict=None, session_id=None, nonce=None, pretty_print=False,
            **kwargs):
        request_model = SetContactsGridRequest(loan_number_id=loan_number_id, payload_dict=payload_dict,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print,
            **kwargs)
        return self.post(resource_endpoint=ApiEndpoints.SET_CONTACTS_GRID, response_model=CommonResponse,
            params=request_model.as_params_dict, data=request_model.as_json, headers=self.json_headers)
