from typing import List, Dict, Any, Union
from dataclasses import dataclass

from base.common.models.request import BaseRequestModelKeys, KwargsRequestModel, DataKeys


@dataclass
class SetPropertyLiensRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"


@dataclass
class SetPropertyLiensPayload:
    PROPERTY_ID: str = "PropertyID"
    CUSTOMER_ID: str = "CustomerID"
    PROPERTY_LIEN_ID: str = "PropertyLienID"
    FIELDS: str = "Fields"


@dataclass
class SetPropertyLiensFieldNames:
    INSTITUTION_ID: str = 'Institution_ID'
    ACCOUNT_NUMBER: str = 'Account_Number'
    BALANCE: str = 'Balance'
    PAYMENT: str = 'Payment'
    TO_BE_PAID_OFF: str = 'To_Be_Paid_Off'
    TERM: str = 'Term'
    RENT: str = 'Rent'
    DISTRICT: str = 'District'
    NEIGHBORHOOD: str = 'Neighborhood'
    PUD_TYPE: str = 'PUD_Type'
    BUILDING_NAME: str = 'Building_Name'
    UNITS: str = 'Units'
    GROSS_RENTAL_INCOME: str = 'Gross_Rental_Income'
    TITLE_HELD_AS: str = 'Title_Held_As'
    LEGAL_DESCRIPTION: str = 'Legal_Description'
    PROPERTY_TAX_ID: str = 'Property_Tax_ID'


class SetPropertyLiensRequest(KwargsRequestModel):
    data_payload = SetPropertyLiensPayload
    REQUEST_PAYLOAD_KEY: str = "PropertyLiens"

    def __init__(self, loan_number_id, payload_dict, session_id, nonce, pretty_print, **kwargs):
        self.loan_number_id = loan_number_id
        super().__init__(session_id=session_id, nonce=nonce, payload=payload_dict, pretty_print=pretty_print, **kwargs)

    def to_params(self) -> Dict[str, Any]:
        args = super().to_params()
        args[SetPropertyLiensRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        return args

    def build_payload(self) -> Dict[str, List[Dict[Any, Union[List[Dict[str, Any]], Any]]]]:
        payload_dict = {}

        # For all fields create a dual entry dictionary:
        # { FIELD_NAME: attr_name, FIELD_VALUE: attr_value }
        for payload_key in self.attr_list:
            if getattr(self, payload_key.lower(), None) is not None:

                if payload_key.title() == SetPropertyLiensPayload.FIELDS:
                    fields_list = []
                    for key, value in getattr(self, payload_key.lower()).items():
                        fields_list.append(
                            {DataKeys.FIELD_NAME: getattr(SetPropertyLiensFieldNames, key.upper(), key),
                             DataKeys.FIELD_VALUE: value})
                    payload_dict.update({SetPropertyLiensPayload.FIELDS: fields_list})
                    continue

                payload_dict.update({getattr(self.data_payload, payload_key.upper(), payload_key): getattr(self, payload_key.lower())})

        return {self.REQUEST_PAYLOAD_KEY: [payload_dict]}


if __name__ == "__main__":
    import pprint
    kwargs = {
        SetPropertyLiensPayload.PROPERTY_ID: 54321,
        'PROPERTY_LIEN_ID': 123,
        'customer_id': 99999,
        "fields": {
            "TITLE_HELD_AS":"San Jose",
            "PUD_TYPE":5,
            SetPropertyLiensFieldNames.BUILDING_NAME: 'red'
        }
    }
    print(f"KWARGS: {pprint.pformat(kwargs)}")

    obj = SetPropertyLiensRequest(loan_number_id=10000001, payload_dict=None, session_id=123456, nonce=123245687, pretty_print=False, **kwargs)
    print(f"\nPAYLOAD: {pprint.pformat(obj.payload)}")

    print("\nTesting SetLoanLiensRequest - payload_dict")
    obj_args = SetPropertyLiensRequest(loan_number_id=986532147, vendor_name="test_vendor", payload_dict=obj.payload,
                                              pretty_print=False, session_id=123456, nonce=123245687)
    print(f"PAYLOAD: {pprint.pformat(obj_args.payload)}")