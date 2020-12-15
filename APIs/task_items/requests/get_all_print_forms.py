from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel


@dataclass
class GetAllPrintFormsRequestParams:
    NEWEST_FIRST: str = "NewestFirst"


class GetAllPrintFormsRequest(SimpleRequestModel):
    def __init__(self, newest_first, session_id, nonce, pretty_print):
        self.newest_first = newest_first
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetAllPrintFormsRequestParams.NEWEST_FIRST] = self.newest_first
        return args
