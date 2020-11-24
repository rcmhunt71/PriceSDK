from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class GetCompaniesByIDsParams(BaseRequestModelKeys):
    COMPANY_IDS: str = "CompanyIds"


class GetCompaniesByIDsRequest(SimpleRequestModel):
    def __init__(self, company_ids, session_id, nonce, pretty_print):
        self.company_ids = company_ids
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetCompaniesByIDsParams.COMPANY_IDS] = self.company_ids
        return args
