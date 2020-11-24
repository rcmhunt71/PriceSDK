import unittest
from random import choice, randrange

from APIs.companies.models.companies import CompaniesKeys, Companies, CompaniesInfoKeys
from APIs.companies.responses.add_company import AddCompanyResponse
from APIs.companies.responses.get_companies import GetCompaniesResponse
from APIs.companies.responses.get_company_ids import GetCompanyIDsResponse, GetCompanyIDsKeys
from logger.logging import Logger
from tests.common.common_response_args import CommonResponseValidations, response_args

log = Logger()

# ---------------------------------------------------------------
#            COMPANY TEST DATA
# ---------------------------------------------------------------

num_company_ids = 6
num_companies = 3
states = ['NY', 'TX', 'CA', 'FL']
cities = ['Rome', 'Albany', 'Montpelier', 'Marlborough']
company_ids_list = [randrange(999) for _ in range(num_company_ids)]


def build_company_args():
    return {
        CompaniesInfoKeys.COMPANY_ID: choice(company_ids_list),
        CompaniesInfoKeys.COMPANY_NAME: f"Test Company {randrange(99):02}",
        CompaniesInfoKeys.VOICE: f'555{randrange(9999999):07}',
        CompaniesInfoKeys.ADDRESS: f"{randrange(9999)} SomePlace Drive",
        CompaniesInfoKeys.CITY: choice(cities),
        CompaniesInfoKeys.STATE: choice(states),
        CompaniesInfoKeys.ZIP: f"{randrange(99999):05}",
    }


companies_arg_list = [build_company_args() for _ in range(num_companies)]


# ---------------------------------------------------------------
#     TEST COMPANY MODELS AND RESPONSES
# ---------------------------------------------------------------
class TestCompany(unittest.TestCase, CommonResponseValidations):

    def test_companies_model(self):
        companies_model = Companies(*companies_arg_list)

        # Verify model has correct number of elements and corresponding data
        self._verify(
            descript=f"{companies_model.model_name}: Company lists are identical",
            actual=len(companies_arg_list), expected=len(companies_model))

        for index, data_model in enumerate(companies_arg_list):
            self._validate_response(model=companies_model[index], model_data=data_model)

    def test_add_company_response(self):
        add_company_args = response_args.copy()
        company_resp = AddCompanyResponse(**add_company_args)

        # Verify model has correct data
        self._validate_response(model=company_resp, model_data=add_company_args)

    def test_get_companies_response(self):
        get_company_args = response_args.copy()
        get_company_args[CompaniesKeys.COMPANIES] = companies_arg_list
        companies_resp = GetCompaniesResponse(**get_company_args)

        # Verify common response has CompaniesKeys.COMPANIES attribute
        self._verify(
            descript=f"{companies_resp.model_name}: Model has '{CompaniesKeys.COMPANIES}' attribute",
            actual=hasattr(companies_resp, CompaniesKeys.COMPANIES), expected=True)

        self._verify(
            descript=f"{companies_resp.model_name}: Company lists are identical",
            actual=len(getattr(companies_resp, CompaniesKeys.COMPANIES)),
            expected=len(companies_arg_list))

        # Verify CompaniesKeys.COMPANIES attribute contains correct data
        for index, company_model in enumerate(getattr(companies_resp, CompaniesKeys.COMPANIES)):
            self._validate_response(model=company_model, model_data=companies_arg_list[index])

        # Verify common response portion of response has correct data
        self._validate_response(model=companies_resp, model_data=get_company_args)

    def test_get_company_ids_response(self):
        company_ids_args = response_args.copy()
        company_ids_args[GetCompanyIDsKeys.COMPANY_IDS] = company_ids_list
        company_ids_response = GetCompanyIDsResponse(**company_ids_args)

        # Verify CompaniesKeys.COMPANY_IDs attribute contains correct data
        self._verify(
            descript=f"{company_ids_response.model_name}: Company id lists are identical",
            actual=getattr(company_ids_response, GetCompanyIDsKeys.COMPANY_IDS),
            expected=company_ids_list)

        # Verify common response portion of response has correct data
        self._validate_response(model=company_ids_response, model_data=company_ids_args)


if __name__ == '__main__':
    unittest.main()
