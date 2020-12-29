from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class SetImportInterfaceRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER: str = "LoanNumber"
    IMPORT_OPTION: str = "ImportOption"
    DO_PROCESS_LIABILITIES: str = "DoProcessLiabilities"
    IMPORT_A_SINGLE_CREDIT_REPORT: str = "ImportASingleCreditReport"


class SetImportInterfaceRequest(SimpleRequestModel):
    def __init__(self, loan_number, import_option, do_process_liabilities, import_a_single_credit_report,
                 session_id, nonce, pretty_print):
        self.loan_number = loan_number
        self.import_option = import_option
        self.do_process_liabilities = do_process_liabilities
        self.import_a_single_credit_report = import_a_single_credit_report
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[SetImportInterfaceRequestParams.LOAN_NUMBER] = self.loan_number
        args[SetImportInterfaceRequestParams.IMPORT_OPTION] = self.import_option
        args[SetImportInterfaceRequestParams.DO_PROCESS_LIABILITIES] = self.do_process_liabilities
        args[SetImportInterfaceRequestParams.IMPORT_A_SINGLE_CREDIT_REPORT] = self.import_a_single_credit_report
        return args
