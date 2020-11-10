from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class GetContactGroupMemberListRequestParams(BaseRequestModelKeys):
    CONTACT_ID: str = "ContactID"


class GetContactGroupMemberListRequest(SimpleRequestModel):
    def __init__(self, contact_id, session_id, nonce, pretty_print):
        self.contact_id = contact_id
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetContactGroupMemberListRequestParams.CONTACT_ID] = self.contact_id
        return args
