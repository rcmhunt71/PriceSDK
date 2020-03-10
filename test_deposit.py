import unittest
from random import randrange, choice

from APIs.deposit.models.add_deposit import AddDepositKeys
from APIs.deposit.models.deposit import DepositKeys, Deposit, DepositsKeys, Deposits
from APIs.deposit.models.deposit_account import (DepositAccountKeys, DepositAccount,
                                                 DepositAccounts, DepositAccountsKeys,
                                                 DepositAccountsFieldsKeys, DepositAccountFieldEntry,
                                                 DepositAccountFieldList, DepositAccountRequestModel)
from APIs.deposit.responses.add_deposit import AddDeposit
from APIs.deposit.responses.get_deposit_accounts import GetDepositAccounts
from APIs.deposit.responses.get_deposits import GetDeposits
from PRICE.tests.common_response_args import CommonResponseValidations, response_args

YES_NO = ["Yes", "No"]
ACCOUNT_TYPES = ["Checking", "Savings", "CD", "Escrow"]
NUMBER_OF_DEPOSIT_DATA_ELEMS = 3
NUMBER_OF_DEPOSIT_ACCOUNT_FIELD_ELEMS = 4

DEPOSIT_ID = f"{randrange(999999999):09}"
DEPOSIT_ACCOUNT_ID = f"{randrange(9999999):07}"

DEPOSIT_ACCT_FIELD_ACCT_TYPE = "Account_Type"
DEPOSIT_ACCT_FIELD_ACCT_NAME = "Account_Name"
DEPOSIT_ACCOUNT_FIELD_VALUES = {
        DEPOSIT_ACCT_FIELD_ACCT_TYPE: ["Savings", "Checking", "IRA", "CD"],
        DEPOSIT_ACCT_FIELD_ACCT_NAME: ["John Homeowner", "Jane Homeowner", "Bob Renter", "Doris Renter"],
}


def build_deposit_data_format():
    return {DepositKeys.CUSTOMER_ID: randrange(4455669985),
            DepositKeys.DEPOSIT_ID: randrange(1122334455),
            DepositKeys.INSTITUTION_ID: randrange(5566884423),
            DepositKeys.VERIFY: choice(YES_NO),
            DepositKeys.VERIFY_DATA: f"{randrange(9999):04}-{randrange(99):02}-{randrange(99):02}",
            DepositKeys.BOTH: choice(YES_NO)}


def build_deposit_account_format():
    return {DepositAccountKeys.CUSTOMER_ID: randrange(1122344566),
            DepositAccountKeys.DEPOSIT_ID: randrange(10),
            DepositAccountKeys.DEPOSIT_ACCOUNT_ID: randrange(10),
            DepositAccountKeys.ACCOUNT_TYPE: choice(ACCOUNT_TYPES),
            DepositAccountKeys.ACCOUNT_NUMBER: "",
            DepositAccountKeys.BALANCE: randrange(9999999)}


def build_set_deposit_account_fields():
    name_field = DEPOSIT_ACCT_FIELD_ACCT_NAME
    type_field = DEPOSIT_ACCT_FIELD_ACCT_TYPE
    return {
        DepositAccountsFieldsKeys.FIELD_NAME: choice(DEPOSIT_ACCOUNT_FIELD_VALUES[type_field]),
        DepositAccountsFieldsKeys.FIELD_VALUE: choice(DEPOSIT_ACCOUNT_FIELD_VALUES[name_field])
    }


deposits_data_list = [build_deposit_data_format() for _ in range(NUMBER_OF_DEPOSIT_DATA_ELEMS)]
deposit_accounts_data_list = [build_deposit_account_format() for _ in range(NUMBER_OF_DEPOSIT_DATA_ELEMS)]
deposit_account_field_data_list = [build_set_deposit_account_fields() for _ in
                                   range(NUMBER_OF_DEPOSIT_ACCOUNT_FIELD_ELEMS)]


def build_deposit_account_data_model():
    return {
        DepositAccountKeys.CUSTOMER_ID: randrange(99),
        DepositAccountKeys.DEPOSIT_ID: randrange(999999),
        DepositAccountKeys.DEPOSIT_ACCOUNT_ID: f"{randrange(99999999):08}",
        DepositAccountKeys.FIELDS: deposit_account_field_data_list,
    }


