from dataclasses import dataclass

from base.responses.base_response import BaseResponse, BaseListResponse


# ============================
# -------- COLUMNS -----------
# ============================
@dataclass
class LoanListHeaderEntryKeys:
    ID: str = "id"
    LABEL: str = "label"
    TYPE: str = "type"


@dataclass
class LoanListHeaderColumnKeys:
    COLS: str = "cols"


class LoanListHeaderEntry(BaseResponse):
    _ADD_KEYS = [LoanListHeaderEntryKeys.ID, LoanListHeaderEntryKeys.LABEL, LoanListHeaderEntryKeys.TYPE]
    _SUB_MODELS = [None for _ in range(len(_ADD_KEYS))]


class LoanListHeaderList(BaseListResponse):
    SUB_MODEL = LoanListHeaderEntry


# ============================
# --------- ROWS -------------
# ============================
@dataclass
class LoanListRowValueEntryKeys:
    VALUE: str = "v"


@dataclass
class LoanListRowColValueEntryKeys:
    COL: str = "c"


@dataclass
class LoanListRowsKeys:
    ROWS: str = "rows"


class LoanListRowValueEntry(BaseResponse):
    _ADD_KEYS = [LoanListRowValueEntryKeys.VALUE]
    _SUB_MODELS = [None]


class LoanListRowValuesList(BaseListResponse):
    SUB_MODEL = LoanListRowValueEntry


class LoanListRowCol(BaseResponse):
    _ADD_KEYS = [LoanListRowColValueEntryKeys.COL]
    _SUB_MODELS = [LoanListRowValuesList]


class LoanListRowColList(BaseListResponse):
    SUB_MODEL = LoanListRowCol


# ============================
# -------- TABLE -------------
# ============================
@dataclass
class CustomerLoanListKeys:
    CUSTOMER_LOAN: str = "CustomerLoan"


class CustomerLoanList(BaseResponse):
    _ADD_KEYS = [LoanListHeaderColumnKeys.COLS, LoanListRowsKeys.ROWS]
    _SUB_MODELS = [LoanListHeaderList, LoanListRowColList]
