from APIs.data_upload.models.process_string import ProcessStringKeys
from base.common.response import CommonResponse


class ProcessString(CommonResponse):
    _ADD_KEYS = [ProcessStringKeys.DL_RESULT, ProcessStringKeys.LOAN_NUMBER_IDS, ProcessStringKeys.DATA_LANGUAGE]
    _SUB_MODELS = [None for _ in range(len(_ADD_KEYS))]
