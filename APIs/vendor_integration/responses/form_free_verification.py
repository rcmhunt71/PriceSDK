from dataclasses import dataclass
from base.common.response import CommonResponse


@dataclass
class FormFreeVerificationKeys:
    RESPONSE: str = "Response"


class FormFreeVerificationResponse(CommonResponse):
    _ADD_KEYS = [FormFreeVerificationKeys.RESPONSE]
    _SUB_MODELS = [None]
