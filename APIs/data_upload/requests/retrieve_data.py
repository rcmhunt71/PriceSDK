from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class RetrieveDataRequestParams(BaseRequestModelKeys):
    TOKEN: str = "Token"
    TYPE: str = "Type"
    HASH: str = "Hash"


class RetrieveDataRequest(SimpleRequestModel):
    def __init__(self, token, type, hash, session_id, nonce, pretty_print):
        self.token = token
        self.type = type
        self.hash = hash
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[RetrieveDataRequestParams.TOKEN] = self.token
        args[RetrieveDataRequestParams.TYPE] = self.type
        args[RetrieveDataRequestParams.HASH] = self.hash
        return args
