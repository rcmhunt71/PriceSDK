from base.common.response import CommonResponse
from APIs.dashboards.models.get_all_dashboards import GetAllDashboardsKeys, GetAllDashboardsList


class GetAllDashboardsResponse(CommonResponse):
    _ADD_KEYS = [GetAllDashboardsKeys.DASHBOARDS]
    _SUB_MODELS = [GetAllDashboardsList]
