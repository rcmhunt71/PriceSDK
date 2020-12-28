from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class DataCheckInfoKeys:
    DATA_CHECK_ID: str = "DataCheckID"
    NAME: str = "Name"
    DESCRIPTION: str = "Description"
    RESULT: str = "Result"


@dataclass
class EvaluateDataCheckBundleListKeys:
    DATA_CHECK_LISTS: str = "DataCheckLists"


@dataclass
class EvaluateDataCheckBundleKeys:
    DATA_CHECK_BUNDLE_ID: str = "DataCheckBundleID"
    DATA_CHECKS: str = "DataChecks"


class DataCheck(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(DataCheckInfoKeys)]


class DataChecks(BaseListResponse):
    _SUB_MODEL = DataCheck


class DataCheckBundle(BaseResponse):
    _ADD_KEYS = [EvaluateDataCheckBundleKeys.DATA_CHECK_BUNDLE_ID, EvaluateDataCheckBundleKeys.DATA_CHECKS]
    _SUB_MODELS = [None, DataChecks]


class DataCheckBundleList(BaseListResponse):
    _SUB_MODEL = DataCheckBundle
