from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class GetLoanStatusVendorTypesInfoKeys:
    CONTACT_TYPE: str = "ContactType"
    DISPLAY_NAME: str = "DisplayName"
    STATUS_ID: str = "StatusID"
    CONTACT_ID: str = "ContactID"


@dataclass
class GetLoanStatusVendorTypesKeys:
    LOAN_STATUS_VENDOR_TYPES: str = "LoanStatusVendorTypes"


class GetLoanStatusVendorType(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(GetLoanStatusVendorTypesInfoKeys)]


class GetLoanStatusVendorTypes(BaseListResponse):
    _SUB_MODEL = GetLoanStatusVendorType
