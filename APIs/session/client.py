from dataclasses import dataclass

from base.clients.base_client import BaseClient

from APIs.session.responses.server_time import ServerTimeResponse
from APIs.session.responses.version import VersionResponse


@dataclass
class ApiEndpoints:
    SERVER_TIME: str = "server_time"
    VERSION: str = "version"


class SessionClient(BaseClient):

    def server_time(self, pretty_print=False):
        args = {'PrettyPrint': pretty_print} if pretty_print else None

        return self.get(resource_endpoint=ApiEndpoints.SERVER_TIME, response_model=ServerTimeResponse,
                        params=args)

    def version(self, pretty_print=False):
        args = {'PrettyPrint': pretty_print} if pretty_print else None

        return self.get(resource_endpoint=ApiEndpoints.VERSION, response_model=VersionResponse,
                        params=args)
