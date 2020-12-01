from base.common.response import CommonResponse
from APIs.price_and_lock.models.pull_qualified_loan_scenario_programs import \
                                                                        PullQualifiedLoanScenarioProgramsKeys, Programs


class PullQualifiedLoanScenarioProgramsResponse(CommonResponse):
    _ADD_KEYS = [PullQualifiedLoanScenarioProgramsKeys.QUALIFIED_LOAN_SCENARIO_PROGRAMS]
    _SUB_MODELS = [Programs]
