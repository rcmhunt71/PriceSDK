from dataclasses import dataclass
from base.common.response import CommonResponse

@dataclass
class CompaniesInfoKeys:
    COMPANY_ID: str = "CompanyID"


class AddCompanyResponse(CommonResponse):
    _ADD_KEYS = [CompaniesInfoKeys.COMPANY_ID]
    _SUB_MODELS = [None]
