from dataclasses import dataclass

from base.responses.base_response import BaseResponse, BaseListResponse


# --------------------------------
# COLUMN DEFINITIONS
# --------------------------------


@dataclass
class LoanDataColEntryKeys:
    ID: str = "id"
    LABEL: str = "label"
    TYPE: str = "type"


class AddLoanDataColEntry(BaseResponse):
    ADD_KEYS = [LoanDataColEntryKeys.ID, LoanDataColEntryKeys.LABEL,
                LoanDataColEntryKeys.TYPE]


class AddLoanDataCols(BaseListResponse):
    SUB_MODEL = AddLoanDataColEntry

# --------------------------------
# ROW DEFINITIONS
# --------------------------------


@dataclass
class LoanRowValueKeys:
    VALUE: str = "v"


@dataclass
class LoanRowColKeys:
    COL: str = "c"


class AddLoanValueEntry(BaseResponse):
    ADD_KEYS = [LoanRowValueKeys.VALUE]
    SUB_MODELS = [None]


class AddLoanRowColsValue(BaseListResponse):
    SUB_MODEL = AddLoanValueEntry


class AddLoanRowEntry(BaseResponse):
    ADD_KEYS = [LoanRowColKeys.COL]
    SUB_MODELS = [AddLoanRowColsValue]


class AddLoanRowList(BaseListResponse):
    SUB_MODEL = AddLoanRowEntry

# --------------------------------
# TABLE DEFINITIONS
# --------------------------------


@dataclass
class LoanDataTableKeys:
    DATA_TABLE: str = "Data"
    COLS: str = "cols"
    ROWS: str = "rows"


class LoanDataTable(BaseResponse):
    ADD_KEYS = [LoanDataTableKeys.ROWS, LoanDataTableKeys.COLS]
    SUB_MODELS = [AddLoanRowList, AddLoanDataCols]

