from dataclasses import dataclass

from base.responses.base_response import BaseResponse, BaseListResponse


# --------------------------------
# COLUMN DEFINITIONS
# --------------------------------

@dataclass
class LoanDetailColEntryKeys:
    ID: str = "id"
    TYPE: str = "type"


class LoanDetailColEntry(BaseResponse):
    _ADD_KEYS = [LoanDetailColEntryKeys.ID, LoanDetailColEntryKeys.TYPE]


class LoanDetailCols(BaseListResponse):
    SUB_MODEL = LoanDetailColEntry


# --------------------------------
# ROW DEFINITIONS
# --------------------------------


@dataclass
class LoanDetailRowValueKeys:
    VALUE: str = "v"


@dataclass
class LoanDetailRowColKeys:
    COL: str = "c"


class LoanDetailRowValueEntry(BaseResponse):
    _ADD_KEYS = [LoanDetailRowValueKeys.VALUE]
    _SUB_MODELS = [None]


class LoanDetailRowColsValue(BaseListResponse):
    SUB_MODEL = LoanDetailRowValueEntry


class LoanDetailRowEntry(BaseResponse):
    _ADD_KEYS = [LoanDetailRowColKeys.COL]
    _SUB_MODELS = [LoanDetailRowColsValue]


class LoanDetailRowList(BaseListResponse):
    SUB_MODEL = LoanDetailRowEntry

# --------------------------------
# TABLE DEFINITIONS
# --------------------------------


@dataclass
class LoanDetailDataTableKeys:
    DATA_TABLE: str = "Data"
    COLS: str = "cols"
    ROWS: str = "rows"


class LoanDetailDataTable(BaseResponse):
    _ADD_KEYS = [LoanDetailDataTableKeys.ROWS, LoanDetailDataTableKeys.COLS]
    _SUB_MODELS = [LoanDetailRowList, LoanDetailCols]

