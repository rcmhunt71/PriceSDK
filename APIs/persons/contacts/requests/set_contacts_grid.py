from typing import List, Dict, Any, Union
from dataclasses import dataclass
from base.common.models.request import KwargsRequestModel, DataKeys, BaseRequestModelKeys


@dataclass
class SetContactsGridRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"


@dataclass
class SetContactsGridPayload:
    CONTACT_TYPE: str = "ContactType"
    DATA_TABLE: str = "DataTable"
    DATA_TABLE_ID: str = "DataTableID"
    FIELDS: str = "Fields"


@dataclass
class SetContactsGridFieldNames:
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


class SetContactsGridRequest(KwargsRequestModel):
    data_payload = SetContactsGridPayload
    REQUEST_PAYLOAD_KEY: str = "ContactsGrid"

    def __init__(self, loan_number_id, payload_dict, session_id, nonce, pretty_print, **kwargs):
        self.loan_number_id = loan_number_id
        super().__init__(session_id=session_id, nonce=nonce, payload=payload_dict, pretty_print=pretty_print, **kwargs)

    def to_params(self) -> Dict[str, Any]:
        args = super().to_params()
        args[SetContactsGridRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        return args

    def build_payload(self) -> Dict[str, List[Dict[Any, Union[List[Dict[str, Any]], Any]]]]:
        payload_dict = {}
        for payload_key in self.attr_list:
            if getattr(self, payload_key.lower(), None) is not None:
                if payload_key.title() == SetContactsGridPayload.FIELDS:
                    fields_list = []
                    for key, value in getattr(self, payload_key.lower()).items():
                        fields_list.append(
                            {DataKeys.FIELD_NAME: getattr(SetContactsGridFieldNames, key.upper(), key),
                            DataKeys.FIELD_VALUE: value})
                    payload_dict.update({SetContactsGridPayload.FIELDS: fields_list})
                    continue
                payload_dict.update({getattr(self.data_payload, payload_key.upper(), payload_key): getattr(self, payload_key.lower())})
        return {self.REQUEST_PAYLOAD_KEY: [payload_dict]}


if __name__ == "__main__":
    import pprint
    kwargs = {
        "ContactType": "Broker",
        "DataTable": "Company",
        "DataTableID": 12,
        "Fields": {
            SetContactsGridFieldNames.CONTACT_TYPE: "Broker",
            SetContactsGridFieldNames.COMPANY_ID: "111222333",
            SetContactsGridFieldNames.TITLE: "Broker Processor",
            SetContactsGridFieldNames.DESIGNATION: "RA",
            SetContactsGridFieldNames.LICENSE_NUMBER: "654321",
            SetContactsGridFieldNames.EXTENSION: "321",
            SetContactsGridFieldNames.VOICE: "1321231234",
            SetContactsGridFieldNames.FAX: "1231231234",
            SetContactsGridFieldNames.NOTIFICATION_EMAILS: "abc@test.com",
            SetContactsGridFieldNames.CONTACT_NO_LONGER_EMPLOYED: False,
            SetContactsGridFieldNames.CONTACT_LOCKOUT: False,
            SetContactsGridFieldNames.NMLS_ID: "123456"
        }
    }
    print(f"KWARGS: {pprint.pformat(kwargs)}")

    obj = SetContactsGridRequest(loan_number_id=333333, payload_dict=None, session_id=123456, nonce=123245687,
        pretty_print=False, **kwargs)
    print(f"\nPAYLOAD: {pprint.pformat(obj.payload)}")

    print("\nTesting SetContactsGridRequest - payload_dict")
    obj_args = SetContactsGridRequest(loan_number_id=333333, payload_dict=obj.payload, pretty_print=False,
        session_id=123456, nonce=123245687)
    print(f"PAYLOAD: {pprint.pformat(obj_args.payload)}")
