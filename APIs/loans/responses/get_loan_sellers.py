from APIs.loans.models.loan_sellers import LoanSellersKeys, LoanSellers
from base.common.response import CommonResponse


class GetLoanSellersResponse(CommonResponse):
    _ADD_KEYS = [LoanSellersKeys.LOAN_SELLERS]
    _SUB_MODELS = [LoanSellers]
