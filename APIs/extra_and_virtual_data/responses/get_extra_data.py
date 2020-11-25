from APIs.extra_and_virtual_data.models.extra_data import (ExtraDataList, ExtraDataKeys,
                                                           ExtraDataMetadataKeys, ExtraDataMetaDataList)
from base.common.response import CommonResponse


class GetExtraDataResponse(CommonResponse):
    _ADD_KEYS = [ExtraDataKeys.EXTRA_DATA, ExtraDataMetadataKeys.EXTRA_DATA_METADATA]
    _SUB_MODELS = [ExtraDataList, ExtraDataMetaDataList]
