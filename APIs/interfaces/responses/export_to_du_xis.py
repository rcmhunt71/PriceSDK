from dataclasses import dataclass
from base.common.response import CommonResponse


@dataclass
class ExportToDuXisKeys:
    RESPONSE_DATA: str = "ResponseData"


class ExportToDuXisResponse(CommonResponse):
    _ADD_KEYS = [ExportToDuXisKeys.RESPONSE_DATA]
    _SUB_MODELS = [None]
