from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class SetDashboardPermissionsRequestParams(BaseRequestModelKeys):
    DASHBOARD_CODE: str = "DashboardCode"
    SECURITY_LEVELS: str = "SecurityLevels"


class SetDashboardPermissionsRequest(SimpleRequestModel):
    def __init__(self, dashboard_code, security_levels, session_id, nonce, pretty_print):
        self.dashboard_code = dashboard_code
        self.security_levels = security_levels
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[SetDashboardPermissionsRequestParams.DASHBOARD_CODE] = self.dashboard_code
        args[SetDashboardPermissionsRequestParams.SECURITY_LEVELS] = self.security_levels
        return args
