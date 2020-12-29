from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class TriggerEventRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    EVENT_ID: str = "EventID"


class TriggerEventRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, event_id, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.event_id = event_id
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[TriggerEventRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[TriggerEventRequestParams.EVENT_ID] = self.event_id
        return args
