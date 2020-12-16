from APIs.interfaces.models.freddiemac_systosys import FreddieMacSysToSysKeys
from base.common.response import CommonResponse


class ResponseFreddieMacSysToSysResponse(CommonResponse):
    _ADD_KEYS = [FreddieMacSysToSysKeys.RESPONSE_STRING, FreddieMacSysToSysKeys.RESPONSE,
        FreddieMacSysToSysKeys.RESULT]
    _SUB_MODELS = [None, None, None]
