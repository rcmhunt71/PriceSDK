from APIs.correspondent.models.loan_correspondent import LoanCorrespondentKeys, LoanCorrespondent
from base.common.response import CommonResponse


class GetLoanCorrespondentResponse(CommonResponse):
    _ADD_KEYS = [LoanCorrespondentKeys.LOAN_CORRESPONDENT]
    _SUB_MODELS = [LoanCorrespondent]
