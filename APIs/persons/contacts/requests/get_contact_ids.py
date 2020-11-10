from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class GetContactIDsRequestParams(BaseRequestModelKeys):
    COMPANY_STATUS: str = "CompanyStatus"
    CONTACT_TYPE: str = "ContactType"
    CONTACT_NAME: str = "ContactName"
    CONTACT_STATE: str = "ContactState"


class GetContactIDsRequest(SimpleRequestModel):
    def __init__(self, company_status, contact_type, contact_name, contact_state, session_id, nonce, pretty_print):
        self.company_status = company_status
        self.contact_type = contact_type
        self.contact_name = contact_name
        self.contact_state = contact_state
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetContactIDsRequestParams.COMPANY_STATUS] = self.company_status
        args[GetContactIDsRequestParams.CONTACT_TYPE] = self.contact_type
        args[GetContactIDsRequestParams.CONTACT_NAME] = self.contact_name
        args[GetContactIDsRequestParams.CONTACT_STATE] = self.contact_state
        return args
