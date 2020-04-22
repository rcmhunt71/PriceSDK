from base.common.response import CommonResponse

from APIs.person.borrower.models.loan_list import CustomerLoanList, CustomerLoanListKeys


class GetCustomerLoanList(CommonResponse):
    _ADD_KEYS = [CustomerLoanListKeys.CUSTOMER_LOAN]
    _SUB_MODELS = [CustomerLoanList]
