from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class GetTaskItemGroupListInfoKeys:
    GROUP_NAME: str = "GroupName"
    EXPLAIN: str = "Explain"


@dataclass
class GetTaskItemGroupListKeys:
    TASK_ITEM_GROUP_LIST: str = "TaskItemGroupList"


class GetTaskItemGroup(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(GetTaskItemGroupListInfoKeys)]


class GetTaskItemGroupList(BaseListResponse):
    _SUB_MODEL = GetTaskItemGroup
