from APIs.liabilities.requests.set_liabilities import SetLiabilitiesPayload
from base.common.response import CommonResponse

class AddLiabilityResponse(CommonResponse):
    _ADD_KEYS = [SetLiabilitiesPayload.LIABILITY_ID]
    _SUB_MODELS = [None]


if __name__ == "__main__":
    import pprint

    sample_response = {
        "LiabilityID": 787878,
        "Successful": True,
    }

    obj = AddLiabilityResponse(**sample_response)
    print(f"\nLiabilityID: {pprint.pformat(getattr(obj, SetLiabilitiesPayload.LIABILITY_ID))}")