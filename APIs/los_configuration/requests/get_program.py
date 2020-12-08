from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class GetProgramRequestParams(BaseRequestModelKeys):
    OTHER_PARAMS: str = "OtherParams"
    PROGRAM_CATEGORY: str = "ProgramCategory"
    FINANCE_METHOD: str = "FinanceMethod"
    PREPAY_PENALTY: str = "PrepayPenalty"
    LOAN_TERM_FROM: str = "LoanTermFrom"
    LOAN_TERM_TO: str = "LoanTermTo"
    INVESTOR_ID: str = "InvestorID"


class GetProgramRequest(SimpleRequestModel):
    def __init__(self, other_params, program_category, finance_method, prepay_penalty, loan_term_from, loan_term_to,
            investor_id, session_id, nonce, pretty_print):
        self.other_params = other_params
        self.program_category = program_category
        self.finance_method = finance_method
        self.prepay_penalty = prepay_penalty
        self.loan_term_from = loan_term_from
        self.loan_term_to = loan_term_to
        self.investor_id = investor_id

        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetProgramRequestParams.OTHER_PARAMS] = self.other_params
        args[GetProgramRequestParams.PROGRAM_CATEGORY] = self.program_category
        args[GetProgramRequestParams.FINANCE_METHOD] = self.finance_method
        args[GetProgramRequestParams.PREPAY_PENALTY] = self.prepay_penalty
        args[GetProgramRequestParams.LOAN_TERM_FROM] = self.loan_term_from
        args[GetProgramRequestParams.LOAN_TERM_TO] = self.loan_term_to
        args[GetProgramRequestParams.INVESTOR_ID] = self.investor_id
        return args
