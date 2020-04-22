from APIs.person.borrower.models.customers import CustomerList, CustomerListKeys
from base.common.response import CommonResponse


class SetCustomer(CommonResponse):
    _ADD_KEYS = [CustomerListKeys.CUSTOMERS]
    _SUB_MODELS = [CustomerList]
