from APIs.loans.models.license_data import Licenses, LicenseDataKeys
from base.common.response import CommonResponse


class GetLoanLicenseDataResponse(CommonResponse):
    _ADD_KEYS = [LicenseDataKeys.LICENSE_DATA]
    _SUB_MODELS = [Licenses]
