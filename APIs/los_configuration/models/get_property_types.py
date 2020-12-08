from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class GetPropertyTypesInfoKeys:
    F_PROPERTY_TYPE: str = "FPropertyType"
    F_SORT_FIELD: str = "FSortField"
    F_DESCRIPTION: str = "FDescription"


@dataclass
class GetPropertyTypesKeys:
    PROPERTY_TYPES: str = "PropertyTypes"


class GetPropertyTypes(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(GetPropertyTypesInfoKeys)]


class GetPropertyTypesList(BaseListResponse):
    _SUB_MODEL = GetPropertyTypes
