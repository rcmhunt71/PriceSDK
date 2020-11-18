from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class GetEmployeeGroupAndMemberListRequestParams(BaseRequestModelKeys):
    EMPLOYEE_ID: str = "EmployeeID"


class GetEmployeeGroupAndMemberListRequest(SimpleRequestModel):
    def __init__(self, employee_id, session_id, nonce, pretty_print):
        self.employee_id = employee_id
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetEmployeeGroupAndMemberListRequestParams.EMPLOYEE_ID] = self.employee_id
        return args
