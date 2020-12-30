from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class UploadMercuryVMPFileRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    UPLOAD_TOKEN: str = "UploadToken"
    HASH: str = "Hash"


class UploadMercuryVMPFileRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, upload_token, hash, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.upload_token = upload_token
        self.hash = hash
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[UploadMercuryVMPFileRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[UploadMercuryVMPFileRequestParams.UPLOAD_TOKEN] = self.upload_token
        args[UploadMercuryVMPFileRequestParams.HASH] = self.hash
        return args
