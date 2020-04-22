from APIs.extra_data.models.extra_data import (ExtraDataEntryList, ExtraDataKeys,
                                                     ExtraDataMetadataKeys, ExtraDataMetadataEntryList)
from base.common.response import CommonResponse


class ExtraData(CommonResponse):
    _ADD_KEYS = [ExtraDataKeys.EXTRA_DATA, ExtraDataMetadataKeys.EXTRA_DATA_METADATA]
    _SUB_MODELS = [ExtraDataEntryList, ExtraDataMetadataEntryList]
