from base.common.response import CommonResponse
from APIs.security.models.get_loan_privilege import GetLoanPrivilegeKeys, GetLoanPrivilegeList


class GetLoanPrivilegeResponse(CommonResponse):
    _ADD_KEYS = [GetLoanPrivilegeKeys.DATA]
    _SUB_MODELS = [None]

# FIXME Modify response model when ticket MD-15194 is resolved
