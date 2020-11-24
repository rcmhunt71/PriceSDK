from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class GetPersonByPersonIDsRequestParams(BaseRequestModelKeys):
    PERSON_IDS: str = "PersonIDs"


class GetPersonByPersonIDsRequest(SimpleRequestModel):
    def __init__(self, person_ids, session_id, nonce, pretty_print):
        self.person_ids = person_ids
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetPersonByPersonIDsRequestParams.PERSON_IDS] = self.person_ids
        return args
