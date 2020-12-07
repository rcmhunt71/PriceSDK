from dataclasses import dataclass

from base.common.models.request import LoanNumberIdRequestModel
from base.clients.base_client import BaseClient

from APIs.secondary.responses.get_adjustment_data import GetAdjustmentDataResponse


@dataclass
class ApiEndpoints:
    GET_ADJUSTMENT_DATA: str = "get_adjustment_data"


class SecondaryClient(BaseClient):

    def get_adjustment_data(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
                                                 session_id=self._get_session_id(session_id),
                                                 nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_ADJUSTMENT_DATA, response_model=GetAdjustmentDataResponse,
                        params=request_model.as_params_dict)
