from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class GetDbColumnInfoKeys:
    TABLE_COLUMN_INFO: str = "TableColumnInfo"


@dataclass
class GetDbColumnInfoTableKeys:
    TABLE_NAME: str = "TableName"
    COLUMN_INFO: str = "ColumnInfo"


@dataclass
class GetDbColumnInfoColumnKeys:
    C: str = "C"
    D: str = "D"
    I: str = "I"
    M: str = "M"
    P: str = "P"
    S: str = "S"
    O: str = "O"


class GetDbColumnInfoColKeys(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(GetDbColumnInfoColumnKeys)]


class GetDbColumnInfoColKeysList(BaseListResponse):
    _SUB_MODEL = GetDbColumnInfoColKeys


class GetDbColumnInfo(BaseResponse):
    _ADD_KEYS = [GetDbColumnInfoTableKeys.TABLE_NAME, GetDbColumnInfoTableKeys.COLUMN_INFO]
    _SUB_MODELS = [None, GetDbColumnInfoColKeysList]


class GetDbColumnInfoList(BaseListResponse):
    _SUB_MODEL = GetDbColumnInfo
