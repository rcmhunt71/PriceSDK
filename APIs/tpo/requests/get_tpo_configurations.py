from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class GetTPOConfigurationsRequestParams(BaseRequestModelKeys):
    COMPANY_ID: str = "CompanyID"


class GetTPOConfigurationsRequest(SimpleRequestModel):
    def __init__(self, company_id, session_id, nonce, pretty_print):
        self.company_id = company_id
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetTPOConfigurationsRequestParams.COMPANY_ID] = self.company_id
        return args
