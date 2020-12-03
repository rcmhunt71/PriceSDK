from APIs.data_upload.models.data_upload import RegisterParameterSetKeys
from base.common.response import CommonResponse


class RegisterParameterSetResponse(CommonResponse):
    _ADD_KEYS = [RegisterParameterSetKeys.PARAMETER_SET_KEY]
    _SUB_MODELS = [None]
