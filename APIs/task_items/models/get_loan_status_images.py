from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class GetLoanStatusImagesInfoKeys:
    STATUS_ID: str = "StatusID"
    IMAGE_ID: str = "ImageID"
    STATUS_ITEM_NAME: str = "StatusItemName"
    STATUS: str = "Status"
    RECEIVED: str = "Received"
    RECEIVED_TIME: str = "ReceivedTime"
    SEQUENCE: str = "Sequence"
    NOTES: str = "Notes"
    PAGE_COUNT: str = "PageCount"
    SHOW_IMAGES_ON_B2B_SITE: str = "ShowImagesOnB2BSite"
    SHOW_IMAGE_NOTES_ON_B2B_SITE: str = "ShowImageNotesOnB2BSite"


@dataclass
class GetLoanStatusImagesKeys:
    LOAN_STATUS_IMAGES: str = "LoanStatusImages"


class GetLoanStatusImages(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(GetLoanStatusImagesInfoKeys)]


class GetLoanStatusImagesList(BaseListResponse):
    _SUB_MODEL = GetLoanStatusImages
