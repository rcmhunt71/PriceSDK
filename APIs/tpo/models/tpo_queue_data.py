from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class TPOQueueDataInfoKeys:
    QUEUE_STATUS: str = "QueueStatus"
    EDIT_DATE: str = "EditDate"
    ACTION_FLAG: str = "ActionFlag"
    FIELD_NAME: str = "FieldName"
    OLD_VALUE: str = "OldValue"
    NEW_VALUE: str = "NewValue"


@dataclass
class TPOQueueDataKeys:
    TPO_QUEUE_DATA: str = "TPOQueueData"


class TPOQueueData(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(TPOQueueDataInfoKeys)]


class TPOQueueDataList(BaseListResponse):
    _SUB_MODEL = TPOQueueData

