from APIs.persons.models.user_details import UserDetailsKeys, UserDetails
from base.common.response import CommonResponse


class GetUserDetailsResponse(CommonResponse):
    _ADD_KEYS = [UserDetailsKeys.USER_DETAILS]
    _SUB_MODELS = [UserDetails]
