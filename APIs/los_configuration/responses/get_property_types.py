from APIs.los_configuration.models.get_property_types import GetPropertyTypesKeys, GetPropertyTypesList
from base.common.response import CommonResponse


class GetPropertyTypesResponse(CommonResponse):
    _ADD_KEYS = [GetPropertyTypesKeys.PROPERTY_TYPES]
    _SUB_MODELS = [GetPropertyTypesList]
