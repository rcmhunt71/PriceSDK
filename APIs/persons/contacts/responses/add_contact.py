from dataclasses import dataclass
from base.common.response import CommonResponse

@dataclass
class ContactIDInfoKeys:
    CONTACT_ID: str = "ContactID"


class AddContactResponse(CommonResponse):
    _ADD_KEYS = [ContactIDInfoKeys.CONTACT_ID]
    _SUB_MODELS = [None]


if __name__ == "__main__":
    import pprint

    sample_response = {"ContactID": 123456, "Successful": True}

    obj = AddContactResponse(**sample_response)
    print(f"\nContactID: {pprint.pformat(getattr(obj, ContactIDInfoKeys.CONTACT_ID))}")
