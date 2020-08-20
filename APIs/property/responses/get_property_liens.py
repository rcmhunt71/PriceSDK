from APIs.property.models.property_liens import PropertyLiensKeys, PropertyLiens
from base.common.response import CommonResponse


class GetPropertyLiensResponse(CommonResponse):
    _ADD_KEYS = [PropertyLiensKeys.PROPERTYLIENS]
    _SUB_MODELS = [PropertyLiens]


if __name__ == "__main__":
    import pprint

    sample_response = {
        "PropertyLiens": [
            {"CustomerID": 11106369, "PropertyID": 1},
            {"CustomerID": 11106370, "PropertyID": 2, "SomeKey": "value"},
        ],
        "Successful": True
    }

    obj = GetPropertyLiensResponse(**sample_response)
    print(f"\n2nd CustomerID: {pprint.pformat(getattr(obj, PropertyLiensKeys.PROPERTYLIENS)[1].CustomerID)}")
