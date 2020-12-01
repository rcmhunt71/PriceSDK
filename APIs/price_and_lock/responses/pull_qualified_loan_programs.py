from base.common.response import CommonResponse
from APIs.price_and_lock.models.pull_qualified_loan_programs import PullQualifiedLoanProgramsKeys, Programs


class PullQualifiedLoanProgramsResponse(CommonResponse):
    _ADD_KEYS = [PullQualifiedLoanProgramsKeys.QUALIFIED_LOAN_PROGRAMS]
    _SUB_MODELS = [Programs]
