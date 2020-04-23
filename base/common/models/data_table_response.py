from dataclasses import dataclass


@dataclass
class DataColEntryKeys:
    ID: str = "id"
    LABEL: str = "label"
    TYPE: str = "type"


@dataclass
class RowValueKeys:
    VALUE: str = "v"


@dataclass
class RowColKeys:
    COL: str = "c"


@dataclass
class DataTableKeys:
    DATA_TABLE: str = "Data"
    COLS: str = "cols"
    ROWS: str = "rows"