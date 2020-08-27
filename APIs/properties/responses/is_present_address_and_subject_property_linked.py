from base.common.response import CommonResponse

ISLINKED: str = 'IsLinked'

class IsPresentAddressAndSubjectPropertyLinkedResponse(CommonResponse):
    _ADD_KEYS = [ISLINKED]
    _SUB_MODELS = [None]


if __name__ == "__main__":
    import pprint

    sample_response = {
        "IsLinked": True,
        "Successful": True,
    }

    obj = IsPresentAddressAndSubjectPropertyLinkedResponse(**sample_response)
    print(f"\nIsLinked: {pprint.pformat(getattr(obj, ISLINKED))}")
