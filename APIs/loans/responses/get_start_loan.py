from base.common.response import CommonResponse
from APIs.loans.models.get_start_loan import GetStartLoanKeys


class GetStartLoanResponse(CommonResponse):
    _ADD_KEYS = [GetStartLoanKeys.START_LOAN_NUMBER, GetStartLoanKeys.FORM_1003]
    _SUB_MODELS = [None, None]
