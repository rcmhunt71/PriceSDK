from dataclasses import dataclass, fields

from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class DatesInfoKeys:
    DATE_NAME: str = "DateName"
    DATE_VALUE: str = "DateValue"


@dataclass
class DatesKeys:
    DATES_LIST: str = 'DatesList'


class Dates(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(DatesInfoKeys)]


class DatesList(BaseListResponse):
    _SUB_MODEL = Dates
