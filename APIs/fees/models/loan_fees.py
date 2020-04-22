from dataclasses import dataclass

from base.responses.base_response import BaseResponse, BaseListResponse


# COLUMN MODELS
# ------------------------
@dataclass
class LoanFeeColumnEntryKeys:
    ID: str = "id"
    LABEL: str = "label"
    TYPE: str = "type"


@dataclass
class LoanFeeColumnKeys:
    COLS: str = "cols"


class LoanFeeColumnEntry(BaseResponse):
    _ADD_KEYS = [LoanFeeColumnEntryKeys.ID, LoanFeeColumnEntryKeys.LABEL, LoanFeeColumnEntryKeys.TYPE]


class LoanFeeColumnEntryList(BaseListResponse):
    SUB_MODEL = LoanFeeColumnEntry


# ROW MODELS
# ------------------------
@dataclass
class LoanFeeRowEntryKeys:
    VALUE: str = "v"


@dataclass
class LoanFeeRowColEntryKey:
    COL: str = "c"


@dataclass
class LoanFeeRowKeys:
    ROWS: str = "rows"


class LoanFeeRowEntry(BaseResponse):
    _ADD_KEYS = [LoanFeeRowEntryKeys.VALUE]


class LoanFeeRowEntryList(BaseListResponse):
    SUB_MODEL = LoanFeeRowEntry


class LoanFeeRowCol(BaseResponse):
    _ADD_KEYS = [LoanFeeRowColEntryKey.COL]
    _SUB_MODELS = [LoanFeeRowEntryList]


class LoanFeeRowColList(BaseListResponse):
    SUB_MODEL = LoanFeeRowCol


# FULL MODEL
# ------------------------
@dataclass
class LoanFeeKeys:
    LOAN_FEES: str = "LoanFees"


class LoanFees(BaseResponse):
    _ADD_KEYS = [LoanFeeColumnKeys.COLS, LoanFeeRowKeys.ROWS]
    _SUB_MODELS = [LoanFeeColumnEntryList, LoanFeeRowColList]
