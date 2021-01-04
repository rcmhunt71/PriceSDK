from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class IsFannieMaeWebPostResultAvailableRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    KEEP_POLLING: str = "KeepPolling"
    WEB_POST_RESULT: str = "WebPostResult"
    WHICH_INTERFACE: str = "WhichInterface"


class IsFannieMaeWebPostResultAvailableRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, keep_polling, web_post_result, which_interface, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.keep_polling = keep_polling
        self.web_post_result = web_post_result
        self.which_interface = which_interface
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[IsFannieMaeWebPostResultAvailableRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[IsFannieMaeWebPostResultAvailableRequestParams.KEEP_POLLING] = self.keep_polling
        args[IsFannieMaeWebPostResultAvailableRequestParams.WEB_POST_RESULT] = self.web_post_result
        args[IsFannieMaeWebPostResultAvailableRequestParams.WHICH_INTERFACE] = self.which_interface
        return args
