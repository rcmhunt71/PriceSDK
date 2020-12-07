from APIs.tpo.models.tpo_configurations import TPOConfigurationsKeys, ContactGroupsList, CompanyTPOAdminsList
from base.common.response import CommonResponse


class GetTPOConfigurationsResponse(CommonResponse):
    _ADD_KEYS = [TPOConfigurationsKeys.CONTACT_GROUPS, TPOConfigurationsKeys.COMPANY_TPO_ADMINS]
    _SUB_MODELS = [ContactGroupsList, CompanyTPOAdminsList]
