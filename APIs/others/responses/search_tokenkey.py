from dataclasses import dataclass
from base.common.response import CommonResponse


@dataclass
class SearchTokenkeyKeys:
    PERSON_ID: str = "PersonId"


class SearchTokenkeyResponse(CommonResponse):
    _ADD_KEYS = [SearchTokenkeyKeys.PERSON_ID]
    _SUB_MODELS = [None]
