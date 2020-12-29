from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class GetCreditAgencyListInfoKeys:
    AGENCY_NAME: str = "AgencyName"


@dataclass
class GetCreditAgencyListKeys:
    DATA: str = "Data"


class GetCreditAgencies(BaseResponse):
    _ADD_KEYS = [GetCreditAgencyListInfoKeys.AGENCY_NAME]


class GetCreditAgencyList(BaseListResponse):
    _SUB_MODEL = GetCreditAgencies
