from base.common.response import CommonResponse
from APIs.task_items.models.get_image_thumbnail_multiple import GetImageThumbnailMultipleKeys, \
                                                                GetImageThumbnailMultipleList


class GetImageThumbnailMultipleResponse(CommonResponse):
    _ADD_KEYS = [GetImageThumbnailMultipleKeys.THUMBNAILS]
    _SUB_MODELS = [GetImageThumbnailMultipleList]
