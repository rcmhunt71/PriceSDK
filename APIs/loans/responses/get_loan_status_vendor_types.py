from APIs.loans.models.get_loan_status_vendor_types import GetLoanStatusVendorTypesKeys, GetLoanStatusVendorTypes
from base.common.response import CommonResponse


class GetLoanStatusVendorTypesResponse(CommonResponse):
    _ADD_KEYS = [GetLoanStatusVendorTypesKeys.LOAN_STATUS_VENDOR_TYPES]
    _SUB_MODELS = [GetLoanStatusVendorTypes]
