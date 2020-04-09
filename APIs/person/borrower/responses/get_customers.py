from APIs.person.borrower.models.customers import CustomerList, CustomerListKeys
from base.common.response import CommonResponse


class GetCustomers(CommonResponse):
    ADD_KEYS = [CustomerListKeys.CUSTOMERS]
    SUB_MODELS = [CustomerList]
