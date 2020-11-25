from dataclasses import dataclass, fields

from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class GetVirtualDataGridFieldKeys:
    FIELD_NAME: str = "FieldName"
    FIELD_VALUE: str = "FieldValue"


@dataclass
class GetVirtualDataGridSectionKeys:
    SECTION: str = "Section"
    SECTION_VALUE: str = "SectionValue"


@dataclass
class GetVirtualDataGridTableKeys:
    TABLE_NAME: str = "TableName"
    DATA: str = "Data"


@dataclass
class GetVirtualDataGridKeys:
    VIRTUAL_DATA: str = "VirtualData"


class GetVirtualDataGridFieldEntry(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(GetVirtualDataGridFieldKeys)]


class GetVirtualDataGridFieldEntryList(BaseListResponse):
    _SUB_MODEL = GetVirtualDataGridFieldEntry


class GetVirtualDataGridSection(BaseResponse):
    _ADD_KEYS = [GetVirtualDataGridSectionKeys.SECTION, GetVirtualDataGridSectionKeys.SECTION_VALUE]
    _SUB_MODEL = [None, GetVirtualDataGridFieldEntryList]


class GetVirtualDataGridTable(BaseResponse):
    _ADD_KEYS = [GetVirtualDataGridTableKeys.TABLE_NAME, GetVirtualDataGridTableKeys.DATA]
    _SUB_MODEL = [None, GetVirtualDataGridSection]
