from APIs.password.models.password import ForceChangePasswordKeys
from base.common.response import CommonResponse


class CheckForForceChangePassword(CommonResponse):
    _ADD_KEYS = [ForceChangePasswordKeys.FORCE_CHANGE_PASSWORD]
    _SUB_MODELS = [None]
