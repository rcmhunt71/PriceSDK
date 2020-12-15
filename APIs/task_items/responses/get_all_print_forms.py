from base.common.response import CommonResponse
from APIs.task_items.models.get_all_print_forms import GetAllPrintFormsList, GetAllPrintFormsKeys


class GetAllPrintFormsResponse(CommonResponse):
    _ADD_KEYS = [GetAllPrintFormsKeys.ALL_PRINT_FORMS]
    _SUB_MODELS = [GetAllPrintFormsList]
