from APIs.data_upload.models.data_upload import ProcessStringKeys
from base.common.response import CommonResponse


class ProcessStringResponse(CommonResponse):
    _ADD_KEYS = [ProcessStringKeys.DL_RESULT, ProcessStringKeys.LOAN_NUMBER_ID, ProcessStringKeys.DATA_LANGUAGE]
    _SUB_MODELS = [None, None, None]
