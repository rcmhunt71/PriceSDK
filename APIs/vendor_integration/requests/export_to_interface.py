from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class ExportToInterfaceRequestParams(BaseRequestModelKeys):
    INTERFACE_TYPE: str = "InterfaceType"
    FLAGS: str = "Flags"
    BEHAVIOR: str = "Behavior"
    LOAN_NUMBER_ID: str = "LoanNumberID"

class ExportToInterfaceRequest(SimpleRequestModel):
    def __init__(self, interface_type, flags, behavior, loan_number_id, session_id, nonce, pretty_print):
        self.interface_type = interface_type
        self.flags = flags
        self.behavior = behavior
        self.loan_number_id = loan_number_id
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[ExportToInterfaceRequestParams.INTERFACE_TYPE] = self.interface_type
        args[ExportToInterfaceRequestParams.FLAGS] = self.flags
        args[ExportToInterfaceRequestParams.BEHAVIOR] = self.behavior
        args[ExportToInterfaceRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        return args
