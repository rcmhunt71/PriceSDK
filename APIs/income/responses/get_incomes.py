from APIs.income.models.income import IncomeEntries, IncomeKeys
from base.common.response import CommonResponse


class GetIncomes(CommonResponse):
    _ADD_KEYS = [IncomeKeys.INCOMES]
    _SUB_MODELS = [IncomeEntries]
