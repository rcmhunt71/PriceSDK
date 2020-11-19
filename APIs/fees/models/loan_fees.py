from dataclasses import dataclass, fields

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
    _ADD_KEYS = [field.default for field in fields(LoanFeeColumnEntryKeys)]


class LoanFeeColumnEntryList(BaseListResponse):
    _SUB_MODEL = LoanFeeColumnEntry


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
    _SUB_MODEL = LoanFeeRowEntry


class LoanFeeRowCol(BaseResponse):
    _ADD_KEYS = [LoanFeeRowColEntryKey.COL]
    _SUB_MODELS = [LoanFeeRowEntryList]


class LoanFeeRowColList(BaseListResponse):
    _SUB_MODEL = LoanFeeRowCol


# FULL MODEL
# ------------------------
@dataclass
class LoanFeeKeys:
    LOAN_FEES: str = "LoanFees"


@dataclass
class AddLoanFeeKeys:
    LOAN_FEE_ID: str = "LoanFeeID"


class LoanFees(BaseResponse):
    _ADD_KEYS = [LoanFeeColumnKeys.COLS, LoanFeeRowKeys.ROWS]
    _SUB_MODELS = [LoanFeeColumnEntryList, LoanFeeRowColList]
