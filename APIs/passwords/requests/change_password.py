from dataclasses import dataclass

from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class ChangePasswordRequestParams(BaseRequestModelKeys):
    LOGIN_NAME: str = "LoginName"
    NEW_PASSWORD: str = "NewPassword"
    TOKEN: str = "Token"
    MAC_ADDRESS: str = "MACAddress"


class ChangePasswordRequest(SimpleRequestModel):
    def __init__(self, login_name, new_password, token, mac_address, session_id, nonce, pretty_print):
        self.login_name = login_name
        self.new_password = new_password
        self.token = token
        self.mac_address = mac_address
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[ChangePasswordRequestParams.LOGIN_NAME] = self.login_name
        args[ChangePasswordRequestParams.NEW_PASSWORD] = self.new_password
        args[ChangePasswordRequestParams.TOKEN] = self.token
        args[ChangePasswordRequestParams.MAC_ADDRESS] = self.mac_address
        return args
