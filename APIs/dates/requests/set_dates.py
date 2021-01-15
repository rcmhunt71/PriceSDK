from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class SetDatesRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"


class SetDatesRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, payload_dict, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        super().__init__(session_id=session_id, nonce=nonce, payload=payload_dict, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[SetDatesRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        return args
