from APIs.properties.models.properties import Properties, PropertiesKeys
from base.common.response import CommonResponse


class GetPropertiesResponse(CommonResponse):
    _ADD_KEYS = [PropertiesKeys.PROPERTIES]
    _SUB_MODELS = [Properties]


if __name__ == "__main__":
    import pprint

    sample_response = {
        "Properties":[
            { "CustomerID": 11106369, "PropertyID": 1},
            { "CustomerID": 11106370, "PropertyID": 2},
        ],
        "Successful": True
    }

    obj = GetPropertiesResponse(**sample_response)
    print(f"\n2nd CustomerID: {pprint.pformat(getattr(obj, PropertiesKeys.PROPERTIES)[1].CustomerID)}")