from dataclasses import dataclass

from base.clients.base_client import BaseClient
from base.common.models.request import SimpleRequestModel

from APIs.databases.requests.get_db_column_info import GetDbColumnInfoRequest

from APIs.databases.responses.get_db_column_info import GetDbColumnInfoResponse
from APIs.databases.responses.get_db_table_names import GetDbTableNamesResponse


@dataclass
class ApiEndpoints:
    GET_DB_COLUMN_INFO: str = "get_db_column_info"
    GET_DB_TABLE_NAMES: str = "get_db_table_names"


class DatabasesClient(BaseClient):

    def get_db_column_info(self, table_name, session_id=None, nonce=None, pretty_print=False):
        request_model = GetDbColumnInfoRequest(table_name=table_name, session_id=self._get_session_id(session_id),
                                               nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_DB_COLUMN_INFO, response_model=GetDbColumnInfoResponse,
                        params=request_model.as_params_dict)

    def get_db_table_names(self, session_id=None, nonce=None, pretty_print=False):
        request_model = SimpleRequestModel(session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
                                           pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_DB_TABLE_NAMES, response_model=GetDbTableNamesResponse,
                        params=request_model.as_params_dict)
