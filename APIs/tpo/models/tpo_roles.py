from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class TPORolesInfoKeys:
    TPO_ROLE_ID: str = "TPORoleID"
    ROLE_NAME: str = "RoleName"
    SECURITY_LEVEL: str = "SecurityLevel"
    PRINT_FORM_LEVEL: str = "PrintFormLevel"


@dataclass
class TPORolesKeys:
    TPO_ROLES: str = "TPORoles"


class TPORoles(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(TPORolesInfoKeys)]


class TPORolesList(BaseListResponse):
    _SUB_MODEL = TPORoles
