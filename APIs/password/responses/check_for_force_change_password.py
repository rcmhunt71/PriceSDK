from APIs.password.models.password import ForceChangePasswordKeys
from base.common.response import CommonResponse


class CheckForForceChangePassword(CommonResponse):
    ADD_KEYS = [ForceChangePasswordKeys.FORCE_CHANGE_PASSWORD]
    SUB_MODELS = [None]
