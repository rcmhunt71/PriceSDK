from base.common.response import CommonResponse
from APIs.task_items.models.get_image_access_logs import GetImageAccessLogsKeys, GetImageAccessLogsList


class GetImageAccessLogsResponse(CommonResponse):
    _ADD_KEYS = [GetImageAccessLogsKeys.IMAGE_ACCESS_LOG]
    _SUB_MODELS = [GetImageAccessLogsList]
