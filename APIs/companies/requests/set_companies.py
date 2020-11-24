from typing import List, Dict, Any, Union
from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, KwargsRequestModel, DataKeys


@dataclass
class SetCompaniesRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"


@dataclass
class SetCompaniesPayload:
    COMPANY_ID: str = "CompanyID"
    FIELDS: str = "Fields"


@dataclass
class SetCompaniesFieldNames:
    COMPANY_NAME: str = "Company_Name"
    VOICE: str = "Voice"
    ADDRESS: str = "Address"
    CITY: str = "City"
    STATE: str = "State"
    ZIP: str = "Zip"
    EMAIL_ADDRESS: str = "EmailAddress"
    NMLS_ID_EXPIRATION_DATE: str = "NMLSIDExpirationDate"
    COUNTRY: str = "Country"


class SetCompaniesRequest(KwargsRequestModel):
    data_payload = SetCompaniesPayload
    REQUEST_PAYLOAD_KEY: str = "Companies"

    def __init__(self, loan_number_id, payload_dict, session_id, nonce, pretty_print, **kwargs):
        self.loan_number_id = loan_number_id
        super().__init__(session_id=session_id, nonce=nonce, payload=payload_dict, pretty_print=pretty_print, **kwargs)

    def to_params(self) -> Dict[str, Any]:
        args = super().to_params()
        args[SetCompaniesRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        return args

    def build_payload(self) -> Dict[str, List[Dict[Any, Union[List[Dict[str, Any]], Any]]]]:
        payload_dict = {}
        for payload_key in self.attr_list:
            if getattr(self, payload_key.lower(), None) is not None:
                if payload_key.title() == SetCompaniesPayload.FIELDS:
                    fields_list = []
                    for key, value in getattr(self, payload_key.lower()).items():
                        fields_list.append({DataKeys.FIELD_NAME: getattr(SetCompaniesFieldNames, key.upper(), key),
                            DataKeys.FIELD_VALUE: value
                        })
                    payload_dict.update({SetCompaniesPayload.FIELDS: fields_list})
                    continue
                payload_dict.update(
                    {getattr(self.data_payload, payload_key.upper(), payload_key): getattr(self, payload_key.lower())})
        return {self.REQUEST_PAYLOAD_KEY: [payload_dict]}


if __name__ == "__main__":
    import pprint

    kwargs = {"CompanyID": 456789,
        "Fields": {
            SetCompaniesFieldNames.COMPANY_NAME: "TestAPI",
            SetCompaniesFieldNames.VOICE: "0987654321",
            SetCompaniesFieldNames.ADDRESS: "123 ABC st.",
            SetCompaniesFieldNames.EMAIL_ADDRESS: "test@test.com",
            SetCompaniesFieldNames.ZIP: "12"
        }
    }
    print(f"KWARGS: {pprint.pformat(kwargs)}")
    obj = SetCompaniesRequest(loan_number_id=10000001, payload_dict=None, session_id=123456, nonce=123245687,
        pretty_print=False, **kwargs)
    print(f"\nPAYLOAD: {pprint.pformat(obj.payload)}")
    print("\nTesting SetCompaniesRequest - payload_dict")
    obj_args = SetCompaniesRequest(loan_number_id=10000001, payload_dict=obj.payload, pretty_print=False,
        session_id=123456, nonce=123245687)
    print(f"PAYLOAD: {pprint.pformat(obj_args.payload)}")