class TestDepositAccount(unittest.TestCase, CommonResponseValidations):
    def test_deposit_account_model(self):
        deposit_acct_model = DepositAccount(**deposit_accounts_data_list[0])
        self._validate_response(model=deposit_acct_model, model_data=deposit_accounts_data_list[0])

    def test_deposit_accounts_list_model(self):
        deposit_accts_list_model = DepositAccounts(*deposit_accounts_data_list)

        self._verify(descript=f"{deposit_accts_list_model.model_name}: has correct number of elements in list",
                     actual=len(deposit_accts_list_model), expected=len(deposit_accounts_data_list))

        for index, sub_model in enumerate(deposit_accts_list_model):
            self._validate_response(model=sub_model, model_data=deposit_accounts_data_list[index])

    def test_GetDepositAccounts_response(self):
        dep_key = DepositAccountsKeys.DEPOSIT_ACCOUNTS

        dep_args = response_args.copy()
        dep_args[dep_key] = deposit_accounts_data_list
        dep_accts_resp = GetDepositAccounts(**dep_args)

        self._verify(descript=f"{dep_accts_resp.model_name}: has '{dep_key}' attribute",
                     actual=hasattr(dep_accts_resp, dep_key), expected=True)
        self._validate_response(model=dep_accts_resp, model_data=dep_args)


class TestDeposits(unittest.TestCase, CommonResponseValidations):
    def test_deposit_model(self):
        deposit_model = Deposit(**deposits_data_list[0])
        self._validate_response(model=deposit_model, model_data=deposits_data_list[0])

    def test_deposits_list_model(self):
        deposit_list_model = Deposits(*deposits_data_list)

        self._verify(descript=f"{deposit_list_model.model_name}: has correct number of elements in list",
                     actual=len(deposit_list_model), expected=len(deposits_data_list))

        for index, sub_model in enumerate(deposit_list_model):
            self._validate_response(model=sub_model, model_data=deposits_data_list[index])

    def test_GetDeposits_response(self):
        dep_key = DepositsKeys.DEPOSITS

        dep_args = response_args.copy()
        dep_args[dep_key] = deposits_data_list
        deposits_resp = GetDeposits(**dep_args)

        self._verify(descript=f"{deposits_resp.model_name}: has '{dep_key}' attribute",
                     actual=hasattr(deposits_resp, dep_key), expected=True)
        self._validate_response(model=deposits_resp, model_data=dep_args)


class TestAddDeposit(unittest.TestCase, CommonResponseValidations):
    def test_AddDeposit_response(self):
        add_deposit_args = response_args.copy()
        add_deposit_args[AddDepositKeys.DEPOSIT_ACCOUNT_ID] = DEPOSIT_ACCOUNT_ID
        add_deposit_args[AddDepositKeys.DEPOSIT_ID] = DEPOSIT_ID
        add_dep_resp = AddDeposit(**add_deposit_args)

        self._validate_response(model=add_dep_resp, model_data=add_deposit_args)


class TestSetDepositAccounts(unittest.TestCase, CommonResponseValidations):
    def test_deposit_account_field_entry_model(self):
        model_data = deposit_account_field_data_list[0]
        deposit_acct_field_model = DepositAccountFieldEntry(**model_data)
        self._validate_response(model=deposit_acct_field_model, model_data=model_data)

    def test_deposit_account_field_list_model(self):
        model_data = deposit_account_field_data_list
        deposit_acct_field_model = DepositAccountFieldList(*model_data)

        self._verify(descript=f"{deposit_acct_field_model.model_name}: has correct number of elements.",
                     actual=len(deposit_acct_field_model), expected=len(model_data))

        for index, sub_model in enumerate(deposit_acct_field_model):
            self._validate_response(model=sub_model, model_data=model_data[index])

    def test_deposit_account_model(self):
        model_data = build_deposit_account_data_model()
        deposit_account_model = DepositAccountRequestModel(**model_data)
        self._verify(descript=f"{deposit_account_model.model_name}: "
                              f"has correct number of elements in {DepositAccountKeys.FIELDS}.",
                     actual=len(getattr(deposit_account_model, DepositAccountKeys.FIELDS)),
                     expected=len(model_data.get(DepositAccountKeys.FIELDS)))

        self._validate_response(model=deposit_account_model, model_data=model_data)


if __name__ == '__main__':
    unittest.main()
