from APIs.loans.models.rate_quote_details import RateQuoteDetails, RateQuoteDetailsKeys
from base.common.response import CommonResponse


class GetLoanRateQuoteDetailsResponse(CommonResponse):
    _ADD_KEYS = [RateQuoteDetailsKeys.LOAN_RATE_QUOTE_DETAILS]
    _SUB_MODELS = [RateQuoteDetails]
