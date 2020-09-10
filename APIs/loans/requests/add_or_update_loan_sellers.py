import pprint
from typing import Dict, Union, Any, List
from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, KwargsRequestModel, DataKeys


@dataclass
class AddOrUpdateLoanSellersRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"


@dataclass
class AddOrUpdateLoanSellersPayload:
    RECORD_ID: str = "RecordID"
    FIELDS: str = "Fields"


@dataclass
class AddOrUpdateLoanSellersFieldNames:
    FIRST_NAME: str = "FirstName"
    LAST_NAME: str = "LastName"
    GENERATION: str = "Generation"
    TITLE: str = "Title"
    ADDRESS: str = "Address"
    SUITE: str = "Suite"
    CITY: str = "City"
    ZIP: str = "Zip"
    SAME_AS_SUBJECT_PROPERTY_ADDRESS: str = "SameAsSubjectPropertyAddress"
    PARTIAL_EXEMPTION: str = "PartialExemption"


class AddOrUpdateLoanSellersRequest(KwargsRequestModel):
    data_payload = AddOrUpdateLoanSellersPayload
    REQUEST_PAYLOAD_KEY = "LoanSellers"

    def __init__(self, loan_number_id, payload_dict, session_id, nonce, pretty_print, **kwargs):

        self.loan_number_id = loan_number_id
        super().__init__(session_id=session_id, nonce=nonce, payload=payload_dict, pretty_print=pretty_print, **kwargs)

    def to_params(self) -> Dict[str, Any]:
        args = super().to_params()
        args[AddOrUpdateLoanSellersRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        return args

    def build_payload(self) -> Dict[str, List[Dict[Any, Union[List[Dict[str, Any]], Any]]]]:
        payload_dict = {}

        for payload_key in self.attr_list:
            if getattr(self, payload_key.lower(), None) is not None:

                if payload_key.title() == AddOrUpdateLoanSellersPayload.FIELDS:
                    fields_list = []
                    for key, value in getattr(self, payload_key.lower()).items():
                        fields_list.append(
                            {DataKeys.FIELD_NAME: getattr(AddOrUpdateLoanSellersFieldNames, key.upper(), key),
                             DataKeys.FIELD_VALUE: value})
                    payload_dict.update({AddOrUpdateLoanSellersPayload.FIELDS: fields_list})
                    continue

                payload_dict.update(
                    {getattr(self.data_payload, payload_key.upper(), payload_key): getattr(self, payload_key.lower())})

        return {self.REQUEST_PAYLOAD_KEY: [payload_dict]}


if __name__ == "__main__":
    # Subject Property > Seller tab
    body = {
            "LoanSellers": [
                {
                    "RecordID": 1,  # Excluding this key will result creating a new Loan Seller record
                    "Fields": [
                        {"FieldName": "FirstName", "FieldValue": "1"},
                        {"FieldName": "LastName", "FieldValue": "2"},
                        {"FieldName": "Generation", "FieldValue": "3"},
                        {"FieldName": "Title", "FieldValue": "4"},
                        {"FieldName": "Address", "FieldValue": "5"},
                        {"FieldName": "Suite", "FieldValue": "6"},
                        {"FieldName": "City", "FieldValue": "7"},
                        {"FieldName": "Zip", "FieldValue": "8"},
                        {"FieldName": "SameAsSubjectPropertyAddress", "FieldValue": "9"},
                        {"FieldName": "PartialExemption", "FieldValue": "10"}
                    ]
                }
            ]
        }

    kwargs = {"record_id": "123", "fields": {"FirstName": "Bob"}}
    a = AddOrUpdateLoanSellersRequest(loan_number_id=1111, payload_dict=None, session_id=1, nonce=1,
                                      pretty_print=None, **kwargs)
    print(f"\nPAYLOAD: {pprint.pformat(a.payload)}")
