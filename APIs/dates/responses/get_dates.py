from APIs.dates.models.dates import Dates, DatesKeys
from base.common.response import CommonResponse


class GetDatesResponse(CommonResponse):
    def __init__(self, **kwargs):
        key = DatesKeys.DATES_LIST
        model = Dates

        self._OBJS = [key]
        self._combine_args(objs=self._OBJS)

        if kwargs.get(key, []):
            kwargs[key] = model(kwargs.get(key, []))
        super().__init__(keys=None, objs=self._OBJS, **kwargs)
