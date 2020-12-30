from APIs.interfaces.models.get_interface_problems import GetInterfaceProblemsKeys, GetInterfaceProblemsList
from base.common.response import CommonResponse


class GetInterfaceProblemsResponse(CommonResponse):
    _ADD_KEYS = [GetInterfaceProblemsKeys.DATA_CHECKS]
    _SUB_MODELS = [GetInterfaceProblemsList]
