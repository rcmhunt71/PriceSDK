import pprint
import typing
from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, KwargsRequestModel


@dataclass
class SetLoanCorrespondentAdjustmentRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"


@dataclass
class SetLoanCorrespondentAdjustmentPayload:
    ADJUSTMENT_ID: str = "AdjustmentID"
    ENABLED: str = "Enabled"
    READ_ONLY: str = "ReadOnly"
    ADJUSTMENT_NAME: str = "AdjustmentName"
    AMOUNT: str = "Amount"
    LOAN_ADJUSTMENT_ID: str = "LoanAdjustmentID"


class SetLoanCorrespondentAdjustmentRequest(KwargsRequestModel):
    data_payload = SetLoanCorrespondentAdjustmentPayload
    REQUEST_PAYLOAD_KEY = "CorrespondentAdjustments"

    def __init__(self, loan_number_id, payload_dict, session_id, nonce, pretty_print, **kwargs):
        self.loan_number_id = loan_number_id
        super().__init__(session_id=session_id, nonce=nonce, payload=payload_dict, pretty_print=pretty_print, **kwargs)

    def to_params(self):
        args = super().to_params()
        args[SetLoanCorrespondentAdjustmentRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        return args

    def build_payload(self) -> typing.Dict[str, typing.List[typing.Dict[str, typing.Any]]]:
        payload_dict = {}

        for payload_key in self.attr_list:
            if getattr(self, payload_key.lower(), None) is not None:
                payload_dict.update(
                    {getattr(self.data_payload, payload_key.upper(), payload_key): getattr(self, payload_key.lower())})
        payload = {self.REQUEST_PAYLOAD_KEY: [payload_dict]}
        return payload


if __name__ == "__main__":
    load = {
            "Loan_Adjustment_id": 0,
            "AdjustmenT_ID": 0,
            "enabled": False,
            "read_Only": False,
            "adjustment_name": "1",
            "AMOUNT": 1.25
        }

    res = SetLoanCorrespondentAdjustmentRequest(loan_number_id=10, payload_dict=None, session_id=1, nonce=2,
                                                pretty_print=False, **load)
    pprint.pprint(res.payload)
