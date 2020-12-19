from base.common.response import CommonResponse
from APIs.loans.models.export_loan import ExportLoanKeys, ExportLoanList


class ExportLoanResponse(CommonResponse):
    _ADD_KEYS = [ExportLoanKeys.LOAN]
    _SUB_MODELS = [ExportLoanList]
