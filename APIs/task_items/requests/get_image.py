from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel


@dataclass
class GetImageRequestParams:
    LOAN_NUMBER_ID: str = "LoanNumberID"
    PAGE_NUMBER: str = "PageNumber"
    IMAGE_ID: str = "ImageID"
    STATUS_ID: str = "StatusID"


class GetImageRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, page_number, image_id, status_id, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.page_number = page_number
        self.image_id = image_id
        self.status_id = status_id
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetImageRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[GetImageRequestParams.PAGE_NUMBER] = self.page_number
        args[GetImageRequestParams.IMAGE_ID] = self.image_id
        args[GetImageRequestParams.STATUS_ID] = self.status_id
        return args
