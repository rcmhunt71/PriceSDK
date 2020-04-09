from APIs.fees.models.loan_fees import LoanFees, LoanFeeKeys
from base.common.response import CommonResponse


class GetLoanFees(CommonResponse):
    ADD_KEYS = [LoanFeeKeys.LOAN_FEES]
    SUB_MODELS = [LoanFees]
