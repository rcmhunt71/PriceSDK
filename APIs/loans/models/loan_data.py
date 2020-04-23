from base.common.models.data_table_response import DataColEntryKeys, RowValueKeys, RowColKeys, DataTableKeys
from base.responses.base_response import BaseResponse, BaseListResponse


# --------------------------------
# COLUMN DEFINITIONS
# --------------------------------


class AddLoanDataColEntry(BaseResponse):
    _ADD_KEYS = [DataColEntryKeys.ID, DataColEntryKeys.LABEL,
                 DataColEntryKeys.TYPE]


class AddLoanDataCols(BaseListResponse):
    _SUB_MODEL = AddLoanDataColEntry

# --------------------------------
# ROW DEFINITIONS
# --------------------------------


class AddLoanValueEntry(BaseResponse):
    _ADD_KEYS = [RowValueKeys.VALUE]
    _SUB_MODELS = [None]


class AddLoanRowColsValue(BaseListResponse):
    _SUB_MODEL = AddLoanValueEntry


class AddLoanRowEntry(BaseResponse):
    _ADD_KEYS = [RowColKeys.COL]
    _SUB_MODELS = [AddLoanRowColsValue]


class AddLoanRowList(BaseListResponse):
    _SUB_MODEL = AddLoanRowEntry

# --------------------------------
# TABLE DEFINITIONS
# --------------------------------


# TODO: REMOVE, no longer used
class LoanDataTable(BaseResponse):
    _ADD_KEYS = [DataTableKeys.ROWS, DataTableKeys.COLS]
    _SUB_MODELS = [AddLoanRowList, AddLoanDataCols]

