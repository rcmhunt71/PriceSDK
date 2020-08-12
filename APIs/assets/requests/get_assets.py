from dataclasses import dataclass

from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class GetAssetsRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"


class GetAssetsRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetAssetsRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        return args