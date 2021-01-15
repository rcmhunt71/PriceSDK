from dataclasses import dataclass
from base.clients.base_client import BaseClient
from base.common.models.request import LoanNumberIdRequestModel
from base.common.response import CommonResponse

from APIs.dates.requests.add_or_update_date import AddOrUpdateDateRequest
from APIs.dates.requests.set_dates import SetDatesRequest
from APIs.dates.responses.get_dates import GetDatesResponse


@dataclass
class ApiEndpoints:
    GET_DATES: str = "get_dates"
    ADD_OR_UPDATE_DATE: str = "add_or_update_date"
    SET_DATES: str = "set_dates"


class DatesClient(BaseClient):
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"
    json_headers = {
        CONTENT_TYPE: APPLICATION_JSON
    }

    def get_dates(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
                                                 session_id=self._get_session_id(session_id),
                                                 nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_DATES, response_model=GetDatesResponse,
                        params=request_model.as_params_dict)

    def add_or_update_date(self, loan_number_id, date_name, date_value, other_params,
                           session_id=None, nonce=None, pretty_print=False):
        request_model = AddOrUpdateDateRequest(loan_number_id=loan_number_id, date_name=date_name,
                                               date_value=date_value, other_params=other_params,
                                               session_id=self._get_session_id(session_id),
                                               nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.ADD_OR_UPDATE_DATE, response_model=CommonResponse,
                         params=request_model.as_params_dict, data=request_model.payload)

    def set_dates(self, loan_number_id, payload_dict=None, session_id=None, nonce=None, pretty_print=False):
        request_model = SetDatesRequest(loan_number_id=loan_number_id, payload_dict=payload_dict,
                                        session_id=self._get_session_id(session_id),
                                        nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.SET_DATES, response_model=CommonResponse,
                         headers=self.json_headers, params=request_model.as_params_dict, data=request_model.as_json)
