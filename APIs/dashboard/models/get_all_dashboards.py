from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class GetAllDashboardsInfoKeys:
    DASHBOARD_ID: str = "DashboardID"
    DASHBOARD_CODE: str = "DashboardCode"
    DASHBOARD_TITLE: str = "DashboardTitle"
    DASHBOARD_HTML: str = "DashboardHTML"
    IS_VENDOR_MAINTAINED: str = "IsVendorMaintained"
    SECURITY_LEVELS: str = "SecurityLevels"


@dataclass
class GetAllDashboardsKeys:
    DASHBOARDS: str = "Dashboards"


class GetAllDashboards(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(GetAllDashboardsInfoKeys)]


class GetAllDashboardsList(BaseListResponse):
    _SUB_MODEL = GetAllDashboards
