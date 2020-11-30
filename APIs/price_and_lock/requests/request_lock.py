from dataclasses import dataclass

from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class RequestLockRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    BASE_PRICE: str = "BasePrice"


class RequestLockRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, base_price, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.base_price = base_price
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[RequestLockRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[RequestLockRequestParams.BASE_PRICE] = self.base_price
        return args
