from APIs.fees.models.loan_fees import LoanFees, LoanFeeKeys
from base.common.response import CommonResponse


class GetLoanFees(CommonResponse):
    _ADD_KEYS = [LoanFeeKeys.LOAN_FEES]
    _SUB_MODELS = [LoanFees]
