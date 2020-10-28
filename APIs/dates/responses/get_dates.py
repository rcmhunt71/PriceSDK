from APIs.dates.models.dates import DatesList, DatesKeys
from base.common.response import CommonResponse


class GetDatesResponse(CommonResponse):
    _ADD_KEYS = [DatesKeys.DATES_LIST]
    _SUB_MODELS = [DatesList]
