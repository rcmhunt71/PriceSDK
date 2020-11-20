from dataclasses import dataclass

from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class EvaluateDataCheckBundleRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    DATA_CHECK_BUNDLE_ID: str = "DataCheckBundleID"


class EvaluateDataCheckBundleRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, data_check_bundle_id, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.data_check_bundle_id = data_check_bundle_id
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[EvaluateDataCheckBundleRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[EvaluateDataCheckBundleRequestParams.DATA_CHECK_BUNDLE_ID] = self.data_check_bundle_id
        return args
