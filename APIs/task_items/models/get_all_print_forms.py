from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class GetAllPrintFormsInfoKeys:
    PRINT_FORM_ID: str = "PrintFormID"
    GROUP: str = "Group"


@dataclass
class GetAllPrintFormsKeys:
    ALL_PRINT_FORMS: str = "AllPrintForms"


class GetAllPrintForms(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(GetAllPrintFormsInfoKeys)]


class GetAllPrintFormsList(BaseListResponse):
    _SUB_MODEL = GetAllPrintForms
