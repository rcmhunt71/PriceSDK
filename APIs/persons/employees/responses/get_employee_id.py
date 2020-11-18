from dataclasses import dataclass
from base.common.response import CommonResponse

@dataclass
class EmployeeIDInfoKeys:
    EMPLOYEE_ID: str = "EmployeeID"


class GetEmployeeIDResponse(CommonResponse):
    _ADD_KEYS = [EmployeeIDInfoKeys.EMPLOYEE_ID]
    _SUB_MODELS = [None]


