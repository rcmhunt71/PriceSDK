from APIs.los_configuration.models.get_configuration_list_multiple import GetConfigurationListMultipleList, \
    GetConfigurationListMultipleKeys
from base.common.response import CommonResponse


class GetConfigurationListMultipleResponse(CommonResponse):
    _ADD_KEYS = [GetConfigurationListMultipleKeys.CONFIGURATION_LIST]
    _SUB_MODELS = [GetConfigurationListMultipleList]
