from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class GetContactsRequestParams(BaseRequestModelKeys):
    CONTACT_ID_LIST: str = "ContactIDList"


class GetContactsRequest(SimpleRequestModel):
    def __init__(self, contact_id_list, session_id, nonce, pretty_print):
        self.contact_id_list = contact_id_list
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetContactsRequestParams.CONTACT_ID_LIST] = self.contact_id_list
        return args
