from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class CheckFeeSystemPrivilegeRequestParams(BaseRequestModelKeys):
    FEE_NUMBER: str = "FeeNumber"
    FEE_ITEM: str = "FeeItem"
    REQUESTED_RIGHT: str = "RequestedRight"


class CheckFeeSystemPrivilegeRequest(SimpleRequestModel):
    def __init__(self, fee_number, fee_item, requested_right, session_id, nonce, pretty_print):
        self.fee_number = fee_number
        self.fee_item = fee_item
        self.requested_right = requested_right
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[CheckFeeSystemPrivilegeRequestParams.FEE_NUMBER] = self.fee_number
        args[CheckFeeSystemPrivilegeRequestParams.FEE_ITEM] = self.fee_item
        args[CheckFeeSystemPrivilegeRequestParams.REQUESTED_RIGHT] = self.requested_right
        return args
