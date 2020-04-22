from APIs.data_check.models.datacheck import DataChecks, EvaluateDataCheckBundleKeys
from base.common.response import CommonResponse


class EvaluateDataCheckBundle(CommonResponse):
    _ADD_KEYS = [EvaluateDataCheckBundleKeys.DATA_CHECKS]
    _SUB_MODELS = [DataChecks]
