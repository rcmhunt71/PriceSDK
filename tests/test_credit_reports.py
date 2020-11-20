import unittest

from APIs.credits.models.credit_report_import import IsCreditReportImportReadyKeys, ImportCreditReportKeys
from APIs.credits.responses.import_credit_report import ImportCreditReportResponse
from APIs.credits.responses.is_credit_report_import_ready import IsCreditReportImportReadyResponse
from tests.common.common_response_args import CommonResponseValidations, response_args


# --------------------------------------------------
#             CREDIT REPORT TESTS
# --------------------------------------------------
class TestCreditReports(unittest.TestCase, CommonResponseValidations):
    def test_credit_report_import_ready_response(self):

        key = IsCreditReportImportReadyKeys.READY_TO_IMPORT
        import_ready_args = response_args.copy()
        import_ready_args[key] = True

        import_ready_response = IsCreditReportImportReadyResponse(**import_ready_args)
        self._validate_response(model=import_ready_response, model_data=import_ready_args)

    def test_import_credit_report_response(self):
        key = ImportCreditReportKeys.WAS_THERE_ANYTHING_IMPORTED
        import_report_args = response_args.copy()
        import_report_args[key] = False

        import_report_response = ImportCreditReportResponse(**import_report_args)
        self._validate_response(model=import_report_response, model_data=import_report_args)


if __name__ == '__main__':
    unittest.main()
