from dataclasses import dataclass

from APIs.company.models.company import Company
from base.responses.base_response import BaseListResponse


@dataclass
class CompaniesKeys:
    COMPANIES: str = 'Companies'


class Companies(BaseListResponse):
    _SUB_MODEL = Company
