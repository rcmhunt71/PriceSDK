from dataclasses import dataclass
from enum import Enum
from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class GetUCDFieldsRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    INTERFACE_ID: str = "InterfaceID"


class InterfaceIDs(Enum):
    FREDDIE_MAC = 0
    FANNIE_MAE = 1


class GetUCDFieldsRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, interface_id, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.interface_id = interface_id
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetUCDFieldsRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[GetUCDFieldsRequestParams.INTERFACE_ID] = self.interface_id
        return args
