from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class GetInterfaceProblemsRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    BORROWER_LIST: str = "BorrowerList"
    WHICH_INTERFACE: str = "WhichInterface"


class GetInterfaceProblemsRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, borrower_list, which_interface, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.borrower_list = borrower_list
        self.which_interface = which_interface
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetInterfaceProblemsRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[GetInterfaceProblemsRequestParams.BORROWER_LIST] = self.borrower_list
        args[GetInterfaceProblemsRequestParams.WHICH_INTERFACE] = self.which_interface
        return args
