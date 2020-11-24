from APIs.companies.models.companies import CompaniesKeys, Companies
from base.common.response import CommonResponse


class GetCompaniesResponse(CommonResponse):
    _ADD_KEYS = [CompaniesKeys.COMPANIES]
    _SUB_MODELS = [Companies]


class GetCompaniesByIDsResponse(GetCompaniesResponse):
    pass
