from base.common.response import CommonResponse

PROPERTY_ID: str = 'PropertyID'

class AddPropertyResponse(CommonResponse):
    _ADD_KEYS = [PROPERTY_ID]
    _SUB_MODELS = [None]


if __name__ == "__main__":
    import pprint

    sample_response = {
        "PropertyID": 77777,
        "Successful": True,
    }

    obj = AddPropertyResponse(**sample_response)
    print(f"\nPropertyID: {pprint.pformat(getattr(obj, PROPERTY_ID))}")
