from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class GetAllWidgetsInfoKeys:
    WIDGET_ID: str = "WidgetID"
    WIDGET_CODE: str = "WidgetCode"
    WIDGET_TITLE: str = "WidgetTitle"
    WIDGET_HTML: str = "WidgetHTML"
    IS_PUBLIC: str = "IsPublic"
    CACHE_EXPIRATION: str = "CacheExpiration"
    CACHE_SCOPE: str = "CacheScope"
    IS_VENDOR_MAINTAINED: str = "IsVendorMaintained"
    SECURITY_LEVELS: str = "SecurityLevels"


@dataclass
class GetAllWidgetsKeys:
    WIDGETS: str = "Widgets"


class GetAllWidgets(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(GetAllWidgetsInfoKeys)]


class GetAllWidgetsList(BaseListResponse):
    _SUB_MODEL = GetAllWidgets
