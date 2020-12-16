from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel


@dataclass
class GetPrintFormPdfRequestParams:
    LOAN_NUMBER_ID: str = "LoanNumberID"
    PRINT_FORM_COMMA_LIST: str = "PrintFormCommaList"
    DOCUMENT_PASSWORD: str = "DocumentPassword"
    PRINT_LN_NAME: str = "PrintLnName"


class GetPrintFormPdfRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, print_form_comma_list, document_password, print_ln_name, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.print_form_comma_list = print_form_comma_list
        self.document_password = document_password
        self.print_ln_name = print_ln_name
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetPrintFormPdfRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[GetPrintFormPdfRequestParams.PRINT_FORM_COMMA_LIST] = self.print_form_comma_list
        args[GetPrintFormPdfRequestParams.DOCUMENT_PASSWORD] = self.document_password
        args[GetPrintFormPdfRequestParams.PRINT_LN_NAME] = self.print_ln_name
        return args
