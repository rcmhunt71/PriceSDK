from dataclasses import dataclass

from base.common.models.request import SimpleRequestModel
from APIs.persons.requests.get_person_by_person_ids import GetPersonByPersonIDsRequest
from APIs.persons.requests.update_persons_by_person_id import UpdatePersonsByPersonIDRequest
from APIs.persons.responses.get_person_by_person_ids import GetPersonByPersonIDsResponse
from APIs.persons.responses.get_user_details import GetUserDetailsResponse
from base.clients.base_client import BaseClient
from base.common.response import CommonResponse


@dataclass
class ApiEndpoints:
    GET_PERSON_BY_PERSON_IDS: str = "get_person_by_person_ids"
    GET_USER_DETAILS: str = "get_user_details"
    UPDATE_PERSONS_BY_PERSON_ID: str = "update_persons_by_person_id"


class PersonsClient(BaseClient):
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"
    json_headers = {CONTENT_TYPE: APPLICATION_JSON}

    def get_person_by_person_ids(self, person_ids, session_id=None, nonce=None, pretty_print=False):
        request_model = GetPersonByPersonIDsRequest(person_ids=person_ids, session_id=self._get_session_id(session_id),
            nonce=self._get_nonce(nonce), pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_PERSON_BY_PERSON_IDS,
            response_model=GetPersonByPersonIDsResponse, params=request_model.as_params_dict)

    def get_user_details(self, session_id=None, nonce=None, pretty_print=False):
        request_model = SimpleRequestModel(session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
            pretty_print=pretty_print)
        return self.get(resource_endpoint=ApiEndpoints.GET_USER_DETAILS, response_model=GetUserDetailsResponse,
            params=request_model.as_params_dict)

    def update_persons_by_person_id(self, payload_dict=None, session_id=None, nonce=None, pretty_print=False, **kwargs):
        request_model = UpdatePersonsByPersonIDRequest(payload_dict=payload_dict,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print,
            **kwargs)
        return self.post(resource_endpoint=ApiEndpoints.UPDATE_PERSONS_BY_PERSON_ID, response_model=CommonResponse,
            params=request_model.as_params_dict, data=request_model.as_json, headers=self.json_headers)
