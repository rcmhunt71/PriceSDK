from APIs.others.models.method_list import MethodListKeys, MethodLists
from base.common.response import CommonResponse


class MethodListResponse(CommonResponse):
    _ADD_KEYS = [MethodListKeys.METHOD_LIST]
    _SUB_MODELS = [MethodLists]
