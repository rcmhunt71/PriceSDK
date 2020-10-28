from dataclasses import dataclass

from APIs.dates.responses.get_dates import GetDatesResponse
from base.clients.base_client import BaseClient
from base.common.models.request import LoanNumberIdRequestModel


@dataclass
class ApiEndpoints:
    GET_DATES: str = "get_dates"


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
