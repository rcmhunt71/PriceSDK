from APIs.data_upload.models.data_upload import UploadDataKeys
from base.common.response import CommonResponse


class UploadDataResponse(CommonResponse):
    _ADD_KEYS = [UploadDataKeys.TOKEN, UploadDataKeys.VALID_UNTIL]
    _SUB_MODELS = [None, None]
