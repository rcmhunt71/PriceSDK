from typing import List, Dict, Any, Union
from dataclasses import dataclass

from base.common.models.request import BaseRequestModelKeys, KwargsRequestModel, DataKeys


@dataclass
class SetAssetsRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"


@dataclass
class SetAssetsPayload:
    CUSTOMER_ID: str = "CustomerID"
    ASSET_ID: str = "AssetID"
    FIELDS: str = "Fields"


@dataclass
class SetAssetsFieldNames:
    FIX_DESCRIPTION: str = "Fix_Description"
    MARKET_VALUE: str = "Market_Value"


class SetAssetsRequest(KwargsRequestModel):
    data_payload = SetAssetsPayload
    REQUEST_PAYLOAD_KEY: str = "Assets"

    def __init__(self, loan_number_id, payload_dict, session_id, nonce, pretty_print, **kwargs):
        self.loan_number_id = loan_number_id
        super().__init__(session_id=session_id, nonce=nonce, payload=payload_dict, pretty_print=pretty_print, **kwargs)

    def to_params(self) -> Dict[str, Any]:
        args = super().to_params()
        args[SetAssetsRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        return args

    def build_payload(self) -> Dict[str, List[Dict[Any, Union[List[Dict[str, Any]], Any]]]]:
        payload_dict = {}

        # For all recorded dynamically created attributes, create a dual entry dictionary:
        # { FIELD_NAME: attr_name, FIELD_VALUE: attr_value }
        for payload_key in self.attr_list:
            if getattr(self, payload_key, None) is not None:

                if payload_key == SetAssetsPayload.FIELDS.lower():
                    fields_list = []
                    for key, value in getattr(self, payload_key).items():
                        fields_list.append(
                            {DataKeys.FIELD_NAME: key,
                             DataKeys.FIELD_VALUE: value})
                    payload_dict.update({payload_key: fields_list})
                    continue

                payload_dict.update({getattr(self.data_payload, payload_key.upper(), payload_key): getattr(self, payload_key)})

        return {self.REQUEST_PAYLOAD_KEY: [payload_dict]}


if __name__ == "__main__":
    import pprint
    kwargs = {
        "asset_id": 12345,
        "customer_id": 98765,
        "fields": {
            SetAssetsFieldNames.FIX_DESCRIPTION:"Honda Civic",
            SetAssetsFieldNames.MARKET_VALUE:1900000
        }
    }
    print(f"KWARGS: {pprint.pformat(kwargs)}")

    obj = SetAssetsRequest(loan_number_id=10000001, payload_dict=None, session_id=123456, nonce=123245687, pretty_print=False, **kwargs)
    print(f"\nPAYLOAD: {pprint.pformat(obj.payload)}")

    print("\nTesting SetLoanDataRequest - payload_dict")
    obj_args = SetAssetsRequest(loan_number_id=986532147, vendor_name="test_vendor", payload_dict=obj.payload,
                                              pretty_print=False, session_id=123456, nonce=123245687)
    print(f"PAYLOAD: {pprint.pformat(obj_args.payload)}")