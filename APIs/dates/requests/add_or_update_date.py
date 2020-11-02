from dataclasses import dataclass

from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class AddOrUpdateDateRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    DATE_NAME: str = "DateName"
    DATE_VALUE: str = "DateValue"
    OTHER_PARAMS: str = "OtherParams"


class AddOrUpdateDateRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, date_name, date_value, other_params, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.date_name = date_name
        self.date_value = date_value
        self.other_params = other_params
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[AddOrUpdateDateRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[AddOrUpdateDateRequestParams.DATE_NAME] = self.date_name
        args[AddOrUpdateDateRequestParams.DATE_VALUE] = self.date_value
        args[AddOrUpdateDateRequestParams.OTHER_PARAMS] = self.other_params
        return args
