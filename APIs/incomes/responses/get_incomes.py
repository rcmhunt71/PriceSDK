from APIs.incomes.models.income import Incomes, IncomesKeys
from base.common.response import CommonResponse


class GetIncomesResponse(CommonResponse):
    _ADD_KEYS = [IncomesKeys.INCOMES]
    _SUB_MODELS = [Incomes]


if __name__ == "__main__":
    import pprint

    sample_response = {
        "Incomes": [
            {"CustomerID": 11106387, "IncomeID": 1},
            {"CustomerID": 11106388, "IncomeID": 2},
        ],
        "Successful": True
    }

    obj = GetIncomesResponse(**sample_response)
    print(f"\n2nd CustomerID: {pprint.pformat(getattr(obj, IncomesKeys.INCOMES)[1].CustomerID)}")