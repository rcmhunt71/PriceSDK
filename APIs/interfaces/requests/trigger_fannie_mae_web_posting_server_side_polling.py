from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class TriggerFannieMaeWebPostingServerSidePollingRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER: str = "LoanNumber"
    CASE_FILE_ID: str = "CaseFileID"
    INTERFACE_ID: str = "InterfaceID"


class TriggerFannieMaeWebPostingServerSidePollingRequest(SimpleRequestModel):
    def __init__(self, loan_number, case_file_id, interface_id, session_id, nonce, pretty_print):
        self.loan_number = loan_number
        self.case_file_id = case_file_id
        self.interface_id = interface_id
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[TriggerFannieMaeWebPostingServerSidePollingRequestParams.LOAN_NUMBER] = self.loan_number
        args[TriggerFannieMaeWebPostingServerSidePollingRequestParams.CASE_FILE_ID] = self.case_file_id
        args[TriggerFannieMaeWebPostingServerSidePollingRequestParams.INTERFACE_ID] = self.interface_id
        return args
