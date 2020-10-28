from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class AddConsentRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    CONSENT_REASON: str = "ConsentReason"
    CONSENT_MARKETING_TYPE: str = "ConsentMarketingType"
    CONSENT_OPT_TYPE: str = "ConsentOptType"
    CONSENT_SOURCE: str = "ConsentSource"
    BORROWER_ID: str = "BorrowerID"


class AddConsentRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, consent_reason, consent_marketing_type, consent_opt_type, consent_source,
            borrower_id, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.consent_reason = consent_reason
        self.consent_marketing_type = consent_marketing_type
        self.consent_opt_type = consent_opt_type
        self.consent_source = consent_source
        self.borrower_id = borrower_id
        super().__init__(session_id = session_id, nonce = nonce, pretty_print = pretty_print)

    def to_params(self):
        args = super().to_params()
        args[AddConsentRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[AddConsentRequestParams.CONSENT_REASON] = self.consent_reason
        args[AddConsentRequestParams.CONSENT_MARKETING_TYPE] = self.consent_marketing_type
        args[AddConsentRequestParams.CONSENT_OPT_TYPE] = self.consent_opt_type
        args[AddConsentRequestParams.CONSENT_SOURCE] = self.consent_source
        args[AddConsentRequestParams.BORROWER_ID] = self.borrower_id
        return args
