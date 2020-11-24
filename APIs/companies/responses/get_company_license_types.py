from APIs.companies.models.company_license_types import CompanyLicenseTypesKeys, CompanyLicenseTypesList
from base.common.response import CommonResponse


class GetCompanyLicenseTypesResponse(CommonResponse):
    _ADD_KEYS = [CompanyLicenseTypesKeys.COMPANY_LICENSE_TYPES]
    _SUB_MODELS = [CompanyLicenseTypesList]
