from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class GetConfigurationListRequestParams(BaseRequestModelKeys):
    LIST_NAME: str = "ListName"


class GetConfigurationListRequest(SimpleRequestModel):
    def __init__(self, list_name, session_id, nonce, pretty_print):
        self.list_name = list_name
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetConfigurationListRequestParams.LIST_NAME] = self.list_name
        return args
