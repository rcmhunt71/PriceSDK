from APIs.vendor_integration.models.verification_data import GetVerificationDataKeys
from base.common.response import CommonResponse


class GetVerificationDataResponse(CommonResponse):
    _ADD_KEYS = [GetVerificationDataKeys.VERIFICATION_OUTCOME, GetVerificationDataKeys.VERIFICATION_DATE]
    _SUB_MODELS = [None, None]
