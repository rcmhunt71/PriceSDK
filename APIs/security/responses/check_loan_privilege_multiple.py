from APIs.security.models.check_loan_privilege_multiple import CheckLoanPrivilegeMultipleKeys, \
    CheckLoanPrivilegeMultipleList
from base.common.response import CommonResponse


class CheckLoanPrivilegeMultipleResponse(CommonResponse):
    _ADD_KEYS = [CheckLoanPrivilegeMultipleKeys.FEE_RIGHTS]
    _SUB_MODELS = [CheckLoanPrivilegeMultipleList]
