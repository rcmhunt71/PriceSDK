from dataclasses import dataclass
from base.common.response import CommonResponse

@dataclass
class ContactIDsInfoKeys:
    CONTACT_IDS: str = "ContactIds"


class GetContactIDsResponse(CommonResponse):
    _ADD_KEYS = [ContactIDsInfoKeys.CONTACT_IDS]
    _SUB_MODELS = [None]


if __name__ == "__main__":
    import pprint

    sample_response = {"ContactIds": [123456, 987654321, 1002585],
        "Successful": True}

    obj = GetContactIDsResponse(**sample_response)
    print(f"\nContactIds: {pprint.pformat(getattr(obj, ContactIDsInfoKeys.CONTACT_IDS))}")
