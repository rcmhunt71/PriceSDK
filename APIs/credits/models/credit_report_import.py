from dataclasses import dataclass, fields

from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class IsCreditReportImportReadyKeys:
    READY_TO_IMPORT: str = "ReadyToImport"
    IMPORT_HINTS: str = "ImportHints"


class IsCreditReportImportReady(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(IsCreditReportImportReadyKeys)]


@dataclass
class ImportCreditReportKeys:
    WAS_THERE_ANYTHING_IMPORTED: str = "WasThereAnythingImported"
    IMPORT_ERROR_MESSAGE: str = "ImportErrorMessage"


class ImportCreditReport(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(ImportCreditReportKeys)]
