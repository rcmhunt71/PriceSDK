from base.common.response import CommonResponse

from APIs.persons.borrowers.models.loan_list import CustomerLoanListsKeys, CustomerLoanLists


class GetCustomerLoanListResponse(CommonResponse):
    _ADD_KEYS = [CustomerLoanListsKeys.CUSTOMER_LOANS]
    _SUB_MODELS = [CustomerLoanLists]
