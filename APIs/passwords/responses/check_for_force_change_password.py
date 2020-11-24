from APIs.passwords.models.password import ForceChangePasswordKeys
from base.common.response import CommonResponse


class CheckForForceChangePasswordResponse(CommonResponse):
    _ADD_KEYS = [ForceChangePasswordKeys.FORCE_CHANGE_PASSWORD]
    _SUB_MODELS = [None]
