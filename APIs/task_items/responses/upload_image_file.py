from base.common.response import CommonResponse


class UploadImageFileKeys:
    PAGE_COUNT: str = "PageCount"


class UploadImageFileResponse(CommonResponse):
    _ADD_KEYS = [UploadImageFileKeys.PAGE_COUNT]
    _SUB_MODELS = [None]
