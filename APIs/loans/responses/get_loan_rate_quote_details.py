from APIs.loans.models.rate_quote_details import RateQuoteDetailsInfoKeys, RateQuoteDetails
from base.common.response import CommonResponse


class GetLoanRateQuoteDetailsResponse(CommonResponse):
    _ADD_KEYS = [RateQuoteDetailsInfoKeys.LOAN_RATE_QUOTE_DETAILS]
    _SUB_MODELS = [RateQuoteDetails]
