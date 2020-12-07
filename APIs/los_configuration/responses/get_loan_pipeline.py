from APIs.los_configuration.models.get_loan_pipeline import GetLoanPipelineKeys, GetLoanPipelineList
from base.common.response import CommonResponse


class GetLoanPipelineResponse(CommonResponse):
    _ADD_KEYS = [GetLoanPipelineKeys.DATA]
    _SUB_MODELS = [GetLoanPipelineList]
