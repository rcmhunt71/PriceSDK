from APIs.credit.models.credit_report_import_ready import CreditReportImportReadyKeys
from base.common.response import CommonResponse


class CreditReportImportReady(CommonResponse):
    _ADD_KEYS = [CreditReportImportReadyKeys.READY_TO_IMPORT]
    _SUB_MODELS = [None]
