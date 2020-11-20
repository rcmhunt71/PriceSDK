from dataclasses import dataclass

from base.clients.base_client import BaseClient
from base.common.models.request import LoanNumberIdRequestModel

from APIs.credits.responses.is_credit_report_import_ready import IsCreditReportImportReadyResponse
from APIs.credits.responses.import_credit_report import ImportCreditReportResponse


@dataclass
class ApiEndpoints:
    IS_CREDIT_REPORT_IMPORT_READY: str = "is_credit_report_import_ready"
    IMPORT_CREDIT_REPORT: str = "import_credit_report"


class CreditsClient(BaseClient):

    def is_credit_report_import_ready(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
                                                 session_id=self._get_session_id(session_id),
                                                 nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.IS_CREDIT_REPORT_IMPORT_READY,
                        response_model=IsCreditReportImportReadyResponse, params=request_model.as_params_dict)

    def import_credit_report(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
                                                 session_id=self._get_session_id(session_id),
                                                 nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.IMPORT_CREDIT_REPORT, response_model=ImportCreditReportResponse,
                         params=request_model.as_params_dict, data=request_model.payload)
