from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class SetContactLockoutRequestParams(BaseRequestModelKeys):
    CONTACT_ID: str = "ContactID"
    LOCKED_OUT: str = "LockedOut"


class SetContactLockoutRequest(SimpleRequestModel):
    def __init__(self, contact_id, locked_out, session_id, nonce, pretty_print):
        self.contact_id = contact_id
        self.locked_out = locked_out
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[SetContactLockoutRequestParams.CONTACT_ID] = self.contact_id
        args[SetContactLockoutRequestParams.LOCKED_OUT] = self.locked_out
        return args
