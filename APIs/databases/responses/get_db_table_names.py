from base.common.response import CommonResponse
from APIs.databases.models.get_db_table_names import GetDbTableNamesKeys


class GetDbTableNamesResponse(CommonResponse):
    _ADD_KEYS = [GetDbTableNamesKeys.TABLE_NAMES]
    _SUB_MODELS = [None]
