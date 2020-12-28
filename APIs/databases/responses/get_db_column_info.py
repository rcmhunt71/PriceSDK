from base.common.response import CommonResponse
from APIs.databases.models.get_db_column_info import GetDbColumnInfoKeys, GetDbColumnInfoList


class GetDbColumnInfoResponse(CommonResponse):
    _ADD_KEYS = [GetDbColumnInfoKeys.TABLE_COLUMN_INFO]
    _SUB_MODELS = [GetDbColumnInfoList]
