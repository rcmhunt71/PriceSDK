from base.common.response import CommonResponse
from APIs.data_checks.models.evaluate_data_check_bundle_list import EvaluateDataCheckBundleListKeys, DataCheckBundleList


class EvaluateDataCheckBundleListResponse(CommonResponse):
    _ADD_KEYS = [EvaluateDataCheckBundleListKeys.DATA_CHECK_LISTS]
    _SUB_MODELS = [DataCheckBundleList]
