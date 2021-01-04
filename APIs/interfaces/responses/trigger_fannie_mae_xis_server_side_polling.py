from dataclasses import dataclass
from base.common.response import CommonResponse


@dataclass
class TriggerFannieMaeXISServerSidePollingKeys:
    FANNIE_MAE_ERROR_MESSAGE: str = "FannieMaeErrorMessage"


class TriggerFannieMaeXISServerSidePollingResponse(CommonResponse):
    _ADD_KEYS = [TriggerFannieMaeXISServerSidePollingKeys.FANNIE_MAE_ERROR_MESSAGE]
    _SUB_MODELS = [None]
