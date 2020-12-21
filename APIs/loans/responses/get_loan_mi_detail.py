from APIs.loans.models.mi_details import MIDetails, MIDetailsKeys
from base.common.response import CommonResponse


class GetLoanMIDetailsResponse(CommonResponse):
    _ADD_KEYS = [MIDetailsKeys.LOANMIDETAILS]
    _SUB_MODELS = [MIDetails]
