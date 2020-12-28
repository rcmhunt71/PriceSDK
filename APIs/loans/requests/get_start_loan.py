from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class GetStartLoanRequestParams(BaseRequestModelKeys):
    OFFICER_ID: str = "OfficerID"


class GetStartLoanRequest(SimpleRequestModel):
    def __init__(self, officer_id, session_id, nonce, pretty_print):
        self.officer_id = officer_id
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetStartLoanRequestParams.OFFICER_ID] = self.officer_id
        return args
