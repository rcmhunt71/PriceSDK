from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class GetTPOQueueDataRequestParams(BaseRequestModelKeys):
    COMPANY_ID: str = "CompanyID"
    CONTACT_ID: str = "ContactID"


class GetTPOQueueDataRequest(SimpleRequestModel):
    def __init__(self, company_id, contact_id, session_id, nonce, pretty_print):
        self.company_id = company_id
        self.contact_id = contact_id
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetTPOQueueDataRequestParams.COMPANY_ID] = self.company_id
        args[GetTPOQueueDataRequestParams.CONTACT_ID] = self.contact_id
        return args
