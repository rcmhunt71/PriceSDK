from dataclasses import dataclass

from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class ValidateResetPasswordTokenRequestParams(BaseRequestModelKeys):
    TOKEN: str = "Token"
    LOGIN_NAME: str = "LoginName"
    MAC_ADDRESS: str = "MACAddress"


class ValidateResetPasswordTokenRequest(SimpleRequestModel):
    def __init__(self, token, login_name, mac_address, session_id, nonce, pretty_print):
        self.token = token
        self.login_name = login_name
        self.mac_address = mac_address
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[ValidateResetPasswordTokenRequestParams.TOKEN] = self.token
        args[ValidateResetPasswordTokenRequestParams.LOGIN_NAME] = self.login_name
        args[ValidateResetPasswordTokenRequestParams.MAC_ADDRESS] = self.mac_address
        return args
