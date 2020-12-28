from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class CheckLoanPrivilegeMultipleRequestParams(BaseRequestModelKeys):
    FEE_NUMBERS: str = "FeeNumbers"
    FEE_ITEMS: str = "FeeItems"
    REQUESTED_RIGHTS: str = "RequestedRights"


class CheckLoanPrivilegeMultipleRequest(SimpleRequestModel):
    def __init__(self, fee_numbers, fee_items, requested_rights, session_id, nonce, pretty_print):
        self.fee_numbers = fee_numbers
        self.fee_items = fee_items
        self.requested_rights = requested_rights
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[CheckLoanPrivilegeMultipleRequestParams.FEE_NUMBERS] = self.fee_numbers
        args[CheckLoanPrivilegeMultipleRequestParams.FEE_ITEMS] = self.fee_items
        args[CheckLoanPrivilegeMultipleRequestParams.REQUESTED_RIGHTS] = self.requested_rights
        return args
