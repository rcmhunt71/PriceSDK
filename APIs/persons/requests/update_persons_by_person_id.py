from typing import List, Dict, Any, Union
from dataclasses import dataclass
from base.common.models.request import KwargsRequestModel, DataKeys


@dataclass
class UpdatePersonsByPersonIDPayload:
    RECORD_ID: str = "RecordID"
    FIELDS: str = "Fields"


@dataclass
class UpdatePersonsByPersonIDFieldNames:
    SPOUSE_ID: str = "SPOUSE_ID"
    PRESENT_ADDRESS_ID: str = "Present_Address_ID"
    LAST_NAME: str = "Last_Name"
    FIRST_NAME: str = "First_Name"
    MIDDLE_NAME: str = "Middle_Name"
    GENERATION: str = "Generation"
    SOCIAL_SECURITY_NUMBER: str = "Social_Security_Number"
    TITLE: str = "Title"
    VOICE: str = "Voice"
    WORK_NUMBER: str = "Work_Number"
    FAX: str = "Fax"
    PAGER: str = "Pager"
    CELL: str = "Cell"
    BIRTHDATE: str = "Birthdate"
    EMAIL_ADDRESS: str = "EMail_Address"
    PERSON_INITIALS: str = "Person_Initials"
    EMAIL_NAME: str = "EmailName"
    WORK_EXTENSION: str = "WorkExtension"
    FORCE_PASSWORD_CHANGE: str = "ForcePasswordChange"


class UpdatePersonsByPersonIDRequest(KwargsRequestModel):
    data_payload = UpdatePersonsByPersonIDPayload
    REQUEST_PAYLOAD_KEY: str = "Persons"

    def __init__(self, payload_dict, session_id, nonce, pretty_print, **kwargs):
        super().__init__(session_id=session_id, nonce=nonce, payload=payload_dict, pretty_print=pretty_print, **kwargs)

    def to_params(self) -> Dict[str, Any]:
        args = super().to_params()
        return args

    def build_payload(self) -> Dict[str, List[Dict[Any, Union[List[Dict[str, Any]], Any]]]]:
        payload_dict = {}
        for payload_key in self.attr_list:
            if getattr(self, payload_key.lower(), None) is not None:
                if payload_key.title() == UpdatePersonsByPersonIDPayload.FIELDS:
                    fields_list = []
                    for key, value in getattr(self, payload_key.lower()).items():
                        fields_list.append(
                            {DataKeys.FIELD_NAME: getattr(UpdatePersonsByPersonIDFieldNames, key.upper(), key),
                                DataKeys.FIELD_VALUE: value
                            })
                    payload_dict.update({UpdatePersonsByPersonIDPayload.FIELDS: fields_list})
                    continue
                payload_dict.update(
                    {getattr(self.data_payload, payload_key.upper(), payload_key): getattr(self, payload_key.lower())})
        return {self.REQUEST_PAYLOAD_KEY: [payload_dict]}


if __name__ == "__main__":
    import pprint

    kwargs = {"RecordID": 98765, "Fields": {
        UpdatePersonsByPersonIDFieldNames.SPOUSE_ID: 789456,
        UpdatePersonsByPersonIDFieldNames.LAST_NAME: "Tester",
        UpdatePersonsByPersonIDFieldNames.TITLE: "Dr",
        UpdatePersonsByPersonIDFieldNames.FIRST_NAME: "Test",
        UpdatePersonsByPersonIDFieldNames.SOCIAL_SECURITY_NUMBER: "132-45-4569"
    }}

    print(f"KWARGS: {pprint.pformat(kwargs)}")

    obj = UpdatePersonsByPersonIDRequest(payload_dict=None, session_id=123456, nonce=123245687, pretty_print=False,
        **kwargs)
    print(f"\nPAYLOAD: {pprint.pformat(obj.payload)}")

    print("\nTesting UpdatePersonsByPersonIDRequest - payload_dict")
    obj_args = UpdatePersonsByPersonIDRequest(payload_dict=obj.payload, pretty_print=False, session_id=123456,
        nonce=123245687)
    print(f"PAYLOAD: {pprint.pformat(obj_args.payload)}")
