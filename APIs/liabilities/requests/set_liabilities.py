from typing import List, Dict, Any, Union
from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, KwargsRequestModel, DataKeys


@dataclass
class SetLiabilitiesRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"


@dataclass
class SetLiabilitiesPayload:
    CUSTOMER_ID: str = "CustomerID"
    LIABILITY_ID: str = "LiabilityID"
    FIELDS: str = "Fields"


@dataclass
class SetLiabilitiesFieldNames:
    LIABILITY_TYPE: str = "Liability_Type"
    ACCOUNT_NUMBER: str = "Account_Number"
    BALANCE: str = "Balance"
    PAYMENTS: str = "Payment"
    TERM: str = "Term"
    TO_BE_PAID_OFF: str = "To_Be_Paid_Off"
    INSTITUTION_ID: str = "Institution_ID"


class SetLiabilitiesRequest(KwargsRequestModel):
    data_payload = SetLiabilitiesPayload
    REQUEST_PAYLOAD_KEY: str = "Liabilities"

    def __init__(self, loan_number_id, payload_dict, session_id, nonce, pretty_print, **kwargs):
        self.loan_number_id = loan_number_id
        super().__init__(session_id=session_id, nonce=nonce, payload=payload_dict, pretty_print=pretty_print, **kwargs)

    def to_params(self) -> Dict[str, Any]:
        args = super().to_params()
        args[SetLiabilitiesRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        return args

    def build_payload(self) -> Dict[str, List[Dict[Any, Union[List[Dict[str, Any]], Any]]]]:
        payload_dict = {}
        for payload_key in self.attr_list:
            if getattr(self, payload_key.lower(), None) is not None:
                if payload_key.title() == SetLiabilitiesPayload.FIELDS:
                    fields_list = []
                    for key, value in getattr(self, payload_key.lower()).items():
                        fields_list.append({DataKeys.FIELD_NAME: getattr(SetLiabilitiesFieldNames, key.upper(), key),
                            DataKeys.FIELD_VALUE: value})
                    payload_dict.update({SetLiabilitiesPayload.FIELDS: fields_list})
                    continue
                payload_dict.update({getattr(self.data_payload, payload_key.upper(), payload_key): getattr(self, payload_key.lower())})
        return {self.REQUEST_PAYLOAD_KEY: [payload_dict]}


if __name__ == "__main__":
    import pprint
    kwargs = {
        "LiabilityID": 12345,
        "CustomerID": 98765,
        "Fields": {
            SetLiabilitiesFieldNames.LIABILITY_TYPE: "Installment",
            SetLiabilitiesFieldNames.ACCOUNT_NUMBER: "56789",
            SetLiabilitiesFieldNames.BALANCE: "12500",
            SetLiabilitiesFieldNames.PAYMENTS: "123",
            SetLiabilitiesFieldNames.TERM: "12",
            SetLiabilitiesFieldNames.TO_BE_PAID_OFF: "Y",
            SetLiabilitiesFieldNames.INSTITUTION_ID: "7777777"
        }
    }
    print(f"KWARGS: {pprint.pformat(kwargs)}")
    obj = SetLiabilitiesRequest(loan_number_id=10000001, payload_dict=None, session_id=123456, nonce=123245687, pretty_print=False, **kwargs)
    print(f"\nPAYLOAD: {pprint.pformat(obj.payload)}")
    print("\nTesting SetLiabilitiesRequest - payload_dict")
    obj_args = SetLiabilitiesRequest(loan_number_id=986532147, vendor_name="test_vendor", payload_dict=obj.payload,
                                              pretty_print=False, session_id=123456, nonce=123245687)
    print(f"PAYLOAD: {pprint.pformat(obj_args.payload)}")