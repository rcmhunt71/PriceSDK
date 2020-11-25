from base.common.response import CommonResponse
from APIs.extra_and_virtual_data.models.get_virtual_data_grid import GetVirtualDataGridKeys, GetVirtualDataGridTable


class GetVirtualDataGridResponse(CommonResponse):
    _ADD_KEYS = [GetVirtualDataGridKeys.VIRTUAL_DATA]
    _SUB_MODELS = [GetVirtualDataGridTable]
