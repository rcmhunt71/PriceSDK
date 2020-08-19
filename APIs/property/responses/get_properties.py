from APIs.property.models.properties import Properties, PropertiesKeys
from base.common.response import CommonResponse


class GetPropertiesResponse(CommonResponse):
    _ADD_KEYS = [PropertiesKeys.PROPERTIES]
    _SUB_MODELS = [Properties]
