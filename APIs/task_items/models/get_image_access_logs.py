from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class GetImageAccessLogsInfoKeys:
    PERSON_ID: str = "PersonID"
    STATUS_ID: str = "StatusID"
    IMAGE_ID: str = "ImageID"
    VIEWED_ON: str = "ViewedOn"
    DOWNLOADED_ON: str = "DownloadedOn"


@dataclass
class GetImageAccessLogsKeys:
    IMAGE_ACCESS_LOG: str = "ImageAccessLog"


class GetImageAccessLogs(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(GetImageAccessLogsInfoKeys)]


class GetImageAccessLogsList(BaseListResponse):
    _SUB_MODEL = GetImageAccessLogs
