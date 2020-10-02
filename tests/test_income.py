from random import choice, randrange
import unittest

from APIs.incomes.models.income import IncomesInfoKeys, Income, IncomesKeys, Incomes
from APIs.incomes.responses.add_income import AddIncomeResponse
from APIs.incomes.responses.get_incomes import GetIncomesResponse
from tests.common.common_response_args import CommonResponseValidations, response_args

job_positions = ['engineer', 'cashier', 'public servant', 'politician', 'teacher', 'spouse']
other_descriptions = ['Alimony', 'Investments', 'Retired', "None"]

NUMBER_OF_INCOME_SOURCES = 5


def build_income_entry():
    return {
        IncomesInfoKeys.CUSTOMER_ID: randrange(999999999),
        IncomesInfoKeys.INCOME_ID: randrange(10),
        IncomesInfoKeys.COMPANY_ID: randrange(99999999),
        IncomesInfoKeys.INCOME_TYPE: randrange(10),
        IncomesInfoKeys.TITLE_POSITION: choice(job_positions),
        IncomesInfoKeys.BASE_INCOME: randrange(10000, 500000),

        IncomesInfoKeys.OVERTIME: randrange(1000, 10000),
        IncomesInfoKeys.BONUSES: randrange(1000, 10000),
        IncomesInfoKeys.COMMISSION: randrange(1000, 10000),
        IncomesInfoKeys.OTHER: randrange(1000, 10000),

        IncomesInfoKeys.OTHER_DESCRIPTION: choice(other_descriptions),
        IncomesInfoKeys.TOTAL: randrange(5000, 100000),
        IncomesInfoKeys.START_DATE: f"{randrange(2010, 2019)}-{randrange(1, 12)}-{randrange(1, 28)}",
        IncomesInfoKeys.END_DATE: f"{randrange(2010, 2019)}-{randrange(1, 12)}-{randrange(1, 28)}",
        IncomesInfoKeys.YEARS_AT_JOB: randrange(9),
    }


incomes = [build_income_entry() for _ in range(NUMBER_OF_INCOME_SOURCES)]


class TestIncome(unittest.TestCase, CommonResponseValidations):
    def test_income_entry(self):
        data = build_income_entry()
        model = Income(**data)
        self._validate_response(model=model, model_data=data)

    def test_incomes_list_model(self):
        model = Incomes(*incomes)

        self._verify(descript=f"{model.model_name} has correct number of elements.",
                     actual=len(model), expected=len(incomes))

        for index, sub_model in enumerate(model):
            self._validate_response(model=sub_model, model_data=incomes[index])

    def test_GetIncomes_response(self):
        data = response_args.copy()
        data[IncomesKeys.INCOMES] = incomes
        model = GetIncomesResponse(**data)

        key = IncomesKeys.INCOMES
        self._verify(descript=f"{model.model_name} has the {key} attribute",
                     actual=hasattr(model, key), expected=True)
        self._validate_response(model=model, model_data=data)


class TestAddIncome(unittest.TestCase, CommonResponseValidations):
    def test_AddIncome_response(self):
        add_income_args = response_args.copy()
        add_income_args[IncomesInfoKeys.INCOME_ID] = randrange(99999999)
        response = AddIncomeResponse(**add_income_args)

        self._validate_response(model=response, model_data=add_income_args)


if __name__ == '__main__':
    unittest.main()
