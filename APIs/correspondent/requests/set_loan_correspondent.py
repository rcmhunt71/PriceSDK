from typing import List, Dict, Any, Union
from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, KwargsRequestModel, DataKeys


@dataclass
class SetLoanCorrespondentRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"


@dataclass
class SetLoanCorrespondentFieldNames:
    CORRESPONDENT_DELEGATED: str = "CorrespondentDelegated"
    CORRESPONDENT_SERVICING: str = "CorrespondentServicing"
    CORRESPONDENT_SERVICING_TRANSFER: str = "CorrespondentServicingTransfer"


class SetLoanCorrespondentRequest(KwargsRequestModel):
    data_payload = SetLoanCorrespondentFieldNames
    REQUEST_PAYLOAD_KEY: str = "Correspondent"

    def __init__(self, loan_number_id, payload_dict, session_id, nonce, pretty_print, **kwargs):
        self.loan_number_id = loan_number_id
        super().__init__(session_id=session_id, nonce=nonce, payload=payload_dict, pretty_print=pretty_print, **kwargs)

    def to_params(self) -> Dict[str, Any]:
        args = super().to_params()
        args[SetLoanCorrespondentRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        return args


if __name__ == "__main__":
    import pprint
    kwargs = {
            "CORRESPONDENT_DELEGATED": "0",
            "CORRESPONDENT_SERVICING": "0",
            "CORRESPONDENT_SERVICING_TRANSFER": "0"}

    obj = SetLoanCorrespondentRequest(loan_number_id=10000001, payload_dict=None, session_id=123456, nonce=123245687,
        pretty_print=False, **kwargs)
    print(f"KWARGS: {pprint.pformat(obj.payload)}")

