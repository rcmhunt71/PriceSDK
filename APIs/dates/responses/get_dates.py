from APIs.dates.models.dates import DatesList, DatesListKeys
from base.common.response import CommonResponse


class GetDates(CommonResponse):
    _ADD_KEYS = [DatesListKeys.DATES_LIST]
    _SUB_MODELS = [DatesList]
