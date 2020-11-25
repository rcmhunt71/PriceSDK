from dataclasses import dataclass

from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class RequestResetPasswordRequestParams(BaseRequestModelKeys):
    DELIVERY_METHOD: str = "DeliveryMethod"
    LOGIN_NAME: str = "LoginName"
    RESET_LINK: str = "ResetLink"
    MAC_ADDRESS: str = "MACAddress"


class RequestResetPasswordRequest(SimpleRequestModel):
    def __init__(self, delivery_method, login_name, reset_link, mac_address, session_id, nonce, pretty_print):
        self.delivery_method = delivery_method
        self.login_name = login_name
        self.reset_link = reset_link
        self.mac_address = mac_address
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[RequestResetPasswordRequestParams.DELIVERY_METHOD] = self.delivery_method
        args[RequestResetPasswordRequestParams.LOGIN_NAME] = self.login_name
        args[RequestResetPasswordRequestParams.RESET_LINK] = self.reset_link
        args[RequestResetPasswordRequestParams.MAC_ADDRESS] = self.mac_address
        return args
