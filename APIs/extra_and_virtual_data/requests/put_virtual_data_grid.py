from dataclasses import dataclass
from typing import Dict, Any

from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class PutVirtualDataGridRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"


class PutVirtualDataGridRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, payload_dict, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        super().__init__(session_id=session_id, nonce=nonce, payload=payload_dict, pretty_print=pretty_print)

    def to_params(self) -> Dict[str, Any]:
        args = super().to_params()
        args[PutVirtualDataGridRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        return args
