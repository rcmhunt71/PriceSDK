from dataclasses import dataclass, fields

from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class IncomesInfoKeys:
    CUSTOMER_ID: str = "CustomerID"
    INCOME_ID: str = "IncomeID"
    COMPANY_ID: str = "CompanyID"
    INCOME_TYPE: str = "IncomeType"
    TITLE_POSITION: str = "TitlePosition"
    BASE_INCOME: str = "BaseIncome"
    OVERTIME: str = "Overtime"
    BONUSES: str = "Bonuses"
    COMMISSION: str = "Commission"
    OTHER: str = "Other"
    OTHER_DESCRIPTION: str = "OtherDescription"
    TOTAL: str = "Total"
    START_DATE: str = "StartDate"
    END_DATE: str = "EndDate"
    YEARS_AT_JOB: str = "YearsAtJob"
    MILITARY_ENTITLEMENTS: str = "MilitaryEntitlements"
    EMPLOYER_RELATIONSHIP_INDICATOR: str = "EmployerRelationshipIndicator"


@dataclass
class IncomesKeys:
    INCOMES: str = "Incomes"

class Income(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(IncomesInfoKeys)]


class Incomes(BaseListResponse):
    _SUB_MODEL = Income
