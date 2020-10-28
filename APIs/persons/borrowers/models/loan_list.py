from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class CustomerLoanListsInfoKeys:
    BORROWER_NUMBER: str = "BorrowerNumber"
    CUSTOMER_ID: str = "CustomerID"


@dataclass
class CustomerLoanListsKeys:
    CUSTOMER_LOANS: str = "CustomerLoans"

class CustomerLoanList(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(CustomerLoanListsInfoKeys)]

class CustomerLoanLists(BaseListResponse):
    _SUB_MODEL = CustomerLoanList
