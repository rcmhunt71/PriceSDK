from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class GetEmployeeIDRequestParams(BaseRequestModelKeys):
    EMPLOYEE_NUMBER: str = "EmployeeNumber"


class GetEmployeeIDRequest(SimpleRequestModel):
    def __init__(self, employee_number, session_id, nonce, pretty_print):
        self.employee_number = employee_number
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetEmployeeIDRequestParams.EMPLOYEE_NUMBER] = self.employee_number
        return args
