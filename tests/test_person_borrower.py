from random import choice, randrange
import unittest

from APIs.persons.borrowers.models.borrower import Borrower, BorrowersInfoKeys, Borrowers, BorrowersKeys
from APIs.persons.borrowers.models.loan_list import CustomerLoanListsInfoKeys,CustomerLoanListsKeys, CustomerLoanList
from APIs.persons.borrowers.responses.get_borrower import GetBorrowerResponse
from APIs.persons.borrowers.responses.get_customers import GetCustomersResponse
from APIs.persons.borrowers.responses.get_customer_loan_list import GetCustomerLoanListResponse
from APIs.persons.borrowers.models.customer import Customer, CustomersInfoKeys, Customers, CustomersKeys
from tests.common.common_response_args import CommonResponseValidations, response_args

NUMBER_OF_BORROWERS = 7
NUMBER_OF_CUSTOMERS = 5


def build_borrower():
    return {
        BorrowersInfoKeys.PERSON_ID: randrange(9999),
        BorrowersInfoKeys.FIRST_NAME: choice(["Fred", "John", "Jane", "Jill", "Mortimer", "Frieda"]),
        BorrowersInfoKeys.LAST_NAME: choice(["Jones", "Smith", "McTavish", "Beaumont", "Humphries", "Katovich"]),
    }


def build_customer():
    return {
        CustomersInfoKeys.CUSTOMER_ID: randrange(999999),
        CustomersInfoKeys.DECLARE_A: choice(["A", "B", "C", "D", "E"]),
        CustomersInfoKeys.DECLARE_B: choice(["V", "W", "X", "Y", "Z"]),
    }


def build_customer_loan_list():
    return {
        CustomerLoanListsInfoKeys.BORROWER_NUMBER: randrange(999999),
        CustomerLoanListsInfoKeys.CUSTOMER_ID: randrange(10)
    }


class TestPersonBorrower(unittest.TestCase, CommonResponseValidations):
    def test_borrower_model(self):
        data = build_borrower()
        model = Borrower(**data)
        self._validate_response(model=model, model_data=data)

    def test_borrower_list_model(self):
        data = [build_borrower() for _ in range(NUMBER_OF_BORROWERS)]
        model = Borrowers(*data)

        self._verify(f"{model.model_name}: Verify correct number of elements.",
                     actual=len(model), expected=len(data))

        for index, sub_model in enumerate(model):
            self._validate_response(model=sub_model, model_data=data[index])

    def test_GetBorrower_Response(self):
        key = BorrowersKeys.BORROWER_DETAIL

        data = response_args.copy()
        data[key] = [build_borrower() for _ in range(NUMBER_OF_BORROWERS)]
        response = GetBorrowerResponse(**data)

        self._verify(f"{response.model_name}: Verify response has '{key}' attribute.",
                     actual=hasattr(response, key), expected=True)
        self._validate_response(model=response, model_data=data)


class TestPersonCustomer(unittest.TestCase, CommonResponseValidations):
    def test_customer_model(self):
        data = build_customer()
        model = Customer(**data)
        self._validate_response(model=model, model_data=data)

    def test_customer_list(self):
        data = [build_customer() for _ in range(NUMBER_OF_CUSTOMERS)]
        model = Customers(*data)

        self._verify(f"{model.model_name}: Verify correct number of elements.",
                     actual=len(model), expected=len(data))

        for index, sub_model in enumerate(model):
            self._validate_response(model=sub_model, model_data=data[index])

    def test_GetCustomer_response(self):
        key = CustomersKeys.CUSTOMERS
        data = response_args.copy()
        data[key] = [build_customer() for _ in range(NUMBER_OF_CUSTOMERS)]
        response = GetCustomersResponse(**data)

        self._verify(f"{response.model_name}: Verify response has '{key}' attribute.",
                     actual=hasattr(response, key), expected=True)
        self._validate_response(model=response, model_data=data)


class TestCustomerLoanList(unittest.TestCase, CommonResponseValidations):
    def test_loan_list_header_entries_model(self):
        data = build_customer_loan_list()
        model = CustomerLoanList(**data)
        self._validate_response(model=model, model_data=data)

    def test_CustomerLoanList_response(self):
        key = CustomerLoanListsKeys.CUSTOMER_LOANS
        data = response_args.copy()
        data[key] = [build_customer_loan_list() for _ in range(NUMBER_OF_BORROWERS)]
        response = GetCustomerLoanListResponse(**data)

        self._verify(f"{response.model_name}: Verify response has '{key}' attribute.", actual = hasattr(response, key),
            expected = True)
        self._validate_response(model = response, model_data = data)


if __name__ == "__main__":
    unittest.main()
