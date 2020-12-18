from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class GetImageThumbnailMultipleInfoKeys:
    STATUS_ID: str = "StatusID"
    IMAGE_ID: str = "ImageID"
    PAGE_NUMBER: str = "PageNumber"
    IMAGE_DATA: str = "ImageData"


@dataclass
class GetImageThumbnailMultipleKeys:
    THUMBNAILS: str = "Thumbnails"


class GetImageThumbnailMultiple(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(GetImageThumbnailMultipleInfoKeys)]


class GetImageThumbnailMultipleList(BaseListResponse):
    _SUB_MODEL = GetImageThumbnailMultiple
