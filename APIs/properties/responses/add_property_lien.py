from base.common.response import CommonResponse

PROPERTY_LIEN_ID: str = 'PropertyLienID'

class AddPropertyLienResponse(CommonResponse):
    _ADD_KEYS = [PROPERTY_LIEN_ID]
    _SUB_MODELS = [None]


if __name__ == "__main__":
    import pprint

    sample_response = {
        "PropertyLienID": 1234567,
        "Successful": True,
    }

    obj = AddPropertyLienResponse(**sample_response)
    print(f"\nPropertyID: {pprint.pformat(getattr(obj, PROPERTY_LIEN_ID))}")
