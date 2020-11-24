from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class AddCompanyParams(BaseRequestModelKeys):
    COMPANY_TYPE: str = "CompanyType"
    FIELD_NAME: str = "FieldName"
    FIELD_VALUE: str = "FieldValue"
    REFERENCED_ONLY_ONCE: str = "ReferencedOnlyOnce"
    EMPLOYEE_ID: str = "EmployeeID"


class AddCompanyRequest(SimpleRequestModel):
    def __init__(self, company_type, field_name, field_value, referenced_only_once, employee_id, session_id,
    nonce, pretty_print):
        self.company_type = company_type
        self.field_name = field_name
        self.field_value = field_value
        self.referenced_only_once = referenced_only_once
        self.employee_id = employee_id
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[AddCompanyParams.COMPANY_TYPE] = self.company_type
        args[AddCompanyParams.FIELD_NAME] = self.field_name
        args[AddCompanyParams.FIELD_VALUE] = self.field_value
        args[AddCompanyParams.REFERENCED_ONLY_ONCE] = self.referenced_only_once
        args[AddCompanyParams.EMPLOYEE_ID] = self.employee_id
        return args
