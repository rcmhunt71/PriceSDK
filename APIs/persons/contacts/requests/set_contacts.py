from typing import List, Dict, Any, Union
from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, KwargsRequestModel, DataKeys


@dataclass
class SetContactsRequestParams(BaseRequestModelKeys):
    pass


@dataclass
class SetContactsPayload:
    RECORD_ID: str = "RecordID"
    FIELDS: str = "Fields"


@dataclass
class SetContactsFieldNames:
    CONTACT_TYPE: str = "Contact_Type"
    COMPANY_ID: str = "Company_ID"
    TITLE: str = "Title"
    DESIGNATION: str = "Designation"
    LICENSE_NUMBER: str = "License_Number"
    EXTENSION: str = "Extension"
    VOICE: str = "Voice"
    FAX: str = "Fax"
    NOTIFICATION_EMAILS: str = "Notification_Emails"
    CONTACT_NO_LONGER_EMPLOYED: str = "Contact_No_Longer_Employed"
    CONTACT_LOCKOUT: str = "Contact_Lockout"
    NMLS_ID: str = "NMLSID"


class SetContactsRequest(KwargsRequestModel):
    data_payload = SetContactsPayload
    REQUEST_PAYLOAD_KEY: str = "Contacts"

    def __init__(self, payload_dict, session_id, nonce, pretty_print, **kwargs):
        super().__init__(session_id=session_id, nonce=nonce, payload=payload_dict, pretty_print=pretty_print, **kwargs)

    def to_params(self) -> Dict[str, Any]:
        args = super().to_params()
        return args

    def build_payload(self) -> Dict[str, List[Dict[Any, Union[List[Dict[str, Any]], Any]]]]:
        payload_dict = {}
        for payload_key in self.attr_list:
            if getattr(self, payload_key.lower(), None) is not None:
                if payload_key.title() == SetContactsPayload.FIELDS:
                    fields_list = []
                    for key, value in getattr(self, payload_key.lower()).items():
                        fields_list.append(
                            {DataKeys.FIELD_NAME: getattr(SetContactsFieldNames, key.upper(), key),
                            DataKeys.FIELD_VALUE: value})
                    payload_dict.update({SetContactsPayload.FIELDS: fields_list})
                    continue
                payload_dict.update({getattr(self.data_payload, payload_key.upper(), payload_key): getattr(self, payload_key.lower())})
        return {self.REQUEST_PAYLOAD_KEY: [payload_dict]}


if __name__ == "__main__":
    import pprint
    kwargs = {
        "RecordID": 98765,
        "Fields": {
            SetContactsFieldNames.CONTACT_TYPE: "Broker",
            SetContactsFieldNames.COMPANY_ID: "111222333",
            SetContactsFieldNames.TITLE: "Broker Processor",
            SetContactsFieldNames.DESIGNATION: "RA",
            SetContactsFieldNames.LICENSE_NUMBER: "654321",
            SetContactsFieldNames.EXTENSION: "321",
            SetContactsFieldNames.VOICE: "1321231234",
            SetContactsFieldNames.FAX: "1231231234",
            SetContactsFieldNames.NOTIFICATION_EMAILS: "abc@test.com",
            SetContactsFieldNames.CONTACT_NO_LONGER_EMPLOYED: False,
            SetContactsFieldNames.CONTACT_LOCKOUT: False,
            SetContactsFieldNames.NMLS_ID: "123456"
        }
    }
    print(f"KWARGS: {pprint.pformat(kwargs)}")

    obj = SetContactsRequest(payload_dict=None, session_id=123456, nonce=123245687, pretty_print=False, **kwargs)
    print(f"\nPAYLOAD: {pprint.pformat(obj.payload)}")

    print("\nTesting SetContactsRequest - payload_dict")
    obj_args = SetContactsRequest(payload_dict=obj.payload, pretty_print=False, session_id=123456, nonce=123245687)
    print(f"PAYLOAD: {pprint.pformat(obj_args.payload)}")
