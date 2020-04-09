from APIs.dates.models.dates import DatesList, DatesListKeys
from base.common.response import CommonResponse


class GetDates(CommonResponse):
    ADD_KEYS = [DatesListKeys.DATES_LIST]
    SUB_MODELS = [DatesList]
