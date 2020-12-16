from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel


@dataclass
class AddDisclosureHistoriesRequestParams:
    LOAN_NUMBER_ID: str = "LoanNumberID"
    EVENT: str = "Event"
    DOCUMENT_TYPE_BY_IDS: str = "DocumentTypeIDs"
    UPLOAD_TOKEN: str = "UploadToken"


class AddDisclosureHistoriesRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, event, document_type_ids, upload_token, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.event = event
        self.document_type_ids = document_type_ids
        self.upload_token = upload_token
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[AddDisclosureHistoriesRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[AddDisclosureHistoriesRequestParams.EVENT] = self.event
        args[AddDisclosureHistoriesRequestParams.DOCUMENT_TYPE_BY_IDS] = self.document_type_ids
        args[AddDisclosureHistoriesRequestParams.UPLOAD_TOKEN] = self.upload_token
        return args
