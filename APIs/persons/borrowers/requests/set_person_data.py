from typing import List, Dict, Any, Union
from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, KwargsRequestModel, DataKeys


@dataclass
class SetPersonDataRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"


@dataclass
class SetPersonDataPayload:
    RECORD_ID: str = "RecordID"
    FIELDS: str = "Fields"


@dataclass
class SetPersonDataFieldNames:
    FIRST_NAME: str = "First_Name"
    MIDDLE_NAME: str = "Middle_Name"
    LAST_NAME: str = "Last_Name"
    GENERATION: str = "Generation"
    TITLE: str = "Title"
    PERSON_INITIALS: str = "Person_Initials"
    BIRTHDATE: str = "Birthdate"
    CELL: str = "Cell"
    VOICE: str = "Voice"
    WORK_NUMBER: str = "Work_Number"
    WORK_EXTENSION: str = "WorkExtension"
    FAX: str = "Fax"
    PAGER: str = "Pager"
    EMAIL_ADDRESS: str = "EMail_Address"
    EMAIL_NAME: str = "EmailName"
    SOCIAL_SECURITY_NUMBER: str = "Social_Security_Number"
    DOCUMENT_PASSWORD: str = "Document_Password"
    PRESENT_ADDRESS_ID: str = "Present_Address_ID"
    MEMBER_NUMBER: str = "MemberNumber"


class SetPersonDataRequest(KwargsRequestModel):
    data_payload = SetPersonDataPayload
    REQUEST_PAYLOAD_KEY: str = "Persons"

    def __init__(self, loan_number_id, payload_dict, session_id, nonce, pretty_print, **kwargs):
        self.loan_number_id = loan_number_id
        super().__init__(session_id=session_id, nonce=nonce, payload=payload_dict, pretty_print=pretty_print, **kwargs)

    def to_params(self) -> Dict[str, Any]:
        args = super().to_params()
        args[SetPersonDataRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        return args

    def build_payload(self) -> Dict[str, List[Dict[Any, Union[List[Dict[str, Any]], Any]]]]:
        payload_dict = {}
        for payload_key in self.attr_list:
            if getattr(self, payload_key.lower(), None) is not None:
                if payload_key.title() == SetPersonDataPayload.FIELDS:
                    fields_list = []
                    for key, value in getattr(self, payload_key.lower()).items():
                        fields_list.append(
                            {DataKeys.FIELD_NAME: getattr(SetPersonDataFieldNames, key.upper(), key),
                            DataKeys.FIELD_VALUE: value})
                    payload_dict.update({SetPersonDataPayload.FIELDS: fields_list})
                    continue
                payload_dict.update({getattr(self.data_payload, payload_key.upper(), payload_key): getattr(self, payload_key.lower())})
        return {self.REQUEST_PAYLOAD_KEY: [payload_dict]}


if __name__ == "__main__":
    import pprint
    kwargs = {
        "RecordID": 98765,
        "Fields": {
            SetPersonDataFieldNames.FIRST_NAME: "John",
            SetPersonDataFieldNames.MIDDLE_NAME: "Thomas",
            SetPersonDataFieldNames.LAST_NAME: "Test",
            SetPersonDataFieldNames.GENERATION: "Jr.",
            SetPersonDataFieldNames.TITLE: "Mr.",
            SetPersonDataFieldNames.PERSON_INITIALS: "Test",
            SetPersonDataFieldNames.BIRTHDATE: "01/01/1970",
            SetPersonDataFieldNames.CELL: "123-123-1234",
            SetPersonDataFieldNames.VOICE: "123-123-1234",
            SetPersonDataFieldNames.WORK_NUMBER: "123-123-1234",
            SetPersonDataFieldNames.WORK_EXTENSION: "4321",
        }
    }
    print(f"KWARGS: {pprint.pformat(kwargs)}")

    obj = SetPersonDataRequest(loan_number_id=10000001, payload_dict=None, session_id=123456, nonce=123245687, pretty_print=False, **kwargs)
    print(f"\nPAYLOAD: {pprint.pformat(obj.payload)}")

    print("\nTesting SetCustomerRequest - payload_dict")
    obj_args = SetPersonDataRequest(loan_number_id=986532147, vendor_name= "test_vendor", payload_dict=obj.payload,
                                              pretty_print=False, session_id=123456, nonce=123245687)
    print(f"PAYLOAD: {pprint.pformat(obj_args.payload)}")
