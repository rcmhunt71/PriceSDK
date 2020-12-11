from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class GetConversationLogAlertRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    JUST_CURRENT_PERSON: str = "JustCurrentPerson"


class GetConversationLogAlertRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, just_current_person, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.just_current_person = just_current_person
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetConversationLogAlertRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[GetConversationLogAlertRequestParams.JUST_CURRENT_PERSON] = self.just_current_person
        return args
