from base.common.models.data_table_response import DataColEntryKeys, RowValueKeys, RowColKeys, DataTableKeys
from base.responses.base_response import BaseResponse, BaseListResponse


# --------------------------------
# COLUMN DEFINITIONS
# --------------------------------


class LoanDataColEntry(BaseResponse):
    _ADD_KEYS = [DataColEntryKeys.ID, DataColEntryKeys.LABEL,
                 DataColEntryKeys.TYPE]


class LoanDataCols(BaseListResponse):
    _SUB_MODEL = LoanDataColEntry

# --------------------------------
# ROW DEFINITIONS
# --------------------------------


class LoanValueEntry(BaseResponse):
    _ADD_KEYS = [RowValueKeys.VALUE]
    _SUB_MODELS = [None]


class LoanRowColsValue(BaseListResponse):
    _SUB_MODEL = LoanValueEntry


class LoanRowEntry(BaseResponse):
    _ADD_KEYS = [RowColKeys.COL]
    _SUB_MODELS = [LoanRowColsValue]


class LoanRowList(BaseListResponse):
    _SUB_MODEL = LoanRowEntry