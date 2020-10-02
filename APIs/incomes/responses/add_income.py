from APIs.incomes.models.income import IncomesInfoKeys
from base.common.response import CommonResponse

class AddIncomeResponse(CommonResponse):
    _ADD_KEYS = [IncomesInfoKeys.INCOME_ID]
    _SUB_MODELS = [None]


if __name__ == "__main__":
    import pprint

    sample_response = {
        "IncomeID": 787878,
        "Successful": True,
    }

    obj = AddIncomeResponse(**sample_response)
    print(f"\nIncomeID: {pprint.pformat(getattr(obj, IncomesInfoKeys.INCOME_ID))}")