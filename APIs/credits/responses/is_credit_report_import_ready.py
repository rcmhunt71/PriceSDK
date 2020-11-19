from APIs.credits.models.credit_report_import import IsCreditReportImportReadyKeys
from base.common.response import CommonResponse


class IsCreditReportImportReadyResponse(CommonResponse):
    _ADD_KEYS = [IsCreditReportImportReadyKeys.READY_TO_IMPORT, IsCreditReportImportReadyKeys.IMPORT_HINTS]
    _SUB_MODELS = [None, None]
