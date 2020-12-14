from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class GetLastInterfaceFileRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    WHICH_INTERFACE: str = "WhichInterface"


class GetLastInterfaceFileRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, which_interface, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.which_interface = which_interface
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetLastInterfaceFileRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[GetLastInterfaceFileRequestParams.WHICH_INTERFACE] = self.which_interface
        return args
