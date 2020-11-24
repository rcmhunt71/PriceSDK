from dataclasses import dataclass

from base.clients.base_client import BaseClient
from base.common.models.request import LoanNumberIdRequestModel
from base.common.response import CommonResponse

from APIs.credits.requests.request_credit_report import RequestCreditReportRequest
from APIs.credits.responses.is_credit_report_import_ready import IsCreditReportImportReadyResponse
from APIs.credits.responses.import_credit_report import ImportCreditReportResponse


@dataclass
class ApiEndpoints:
    IS_CREDIT_REPORT_IMPORT_READY: str = "is_credit_report_import_ready"
    IMPORT_CREDIT_REPORT: str = "import_credit_report"
    REQUEST_CREDIT_REPORT: str = "request_credit_report"


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

    def request_credit_report(self, loan_number_id=None, rmcr=None, fm_du_id=None, pre_qualification=None, trw=None,
                              borrower_id_list=None, cbi=None, username=None, password=None, credit_company=None,
                              tu=None, payload_dict=None, session_id=None, nonce=None, pretty_print=False):
        request_model = RequestCreditReportRequest(loan_number_id=loan_number_id, rmcr=rmcr, fm_du_id=fm_du_id,
                                                   pre_qualification=pre_qualification, trw=trw,
                                                   borrower_id_list=borrower_id_list, cbi=cbi, username=username,
                                                   password=password, credit_company=credit_company, tu=tu,
                                                   payload_dict=payload_dict,
                                                   session_id=self._get_session_id(session_id),
                                                   nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.REQUEST_CREDIT_REPORT, response_model=CommonResponse,
                         params=request_model.as_params_dict, data=request_model.payload)
