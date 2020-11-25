from dataclasses import dataclass, fields

from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class ExtraDataInfoKeys:
    DATA_NAME: str = "DataName"
    DATA_VALUE: str = "DataValue"
    DATA_NUMERIC_VALUE: str = "DataNumericValue"
    ROW_NUMBER_ID: str = "RowNumberID"


@dataclass
class ExtraDataMetaDataInfoKeys:
    DISPLAY_NAME: str = "DisplayName"
    DATA_NAME: str = "DataName"
    EXTRA_DATA_TYPE: str = "ExtraDataType"


@dataclass
class ExtraDataKeys:
    EXTRA_DATA: str = "ExtraData"


@dataclass
class ExtraDataMetadataKeys:
    EXTRA_DATA_METADATA: str = "ExtraDataMetaData"


class ExtraData(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(ExtraDataInfoKeys)]


class ExtraDataList(BaseListResponse):
    _SUB_MODEL = ExtraData


class ExtraDataMetaData(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(ExtraDataMetaDataInfoKeys)]


class ExtraDataMetaDataList(BaseListResponse):
    _SUB_MODEL = ExtraDataMetaData
