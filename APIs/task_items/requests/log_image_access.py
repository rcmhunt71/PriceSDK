from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel


@dataclass
class LogImageAccessRequestParams:
    LOAN_NUMBER_ID: str = "LoanNumberID"
    IMAGE_ID: str = "ImageID"
    PERSON_ID: str = "PersonID"
    LOG_OPTION: str = "LogOption"
    STATUS_ID: str = "StatusID"


class LogImageAccessRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, image_id, person_id, log_option, status_id, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.image_id = image_id
        self.person_id = person_id
        self.log_option = log_option
        self.status_id = status_id
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[LogImageAccessRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[LogImageAccessRequestParams.IMAGE_ID] = self.image_id
        args[LogImageAccessRequestParams.PERSON_ID] = self.person_id
        args[LogImageAccessRequestParams.LOG_OPTION] = self.log_option
        args[LogImageAccessRequestParams.STATUS_ID] = self.status_id
        return args
