from typing import List, Dict, Any, Union
from dataclasses import dataclass

from base.common.models.request import BaseRequestModelKeys, KwargsRequestModel, DataKeys


@dataclass
class SetPropertyDataRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"


@dataclass
class SetPropertyDataPayload:
    PROPERTY_ID: str = "PropertyID"
    FIELDS: str = "Fields"


@dataclass
class SetPropertyDataFieldNames:
    PROPERTY_TYPE: str = 'PropertyType'
    ADDRESS: str = 'Address'
    CITY: str = 'City'
    STATE: str = 'State'
    ZIP: str = 'Zip'
    PURPOSE_OF_REFINANCE: str = 'Purpose_Of_Refinance'
    PROPERTY_CLASSIFICATION: str = 'Property_Classification'
    OCCUPANCY: str = 'Occupancy'
    OWN_RENT_YEARS: str = 'OwnRentYears'
    OWN_RENT: str = 'OwnRent'
    MARKET_VALUE: str = 'Market_Value'
    APPRAISED_VALUE: str = 'Appraised_Value'
    SALES_PRICE: str = 'Sales_Price'
    DATE_ACQUIRED: str = 'Date_Acquired'
    ORIGINAL_COST: str = 'Original_Cost'
    PROPERTY_TAX: str = 'Property_Tax'
    ASSOCIATION_DUES: str = 'Association_Dues'
    LEASE_RENT: str = 'Lease_Rent'
    LEASE_RENEGOTIATE_DATE: str = 'Lease_Renegotiate_Date'
    LEASE_EXPIRE_DATE: str = 'Lease_Expire_Date'
    TENURE: str = 'Tenure'
    YEAR_BUILT: str = 'Year_Built'
    NET_RENTAL_INCOME: str = 'Net_Rental_Income'
    HAZARD_INSURANCE: str = 'Hazard_Insurance'
    MORTGAGE_INSURANCE: str = 'Mortgage_Insurance'
    FLOOD_INSURANCE: str = 'Flood_Insurance'
    OTHER_COSTS: str = 'Other_Costs'
    CONTINUED_RENTAL: str = 'Continued_Rental'
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


class SetPropertyDataRequest(KwargsRequestModel):
    data_payload = SetPropertyDataPayload
    REQUEST_PAYLOAD_KEY: str = "Properties"

    def __init__(self, loan_number_id, payload_dict, session_id, nonce, pretty_print, **kwargs):
        self.loan_number_id = loan_number_id
        super().__init__(session_id=session_id, nonce=nonce, payload=payload_dict, pretty_print=pretty_print, **kwargs)

    def to_params(self) -> Dict[str, Any]:
        args = super().to_params()
        args[SetPropertyDataRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        return args

    def build_payload(self) -> Dict[str, List[Dict[Any, Union[List[Dict[str, Any]], Any]]]]:
        payload_dict = {}

        # For all fields create a dual entry dictionary:
        # { FIELD_NAME: attr_name, FIELD_VALUE: attr_value }
        for payload_key in self.attr_list:
            if getattr(self, payload_key.lower(), None) is not None:

                if payload_key.title() == SetPropertyDataPayload.FIELDS:
                    fields_list = []
                    for key, value in getattr(self, payload_key.lower()).items():
                        fields_list.append(
                            {DataKeys.FIELD_NAME: getattr(SetPropertyDataFieldNames, key.upper(), key),
                             DataKeys.FIELD_VALUE: value})
                    payload_dict.update({SetPropertyDataPayload.FIELDS: fields_list})
                    continue

                payload_dict.update({getattr(self.data_payload, payload_key.upper(), payload_key): getattr(self, payload_key.lower())})

        return {self.REQUEST_PAYLOAD_KEY: [payload_dict]}


if __name__ == "__main__":
    import pprint
    kwargs = {
        SetPropertyDataPayload.PROPERTY_ID: 54321,
        "fields": {
            "property_type":"San Jose",
            "OWN_RENT_YEARS":5,
            SetPropertyDataFieldNames.OWN_RENT: True
        }
    }
    print(f"KWARGS: {pprint.pformat(kwargs)}")

    obj = SetPropertyDataRequest(loan_number_id=10000001, payload_dict=None, session_id=123456, nonce=123245687, pretty_print=False, **kwargs)
    print(f"\nPAYLOAD: {pprint.pformat(obj.payload)}")

    print("\nTesting SetLoanDataRequest - payload_dict")
    obj_args = SetPropertyDataRequest(loan_number_id=986532147, vendor_name="test_vendor", payload_dict=obj.payload,
                                              pretty_print=False, session_id=123456, nonce=123245687)
    print(f"PAYLOAD: {pprint.pformat(obj_args.payload)}")