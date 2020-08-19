from APIs.property.models.property_liens import PropertyLiensKeys, PropertyLiens
from base.common.response import CommonResponse


class GetPropertyLiensResponse(CommonResponse):
    _ADD_KEYS = [PropertyLiensKeys.PROPERTYLIENS]
    _SUB_MODELS = [PropertyLiens]
