from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse

@dataclass
class CompanyLicenseTypesInfoKeys:
    COMPANY_ID: str = "CompanyID"
    COMPANY_TYPE: str = "CompanyType"
    COMPANY_LICENSE_NUMBER: str = "CompanyLicenseNumber"


@dataclass
class CompanyLicenseTypesKeys:
    COMPANY_LICENSE_TYPES: str = "CompanyLicenseTypes"


class CompanyLicenseTypes(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(CompanyLicenseTypesInfoKeys)]


class CompanyLicenseTypesList(BaseListResponse):
    _SUB_MODEL = CompanyLicenseTypes
