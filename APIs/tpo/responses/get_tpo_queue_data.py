from APIs.tpo.models.tpo_queue_data import TPOQueueDataKeys, TPOQueueDataList
from base.common.response import CommonResponse


class GetTPOQueueDataResponse(CommonResponse):
    _ADD_KEYS = [TPOQueueDataKeys.TPO_QUEUE_DATA]
    _SUB_MODELS = [TPOQueueDataList]
