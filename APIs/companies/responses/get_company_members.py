from APIs.companies.models.company_members import CompanyMembersKeys, CompanyMembersList
from base.common.response import CommonResponse


class GetCompanyMembersResponse(CommonResponse):
    _ADD_KEYS = [CompanyMembersKeys.MEMBERS]
    _SUB_MODELS = [CompanyMembersList]
