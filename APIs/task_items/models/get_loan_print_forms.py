from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class GetLoanPrintFormsInfoKeys:
    PRINT_ID: str = "PrintID"
    KEY_1: str = "Key1"
    KEY_2: str = "Key2"
    KEY_3: str = "Key3"
    KEY_4: str = "Key4"
    KEY_5: str = "Key5"
    PRINT_FORM_ID: str = "PrintFormID"
    SORT_FIELD: str = "SortField"
    DESCRIPTION: str = "Description"
    CATEGORY: str = "Category"
    COMPANY_NAME: str = "CompanyName"
    LEGAL: str = "Legal"


@dataclass
class GetLoanPrintFormsKeys:
    LOAN_PRINT_FORMS: str = "LoanPrintForms"


class GetLoanPrintForms(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(GetLoanPrintFormsInfoKeys)]


class GetLoanPrintFormsList(BaseListResponse):
    _SUB_MODEL = GetLoanPrintForms
