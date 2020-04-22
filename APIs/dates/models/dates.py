from dataclasses import dataclass

from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class DateKeys:
    DATE_NAME: str = "DateName"
    DATE_VALUE: str = "DateValue"


class DateEntry(BaseResponse):
    _ADD_KEYS = [DateKeys.DATE_NAME, DateKeys.DATE_VALUE]
    _SUB_MODELS = [None, None]


@dataclass
class DatesListKeys:
    DATES_LIST: str = 'DatesList'


class DatesList(BaseListResponse):
    SUB_MODEL = DateEntry
