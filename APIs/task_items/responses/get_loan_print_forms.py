from APIs.task_items.models.get_loan_print_forms import GetLoanPrintFormsList, GetLoanPrintFormsKeys
from base.common.response import CommonResponse


class GetLoanPrintFormsResponse(CommonResponse):
    _ADD_KEYS = [GetLoanPrintFormsKeys.LOAN_PRINT_FORMS]
    _SUB_MODELS = [GetLoanPrintFormsList]
