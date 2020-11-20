from typing import List, Dict, Any, Union
from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, KwargsRequestModel, DataKeys


@dataclass
class AddOrUpdateEmployeePayload:
    EMPLOYEE_ID: str = "EmployeeID"
    FIELDS: str = "Fields"


@dataclass
class AddOrUpdateEmployeeFieldNames:
    #TODO The lack of documentation in Confluence about what FieldNames can be accepted. Should be revised after documentation updates.
    FIRST_NAME: str = "First_Name"
    LAST_NAME: str = "Last_Name"
    EMPLOYEE_TYPE: str = "Employee_Type"
    EMAIL_ADDRESS: str = "Email_Address"
    TITLE: str = "Title"
    VOICE: str = "Voice"
    CELL: str = "Cell"
    NMLS_ID: str = "NMLSID"
    LENDER_OFFICE_ID: str = "Lender_Office_ID"


class AddOrUpdateEmployeeRequest(KwargsRequestModel):
    data_payload = AddOrUpdateEmployeePayload
    REQUEST_PAYLOAD_KEY: str = "Employee"

    def __init__(self, payload_dict, session_id, nonce, pretty_print, **kwargs):
        super().__init__(session_id=session_id, nonce=nonce, payload=payload_dict, pretty_print=pretty_print, **kwargs)

    def to_params(self) -> Dict[str, Any]:
        args = super().to_params()
        return args

    def build_payload(self) -> Dict[str, List[Dict[Any, Union[List[Dict[str, Any]], Any]]]]:
        payload_dict = {}
        for payload_key in self.attr_list:
            if getattr(self, payload_key.lower(), None) is not None:
                if payload_key.title() == AddOrUpdateEmployeePayload.FIELDS:
                    fields_list = []
                    for key, value in getattr(self, payload_key.lower()).items():
                        fields_list.append(
                            {DataKeys.FIELD_NAME: getattr(AddOrUpdateEmployeeFieldNames, key.upper(), key),
                            DataKeys.FIELD_VALUE: value})
                    payload_dict.update({AddOrUpdateEmployeePayload.FIELDS: fields_list})
                    continue
                payload_dict.update({getattr(self.data_payload, payload_key.upper(), payload_key): getattr(self, payload_key.lower())})
        return {self.REQUEST_PAYLOAD_KEY: [payload_dict]}


if __name__ == "__main__":
    import pprint
    kwargs = {
        "EmployeeID": 98765,
        "Fields": {
            AddOrUpdateEmployeeFieldNames.FIRST_NAME: "Test",
            AddOrUpdateEmployeeFieldNames.LAST_NAME: "Tester",
            AddOrUpdateEmployeeFieldNames.EMPLOYEE_TYPE: "Loan Officer",
            AddOrUpdateEmployeeFieldNames.EMAIL_ADDRESS: "test@test.com",
            AddOrUpdateEmployeeFieldNames.TITLE: "Processor",
            AddOrUpdateEmployeeFieldNames.VOICE: "7987654321",
            AddOrUpdateEmployeeFieldNames.CELL: "1234567890",
            AddOrUpdateEmployeeFieldNames.NMLS_ID: "987456",
            AddOrUpdateEmployeeFieldNames.LENDER_OFFICE_ID: "123"
        }
    }
    print(f"KWARGS: {pprint.pformat(kwargs)}")

    obj = AddOrUpdateEmployeeRequest(payload_dict=None, session_id=123456, nonce=123245687, pretty_print=False, **kwargs)
    print(f"\nPAYLOAD: {pprint.pformat(obj.payload)}")

    print("\nTesting AddOrUpdateEmployeeRequest - payload_dict")
    obj_args = AddOrUpdateEmployeeRequest(payload_dict=obj.payload, pretty_print=False, session_id=123456, nonce=123245687)
    print(f"PAYLOAD: {pprint.pformat(obj_args.payload)}")
