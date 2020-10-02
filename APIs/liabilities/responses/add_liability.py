from APIs.liabilities.models.liability import LiabilitiesInfoKeys
from base.common.response import CommonResponse

class AddLiabilityResponse(CommonResponse):
    _ADD_KEYS = [LiabilitiesInfoKeys.LIABILITY_ID]
    _SUB_MODELS = [None]


if __name__ == "__main__":
    import pprint

    sample_response = {
        "LiabilityID": 787878,
        "Successful": True,
    }

    obj = AddLiabilityResponse(**sample_response)
    print(f"\nLiabilityID: {pprint.pformat(getattr(obj, LiabilitiesInfoKeys.LIABILITY_ID))}")