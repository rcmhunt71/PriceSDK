from APIs.credits.models.credit_report_import import ImportCreditReportKeys
from base.common.response import CommonResponse


class ImportCreditReportResponse(CommonResponse):
    _ADD_KEYS = [ImportCreditReportKeys.WAS_THERE_ANYTHING_IMPORTED, ImportCreditReportKeys.IMPORT_ERROR_MESSAGE]
    _SUB_MODELS = [None, None]
