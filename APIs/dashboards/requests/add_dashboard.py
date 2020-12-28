from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class AddDashboardRequestParams(BaseRequestModelKeys):
    DASHBOARD_CODE: str = "DashboardCode"
    DASHBOARD_TITLE: str = "DashboardTitle"
    DASHBOARD_HTML: str = "DashboardHTML"
    IS_VENDOR_MAINTAINED: str = "IsVendorMaintained"


class AddDashboardRequest(SimpleRequestModel):
    def __init__(self, dashboard_code, dashboard_title, dashboard_html, is_vendor_maintained, session_id, nonce,
                 pretty_print):
        self.dashboard_code = dashboard_code
        self.dashboard_title = dashboard_title
        self.dashboard_html = dashboard_html
        self.is_vendor_maintained = is_vendor_maintained
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[AddDashboardRequestParams.DASHBOARD_CODE] = self.dashboard_code
        args[AddDashboardRequestParams.DASHBOARD_TITLE] = self.dashboard_title
        args[AddDashboardRequestParams.DASHBOARD_HTML] = self.dashboard_html
        args[AddDashboardRequestParams.IS_VENDOR_MAINTAINED] = self.is_vendor_maintained
        return args
