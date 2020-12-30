from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class GetInterfaceProblemsInfoKeys:
    DATA_CHECK_ID: str = "DataCheckID"
    NAME: str = "Name"
    DESCRIPTION: str = "Description"
    RESULT: str = "Result"


@dataclass
class GetInterfaceProblemsKeys:
    DATA_CHECKS: str = "DataChecks"


class GetInterfaceProblems(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(GetInterfaceProblemsInfoKeys)]


class GetInterfaceProblemsList(BaseListResponse):
    _SUB_MODEL = GetInterfaceProblems
