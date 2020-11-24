from dataclasses import dataclass

from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class SetLockoutRequestParams(BaseRequestModelKeys):
    EMPLOYEE_ID: str = "EmployeeID"
    LOCKOUT: str = "Lockout"


class SetLockoutRequest(SimpleRequestModel):
    def __init__(self, employee_id, lockout, session_id, nonce, pretty_print):
        self.employee_id = employee_id
        self.lockout = lockout
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[SetLockoutRequestParams.EMPLOYEE_ID] = self.employee_id
        args[SetLockoutRequestParams.LOCKOUT] = self.lockout
        return args
