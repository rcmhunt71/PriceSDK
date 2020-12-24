from base.common.response import CommonResponse
from APIs.dashboard.models.get_all_widgets import GetAllWidgetsKeys, GetAllWidgetsList


class GetAllWidgetsResponse(CommonResponse):
    _ADD_KEYS = [GetAllWidgetsKeys.WIDGETS]
    _SUB_MODELS = [GetAllWidgetsList]
