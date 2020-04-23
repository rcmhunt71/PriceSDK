from dataclasses import dataclass

from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class ExtraDataEntryKeys:
    DATA_NAME: str = "DataName"
    DATA_VALUE: str = "DataValue"
    DATA_NUMERIC_VALUE: str = "DataNumericValue"
    ROW_NUMBER_ID: str = "RowNumberID"


@dataclass
class ExtraDataMetadataEntryKeys:
    DATA_NAME: str = "DataName"
    DATA_VALUE: str = "DataValue"
    EXTRA_DATA_TYPE: str = "ExtraDataType"


@dataclass
class ExtraDataKeys:
    EXTRA_DATA: str = "ExtraData"


@dataclass
class ExtraDataMetadataKeys:
    EXTRA_DATA_METADATA: str = "ExtraDataMetadata"


class ExtraDataEntry(BaseResponse):
    _ADD_KEYS = [ExtraDataEntryKeys.DATA_NAME, ExtraDataEntryKeys.DATA_NUMERIC_VALUE,
                ExtraDataEntryKeys.DATA_VALUE, ExtraDataEntryKeys.ROW_NUMBER_ID]


class ExtraDataEntryList(BaseListResponse):
    _SUB_MODEL = ExtraDataEntry


class ExtraDataMetadataEntry(BaseResponse):
    _ADD_KEYS = [ExtraDataMetadataEntryKeys.DATA_NAME, ExtraDataMetadataEntryKeys.DATA_VALUE,
                ExtraDataMetadataEntryKeys.EXTRA_DATA_TYPE]


class ExtraDataMetadataEntryList(BaseListResponse):
    _SUB_MODEL = ExtraDataMetadataEntry
