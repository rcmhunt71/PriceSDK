from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class SearchTokenkeyRequestParams(BaseRequestModelKeys):
    TOKEN_KEY: str = "TokenKey"


class SearchTokenkeyRequest(SimpleRequestModel):
    def __init__(self, token_key, session_id, nonce, pretty_print):
        self.token_key = token_key
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[SearchTokenkeyRequestParams.TOKEN_KEY] = self.token_key
        return args
