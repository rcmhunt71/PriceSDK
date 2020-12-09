from dataclasses import dataclass

from base.common.models.request import SimpleRequestModel


@dataclass
class DownloadImageFilesRequestParams:
    LOAN_NUMBER_ID: str = "LoanNumberID"
    STATUS_ID: str = "StatusID"


class DownloadImageFilesRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, status_id, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.status_id = status_id
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[DownloadImageFilesRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[DownloadImageFilesRequestParams.STATUS_ID] = self.status_id
        return args
