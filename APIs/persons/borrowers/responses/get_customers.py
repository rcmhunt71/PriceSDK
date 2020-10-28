from APIs.persons.borrowers.models.customer import Customers, CustomersKeys
from base.common.response import CommonResponse


class GetCustomersResponse(CommonResponse):
    _ADD_KEYS = [CustomersKeys.CUSTOMERS]
    _SUB_MODELS = [Customers]
