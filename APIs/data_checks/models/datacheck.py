from dataclasses import dataclass, fields

from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class DataCheckInfoKeys:
    DATA_CHECK_ID: str = "DataCheckID"
    NAME: str = "Name"
    DESCRIPTION: str = "Description"
    RESULT: str = "Result"


@dataclass
class EvaluateDataCheckBundleKeys:
    DATA_CHECKS: str = "DataChecks"


class DataCheck(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(DataCheckInfoKeys)]


class DataChecks(BaseListResponse):
    _SUB_MODEL = DataCheck
