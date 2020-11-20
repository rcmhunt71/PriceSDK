from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class GetEmployeesRequestParams(BaseRequestModelKeys):
    EMPLOYEE_ID_LISTS: str = "EmployeeIdLists"


class GetEmployeesRequest(SimpleRequestModel):
    def __init__(self, employee_id_lists, session_id, nonce, pretty_print):
        self.employee_id_lists = employee_id_lists
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetEmployeesRequestParams.EMPLOYEE_ID_LISTS] = self.employee_id_lists
        return args
