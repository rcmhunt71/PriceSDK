from APIs.liabilities.models.liability import LiabilitiesKeys, Liabilities

from base.common.response import CommonResponse


class GetLiabilitiesResponse(CommonResponse):
    _ADD_KEYS = [LiabilitiesKeys.LIABILITIES]
    _SUB_MODELS = [Liabilities]


if __name__ == "__main__":
    import pprint

    sample_response = {
        "Liabilities": [
            {"CustomerID": 11106387, "LiabilityID": 1},
            {"CustomerID": 11106388, "LiabilityID": 2},
        ],
        "Successful": True
    }

    obj = GetLiabilitiesResponse(**sample_response)
    print(f"\n2nd CustomerID: {pprint.pformat(getattr(obj, LiabilitiesKeys.LIABILITIES)[1].CustomerID)}")