from dataclasses import dataclass

from base.clients.base_client import BaseClient
from base.common.models.request import SimpleRequestModel

from APIs.passwords.responses.check_for_force_change_password import CheckForForceChangePasswordResponse


@dataclass
class ApiEndpoints:
    CHECK_FOR_FORCE_CHANGE_PASSWORD: str = "check_for_force_change_password"


class PasswordsClient(BaseClient):

    def check_for_force_change_password(self, session_id=None, nonce=None, pretty_print=False):
        request_model = SimpleRequestModel(session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
                                           pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.CHECK_FOR_FORCE_CHANGE_PASSWORD,
                        response_model=CheckForForceChangePasswordResponse, params=request_model.as_params_dict)
