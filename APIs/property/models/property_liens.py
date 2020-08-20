from dataclasses import dataclass, fields
from base.responses.base_response import BaseListResponse, BaseResponse


@dataclass
class PropertyLiensKeys:
    PROPERTYLIENS: str = 'PropertyLiens'


@dataclass
class PropertyLienKeys:
    CUSTOMER_ID: str = 'CustomerID'
    PROPERTY_LIEN_ID: str = 'PropertyLienID'
    PROPERTY_ID: str = 'PropertyID'
    INSTITUTION_ID: str = 'InstitutionID'
    ACCOUNT_NUMBER: str = 'AccountNumber'
    BALANCE: str = 'Balance'
    PAYMENT: str = 'Payment'
    TERM: str = 'Term'
    TO_BE_PAID_OFF: str = 'ToBePaidOff'


class PropertyLien(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(PropertyLienKeys)]


class PropertyLiens(BaseListResponse):
    _SUB_MODEL = PropertyLien
