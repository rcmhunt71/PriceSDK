from APIs.interfaces.models.freddiemac_systosys import FreddieMacSysToSysKeys
from base.common.response import CommonResponse


class MergeFreddieMacSysToSysResponse(CommonResponse):
    _ADD_KEYS = [FreddieMacSysToSysKeys.MERGE_MESSAGE, FreddieMacSysToSysKeys.MERGED,
        FreddieMacSysToSysKeys.RESULT]
    _SUB_MODELS = [None, None, None]
