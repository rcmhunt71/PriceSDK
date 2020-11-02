from base.common.response import CommonResponse
from APIs.fees.models.loan_fees import AddLoanFeeKeys


class AddLoanFeeResponse(CommonResponse):
    _ADD_KEYS = [AddLoanFeeKeys.LOAN_FEE_ID]
    _SUB_MODELS = [None]
