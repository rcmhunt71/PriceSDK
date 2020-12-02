from dataclasses import dataclass

from base.clients.base_client import BaseClient
from base.common.models.request import SimpleRequestModel
from base.common.response import CommonResponse

from APIs.session.requests.echo import EchoRequest
from APIs.session.responses.echo import EchoResponse
from APIs.session.responses.server_time import ServerTimeResponse
from APIs.session.responses.version import VersionResponse


@dataclass
class ApiEndpoints:
    ECHO: str = "echo"
    PING_SESSION: str = "ping_session"
    SERVER_TIME: str = "server_time"
    VERSION: str = "version"


class SessionClient(BaseClient):
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"
    json_headers = {
        CONTENT_TYPE: APPLICATION_JSON
    }

    def echo(self, payload_dict=None, session_id=None, nonce=None, pretty_print=False, **kwargs):
        request_model = EchoRequest(payload_dict=payload_dict, session_id=self._get_session_id(session_id),
                                    nonce=self._get_nonce(nonce), pretty_print=pretty_print, **kwargs)

        return self.post(resource_endpoint=ApiEndpoints.ECHO, response_model=EchoResponse,
                         params=request_model.as_params_dict, data=request_model.payload, headers=self.json_headers)

    def ping_session(self, session_id=None, nonce=None, pretty_print=False):
        request_model = SimpleRequestModel(session_id=self._get_session_id(session_id),
                                           nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.PING_SESSION, response_model=CommonResponse,
                         params=request_model.as_params_dict, data=request_model.payload)

    def server_time(self, pretty_print=False):
        args = {'PrettyPrint': pretty_print} if pretty_print else None

        return self.get(resource_endpoint=ApiEndpoints.SERVER_TIME, response_model=ServerTimeResponse, params=args)

    def version(self, pretty_print=False):
        args = {'PrettyPrint': pretty_print} if pretty_print else None

        return self.get(resource_endpoint=ApiEndpoints.VERSION, response_model=VersionResponse, params=args)
