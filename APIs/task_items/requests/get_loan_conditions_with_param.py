from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel


@dataclass
class GetLoanConditionsWithParamRequestParams:
    LOAN_NUMBER_ID: str = "LoanNumberID"
    OTHER_PARAMS: str = "OtherParams"


class GetLoanConditionsWithParamRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, other_params, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.other_params = other_params
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetLoanConditionsWithParamRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[GetLoanConditionsWithParamRequestParams.OTHER_PARAMS] = self.other_params
        return args
