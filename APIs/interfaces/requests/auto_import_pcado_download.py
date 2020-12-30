from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class AutoImportPcadoDownloadRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER: str = "LoanNumber"


class AutoImportPcadoDownloadRequest(SimpleRequestModel):
    def __init__(self, loan_number, session_id, nonce, pretty_print):
        self.loan_number = loan_number
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[AutoImportPcadoDownloadRequestParams.LOAN_NUMBER] = self.loan_number
        return args
