from dataclasses import dataclass
from base.common.response import CommonResponse


@dataclass
class SetImportInterfaceKeys:
    IMPORTED: str = "Imported"


class SetImportInterfaceResponse(CommonResponse):
    _ADD_KEYS = [SetImportInterfaceKeys.IMPORTED]
    _SUB_MODELS = [None]
