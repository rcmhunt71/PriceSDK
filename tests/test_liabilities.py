from random import choice, randrange
import unittest

from APIs.liabilities.models.liability import LiabilitiesKeys, Liability, LiabilitiesInfoKeys, Liabilities
from APIs.liabilities.responses.get_liabilities import GetLiabilitiesResponse
from APIs.liabilities.responses.add_liability import AddLiabilityResponse
from tests.common.common_response_args import CommonResponseValidations, response_args

liability_types = ["other", "revolving", "HELOC", "auto"]
applicant_names = ["Jane Doe", "John Doe", "Freddy Kruger", "Jason (NLN)", "Michael Myers"]
yes_no = ["Yes", "No"]

NUMBER_OF_LIABILITIES = 15


def build_liability_entry():
    return {
        LiabilitiesInfoKeys.LIABILITY_ID: randrange(10),
        LiabilitiesInfoKeys.CUSTOMER_ID: randrange(99999999),
        LiabilitiesInfoKeys.INSTITUTION_ID: randrange(99999999),
        LiabilitiesInfoKeys.LIABILITY_TYPE: choice(liability_types),
        LiabilitiesInfoKeys.ACCOUNT_NAME: choice(applicant_names),
        LiabilitiesInfoKeys.ACCOUNT_NUMBER: randrange(99999999),
        LiabilitiesInfoKeys.BALANCE: randrange(100000),
        LiabilitiesInfoKeys.TERM: randrange(60),
        LiabilitiesInfoKeys.PAYMENT: randrange(10, 1000),
        LiabilitiesInfoKeys.PAYOFF: randrange(100000),
        LiabilitiesInfoKeys.TO_BE_PAID_OFF: choice(yes_no)
    }


def build_liabilities_data():
    return [build_liability_entry() for _ in range(NUMBER_OF_LIABILITIES)]


class TestLiabilities(unittest.TestCase, CommonResponseValidations):
    def test_liability_entry_model(self):
        data = build_liability_entry()
        model = Liability(**data)
        self._validate_response(model=model, model_data=data)

    def test_liabilities_entries_list_model(self):
        data = build_liabilities_data()
        model = Liabilities(*data)

        self._verify(descript=f"{model.model_name} has the correct number of elements.",
                     actual=len(model), expected=len(data))

        for index, sub_model in enumerate(model):
            self._validate_response(model=sub_model, model_data=data[index])

    def test_GetLiabilities_response(self):
        key = LiabilitiesKeys.LIABILITIES
        data = response_args.copy()
        data[key] = build_liabilities_data()
        response = GetLiabilitiesResponse(**data)

        self._verify(descript=f"{response.model_name} has {key} attribute",
                     actual=hasattr(response, key), expected=True)
        self._validate_response(model=response, model_data=data)


class TestAddLiability(unittest.TestCase, CommonResponseValidations):
    def test_AddLiability_response(self):
        data = response_args.copy()
        data[LiabilitiesInfoKeys.LIABILITY_ID] = randrange(999999)
        response = AddLiabilityResponse(**data)
        self._validate_response(model=response, model_data=data)


if __name__ == '__main__':
    unittest.main()
