from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel


@dataclass
class DownloadImageFilesByStatusIdListRequestParams:
    LOAN_NUMBER_ID: str = "LoanNumberID"
    STATUS_ID_LIST: str = "StatusIDList"
    DOC_PASSWORD: str = "DocPassword"


class DownloadImageFilesByStatusIdListRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, status_id_list, doc_password, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.status_id_list = status_id_list
        self.doc_password = doc_password
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[DownloadImageFilesByStatusIdListRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[DownloadImageFilesByStatusIdListRequestParams.STATUS_ID_LIST] = self.status_id_list
        args[DownloadImageFilesByStatusIdListRequestParams.DOC_PASSWORD] = self.doc_password
        return args
