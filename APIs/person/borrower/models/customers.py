from dataclasses import dataclass

from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class CustomerKeys:
    CUSTOMER_ID: str = "CustomerID"
    DECLARE_A: str = "DeclareA"
    DECLARE_B: str = "DeclareB"


@dataclass
class CustomerListKeys:
    CUSTOMERS: str = "Customers"


class Customer(BaseResponse):
    _ADD_KEYS = [CustomerKeys.CUSTOMER_ID, CustomerKeys.DECLARE_A, CustomerKeys.DECLARE_B]
    _SUB_MODELS = [None for _ in range(len(_ADD_KEYS))]


class CustomerList(BaseListResponse):
    _SUB_MODEL = Customer

