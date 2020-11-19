from APIs.credits.models.credit_report_import import ImportCreditReportKeys
from base.common.response import CommonResponse


class ImportCreditReport(CommonResponse):
    _ADD_KEYS = [ImportCreditReportKeys.WAS_THERE_ANYTHING_IMPORTED]
    _SUB_MODELS = [None]
