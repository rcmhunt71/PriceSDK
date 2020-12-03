from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class ProcessStringParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    DATA_LANGUAGE: str = "DataLanguage"
    PARAMETER_SET_KEY: str = "ParameterSetKey"


class ProcessStringRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, data_language, parameter_set_key, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.data_language = data_language
        self.parameter_set_key = parameter_set_key
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[ProcessStringParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[ProcessStringParams.DATA_LANGUAGE] = self.data_language
        args[ProcessStringParams.PARAMETER_SET_KEY] = self.parameter_set_key
        return args
