from base.common.response import CommonResponse
from APIs.task_items.models.get_task_item_group_list import GetTaskItemGroupListKeys, GetTaskItemGroupList


class GetTaskItemGroupListResponse(CommonResponse):
    _ADD_KEYS = [GetTaskItemGroupListKeys.TASK_ITEM_GROUP_LIST]
    _SUB_MODELS = [GetTaskItemGroupList]
