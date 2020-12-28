from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class DeleteWidgetRequestParams(BaseRequestModelKeys):
    WIDGET_CODE: str = "WidgetCode"


class DeleteWidgetRequest(SimpleRequestModel):
    def __init__(self, widget_code, session_id, nonce, pretty_print):
        self.widget_code = widget_code
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[DeleteWidgetRequestParams.WIDGET_CODE] = self.widget_code
        return args
