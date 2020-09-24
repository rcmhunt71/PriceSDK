import os
from typing import Dict, Any, List
from dataclasses import dataclass, fields
from base.common.models.request import BaseRequestModelKeys, KwargsRequestModel, DataKeys
import pprint


@dataclass
class SetLoanMIGridDetailPayload:
    FIELDROW: str = "FieldRow"
    RATE: str = "Rate"
    YEARS: str = "Years"

@dataclass
class SetLoanMIGridDetailRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"


class SetLoanMIGridDetailRequest(KwargsRequestModel):
    data_payload = SetLoanMIGridDetailPayload
    REQUEST_PAYLOAD_KEY: str = "LoanMIGridFields"

    def __init__(self, loan_number_id, payload_dict, session_id, nonce, pretty_print, **kwargs):
        self.loan_number_id = loan_number_id
        super().__init__(session_id=session_id, nonce=nonce, payload=payload_dict, pretty_print=pretty_print, **kwargs)

    def to_params(self) -> Dict[str, Any]:
        args = super().to_params()
        args.update({
            SetLoanMIGridDetailRequestParams.LOAN_NUMBER_ID: self.loan_number_id,
        })
        return args

    def build_payload(self) -> Dict[str, List[Dict[str, Any]]]:
        valid_keys = [elem.name for elem in fields(self.data_payload)]
        field_row = getattr(self, SetLoanMIGridDetailPayload.FIELDROW.lower(), None)
        if not field_row:
            raise KeyError("FieldRow argument is required for this API method")
        payload_list = []
        for payload_key in self.attr_list:
            if payload_key.lower() == SetLoanMIGridDetailPayload.FIELDROW.lower():
                payload_list.append({SetLoanMIGridDetailPayload.FIELDROW: field_row})
                continue
            elif payload_key.upper() in valid_keys or os.environ.get('TEST_ENV'):
                payload_list.append({DataKeys.FIELD_NAME: getattr(SetLoanMIGridDetailPayload, payload_key.upper(), payload_key),
                            DataKeys.FIELD_VALUE: getattr(self, payload_key.lower())})
        payload_dict = {self.REQUEST_PAYLOAD_KEY: [{**payload_list[0], **payload_list[1]}]}
        return payload_dict

if __name__ == "__main__":
    body = {"LoanMIGridFields": [{"FieldRow": 1, ''"FieldName": "Rate", "FieldValue": "2.5"},
                                 {"FieldRow": 1, "FieldName": "Years", "FieldValue": "20"}]}

    kwargs = {"FieldRow": 1, "Rate": "3"}

    abc = SetLoanMIGridDetailRequest(loan_number_id = 12345, payload_dict = None, session_id = 777, nonce = 888,
        pretty_print = None, **kwargs)
    print(f"\nPAYLOAD: {pprint.pformat(abc.payload)}")
