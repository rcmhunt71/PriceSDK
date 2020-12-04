from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class MergeEmailTemplateRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    TO_EMAIL_LIST: str = "ToEmailList"
    CC_EMAIL_LIST: str = "CCEmailList"
    BCC_EMAIL_LIST: str = "BCCEmailList"
    EMAIL_TEMPLATE_ID: str = "EmailTemplateID"


class MergeEmailTemplateRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, to_email_list, cc_email_list, bcc_email_list, email_template_id, session_id,
            nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.to_email_list = to_email_list
        self.cc_email_list = cc_email_list
        self.bcc_email_list = bcc_email_list
        self.email_template_id = email_template_id
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[MergeEmailTemplateRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[MergeEmailTemplateRequestParams.TO_EMAIL_LIST] = self.to_email_list
        args[MergeEmailTemplateRequestParams.CC_EMAIL_LIST] = self.cc_email_list
        args[MergeEmailTemplateRequestParams.BCC_EMAIL_LIST] = self.bcc_email_list
        args[MergeEmailTemplateRequestParams.EMAIL_TEMPLATE_ID] = self.email_template_id
        return args
