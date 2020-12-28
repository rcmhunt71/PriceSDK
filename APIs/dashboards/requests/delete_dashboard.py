from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class DeleteDashboardRequestParams(BaseRequestModelKeys):
    DASHBOARD_CODE: str = "DashboardCode"


class DeleteDashboardRequest(SimpleRequestModel):
    def __init__(self, dashboard_code, session_id, nonce, pretty_print):
        self.dashboard_code = dashboard_code
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[DeleteDashboardRequestParams.DASHBOARD_CODE] = self.dashboard_code
        return args
