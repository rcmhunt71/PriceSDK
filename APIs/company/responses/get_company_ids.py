from dataclasses import dataclass

from base.common.response import CommonResponse


@dataclass
class GetCompanyIDsKeys:
    COMPANY_IDS: str = 'CompanyIds'


class GetCompanyIDsResponse(CommonResponse):
    _ADD_KEYS = [GetCompanyIDsKeys.COMPANY_IDS]
    _SUB_MODELS = [None]
