from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel


@dataclass
class GetImageThumbnailRequestParams:
    LOAN_NUMBER_ID: str = "LoanNumberID"
    STATUS_ID: str = "StatusID"
    IMAGE_ID: str = "ImageID"
    PAGE_NUMBER: str = "PageNumber"
    HEIGHT: str = "Height"
    WIDTH: str = "Width"


class GetImageThumbnailRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, status_id, image_id, page_number, height, width, session_id, nonce,
                 pretty_print):
        self.loan_number_id = loan_number_id
        self.status_id = status_id
        self.image_id = image_id
        self.page_number = page_number
        self.height = height
        self.width = width
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetImageThumbnailRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[GetImageThumbnailRequestParams.STATUS_ID] = self.status_id
        args[GetImageThumbnailRequestParams.IMAGE_ID] = self.image_id
        args[GetImageThumbnailRequestParams.PAGE_NUMBER] = self.page_number
        args[GetImageThumbnailRequestParams.HEIGHT] = self.height
        args[GetImageThumbnailRequestParams.WIDTH] = self.width
        return args
