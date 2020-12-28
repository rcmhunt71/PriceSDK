from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class CheckSystemPrivilegeRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    SCREEN: str = "Screen"
    FIELD_NAME: str = "FieldName"
    REQUESTED_RIGHT: str = "RequestedRight"


class CheckSystemPrivilegeRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, screen, field_name, requested_right, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.screen = screen
        self.field_name = field_name
        self.requested_right = requested_right
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[CheckSystemPrivilegeRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[CheckSystemPrivilegeRequestParams.SCREEN] = self.screen
        args[CheckSystemPrivilegeRequestParams.FIELD_NAME] = self.field_name
        args[CheckSystemPrivilegeRequestParams.REQUESTED_RIGHT] = self.requested_right
        return args
