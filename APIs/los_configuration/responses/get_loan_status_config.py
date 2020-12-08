from APIs.los_configuration.models.get_loan_status_config import GetLoanStatusConfigKeys, GetLoanStatusConfigList
from base.common.response import CommonResponse


class GetLoanStatusConfigResponse(CommonResponse):
    _ADD_KEYS = [GetLoanStatusConfigKeys.LOAN_STATUSES]
    _SUB_MODELS = [GetLoanStatusConfigList]
