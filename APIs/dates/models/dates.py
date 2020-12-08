from dataclasses import dataclass, fields

from base.responses.base_response import BaseResponse


@dataclass
class DatesInfoKeys:
    DATE_NAME: str = "DateName"
    DATE_VALUE: str = "DateValue"


@dataclass
class DatesKeys:
    DATES_LIST: str = 'DatesList'


class Date(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(DatesInfoKeys)]


class Dates(BaseResponse):

    def __init__(self, arg_list):
        self.model_name = self.__class__.__name__
        self.raw = arg_list[::]

        self._ADD_KEYS = [date.get(DatesInfoKeys.DATE_NAME).replace(' ','_').lower() for date in arg_list]
        self._SUB_MODELS = [Date for _ in range(len(self._ADD_KEYS))]
        kwargs = dict(zip(self._ADD_KEYS, arg_list))
        super().__init__(**kwargs)