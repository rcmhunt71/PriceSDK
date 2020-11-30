from dataclasses import dataclass

from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class DeletePricingAdjustmentRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    SECTION_DATA: str = "SectionData"


class DeletePricingAdjustmentRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, section_data, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.section_data = section_data
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[DeletePricingAdjustmentRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[DeletePricingAdjustmentRequestParams.SECTION_DATA] = self.section_data
        return args
