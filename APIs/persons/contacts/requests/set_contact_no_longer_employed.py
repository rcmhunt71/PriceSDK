from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class SetContactNoLongerEmployedRequestParams(BaseRequestModelKeys):
    CONTACT_ID: str = "ContactID"
    NO_LONGER_EMPLOYED: str = "NoLongerEmployed"


class SetContactNoLongerEmployedRequest(SimpleRequestModel):
    def __init__(self, contact_id, no_longer_employed, session_id, nonce, pretty_print):
        self.contact_id = contact_id
        self.no_longer_employed = no_longer_employed
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[SetContactNoLongerEmployedRequestParams.CONTACT_ID] = self.contact_id
        args[SetContactNoLongerEmployedRequestParams.NO_LONGER_EMPLOYED] = self.no_longer_employed
        return args
