from APIs.interfaces.models.freddiemac_systosys import FreddieMacSysToSysKeys
from base.common.response import CommonResponse


class RequestFreddieMacSysToSysResponse(CommonResponse):
    _ADD_KEYS = [FreddieMacSysToSysKeys.REQUEST, FreddieMacSysToSysKeys.RESULT]
    _SUB_MODELS = [None, None]
