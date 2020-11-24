from APIs.passwords.models.password import PasswordAgeKeys
from base.common.response import CommonResponse


class GetEmployeePasswordAgeResponse(CommonResponse):
    _ADD_KEYS = [PasswordAgeKeys.EXPIRES, PasswordAgeKeys.DAYS_REMAINING, PasswordAgeKeys.EXPIRY_NOTICE_IN_DAYS]
    _SUB_MODELS = [None, None, None]
