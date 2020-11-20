from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class GetEmployeesWithParamRequestParams(BaseRequestModelKeys):
    LAST_NAME: str = "LastName"
    EMPLOYEE_TYPE: str = "EmployeeType"


class GetEmployeesWithParamRequest(SimpleRequestModel):
    def __init__(self, last_name, employee_type, session_id, nonce, pretty_print):
        self.last_name = last_name
        self.employee_type = employee_type
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetEmployeesWithParamRequestParams.LAST_NAME] = self.last_name
        args[GetEmployeesWithParamRequestParams.EMPLOYEE_TYPE] = self.employee_type
        return args
