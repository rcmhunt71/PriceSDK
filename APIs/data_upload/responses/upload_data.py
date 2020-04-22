from APIs.data_upload.models.upload_data import UploadDataKeys
from base.common.response import CommonResponse


class UploadData(CommonResponse):
    _ADD_KEYS = [UploadDataKeys.TOKEN, UploadDataKeys.VALID_UNTIL]
    _SUB_MODELS = [None, None]
