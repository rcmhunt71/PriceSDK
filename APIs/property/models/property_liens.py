from dataclasses import dataclass, fields
from base.responses.base_response import BaseListResponse, BaseResponse


@dataclass
class PropertyLiensKeys:
    PROPERTYLIENS: str = 'PropertyLiens'


@dataclass
class PropertyLienKeys:
    CUSTOMERID: str = 'CustomerID'
    PROPERTYLIENID: str = 'PropertyLienID'
    PROPERTYID: str = 'PropertyID'
    INSTITUTIONID: str = 'InstitutionID'
    ACCOUNTNUMBER: str = 'AccountNumber'
    BALANCE: str = 'Balance'
    PAYMENT: str = 'Payment'
    TERM: str = 'Term'
    TOBEPAIDOFF: str = 'ToBePaidOff'


class PropertyLien(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(PropertyLienKeys)]


class PropertyLiens(BaseListResponse):
    _SUB_MODEL = PropertyLien
