from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class GetDbColumnInfoRequestParams(BaseRequestModelKeys):
    TABLE_NAME: str = "TableName"


class GetDbColumnInfoRequest(SimpleRequestModel):
    def __init__(self, table_name, session_id, nonce, pretty_print):
        self.table_name = table_name
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetDbColumnInfoRequestParams.TABLE_NAME] = self.table_name
        return args
