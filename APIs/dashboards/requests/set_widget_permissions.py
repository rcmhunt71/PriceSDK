from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class SetWidgetPermissionsRequestParams(BaseRequestModelKeys):
    WIDGET_CODE: str = "WidgetCode"
    SECURITY_LEVELS: str = "SecurityLevels"


class SetWidgetPermissionsRequest(SimpleRequestModel):
    def __init__(self, widget_code, security_levels, session_id, nonce, pretty_print):
        self.widget_code = widget_code
        self.security_levels = security_levels
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[SetWidgetPermissionsRequestParams.WIDGET_CODE] = self.widget_code
        args[SetWidgetPermissionsRequestParams.SECURITY_LEVELS] = self.security_levels
        return args
