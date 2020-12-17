from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class DocutechPushbackResponseRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER: str = "LoanNumber"
    TOKEN_KEY: str = "TokenKey"
    HASH: str = "Hash"


class DocutechPushbackResponseRequest(SimpleRequestModel):
    def __init__(self, loan_number, token_key, hash, session_id, nonce, pretty_print):
        self.loan_number = loan_number
        self.token_key = token_key
        self.hash = hash
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[DocutechPushbackResponseRequestParams.LOAN_NUMBER] = self.loan_number
        args[DocutechPushbackResponseRequestParams.TOKEN_KEY] = self.token_key
        args[DocutechPushbackResponseRequestParams.HASH] = self.hash
        return args
