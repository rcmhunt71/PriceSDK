from base.common.response import CommonResponse
from APIs.income.models.income import AddIncomeKeys


class AddIncome(CommonResponse):
    _ADD_KEYS = [AddIncomeKeys.INCOME_ID]
    _SUB_MODELS = [None]
