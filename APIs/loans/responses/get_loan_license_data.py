from APIs.loans.models.license_data import Licenses, LicenseDataKeys
from base.common.response import CommonResponse


class GetLoanLicenseDataResponse(CommonResponse):
    ADD_KEYS = [LicenseDataKeys.LICENSE_DATA]
    SUB_MODELS = [Licenses]
