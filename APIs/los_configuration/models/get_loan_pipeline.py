from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class GetLoanPipelineInfoKeys:
    LOAN_STATUS: str = "LoanStatus"
    NUMBER_OF_LOANS: str = "NumberOfLoans"
    VOLUME: str = "Volume"


@dataclass
class GetLoanPipelineKeys:
    DATA: str = "Data"


class GetLoanPipeline(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(GetLoanPipelineInfoKeys)]


class GetLoanPipelineList(BaseListResponse):
    _SUB_MODEL = GetLoanPipeline
