from dataclasses import dataclass
from base.common.response import CommonResponse


@dataclass
class ExportToInterfaceKeys:
    EXPORT_RESULT: str = "ExportResult"


class ExportToInterfaceResponse(CommonResponse):
    _ADD_KEYS = [ExportToInterfaceKeys.EXPORT_RESULT]
    _SUB_MODELS = [None]
