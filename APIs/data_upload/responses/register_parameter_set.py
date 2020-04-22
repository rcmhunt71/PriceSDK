from APIs.data_upload.models.register_parameter_set import RegisterParameterSetKeys
from base.common.response import CommonResponse


class RegisterParameterSet(CommonResponse):
    _ADD_KEYS = [RegisterParameterSetKeys.PARAMETER_SET_KEY]
    _SUB_MODELS = [None]
