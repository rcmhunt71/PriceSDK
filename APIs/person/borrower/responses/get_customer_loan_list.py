from base.common.response import CommonResponse

from APIs.person.borrower.models.loan_list import CustomerLoanList, CustomerLoanListKeys


class GetCustomerLoanList(CommonResponse):
    ADD_KEYS = [CustomerLoanListKeys.CUSTOMER_LOAN]
    SUB_MODELS = [CustomerLoanList]
