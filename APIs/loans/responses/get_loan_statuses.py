from APIs.loans.models.loan_status import LoanStatusKeys, LoanStatuses
from base.common.response import CommonResponse


class GetLoanStatusesResponse(CommonResponse):
    _ADD_KEYS = [LoanStatusKeys.LOAN_STATUSES]
    _SUB_MODELS = [LoanStatuses]
