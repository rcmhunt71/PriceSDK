from dataclasses import dataclass

from APIs.company.models.company import Company
from base.responses.base_response import BaseListResponse


@dataclass
class CompaniesKeys:
    COMPANIES: str = 'Companies'


class Companies(BaseListResponse):
    SUB_MODEL = Company
