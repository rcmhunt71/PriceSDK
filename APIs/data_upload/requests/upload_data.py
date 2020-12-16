from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class UploadDataParams(BaseRequestModelKeys):
    TOKEN: str = "Token"
    APPEND: str = "Append"
    TYPE: str = "Type"


class UploadDataRequest(SimpleRequestModel):
    def __init__(self, token, append, type, binary_file, session_id, nonce, pretty_print):
        self.token = token
        self.append = append
        self.type = type
        self.binary_file = binary_file
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[UploadDataParams.TOKEN] = self.token
        args[UploadDataParams.APPEND] = self.append
        args[UploadDataParams.TYPE] = self.type
        return args
