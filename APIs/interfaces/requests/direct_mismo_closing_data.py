from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class DirectMISMOClosingDataRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    WHICH_INTERFACE: str = "WhichInterface"
    BEHAVIOR: str = "Behavior"
    FLAGS: str = "Flags"


class DirectMISMOClosingDataRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, which_interface, behavior, flags, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.which_interface = which_interface
        self.behavior = behavior
        self.flags = flags
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[DirectMISMOClosingDataRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[DirectMISMOClosingDataRequestParams.WHICH_INTERFACE] = self.which_interface
        args[DirectMISMOClosingDataRequestParams.BEHAVIOR] = self.behavior
        args[DirectMISMOClosingDataRequestParams.FLAGS] = self.flags
        return args
