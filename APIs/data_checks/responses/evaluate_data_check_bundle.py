from APIs.data_checks.models.datacheck import DataChecks, EvaluateDataCheckBundleKeys
from base.common.response import CommonResponse


class EvaluateDataCheckBundleResponse(CommonResponse):
    _ADD_KEYS = [EvaluateDataCheckBundleKeys.DATA_CHECKS]
    _SUB_MODELS = [DataChecks]
