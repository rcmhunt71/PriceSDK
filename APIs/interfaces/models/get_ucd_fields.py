from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class GetUCDFieldsInfoKeys:
    SUBMISSION_DATE_TIME: str = "SubmissionDateTime"
    SUBMISSION_STATUS: str = "SubmissionStatus"
    SUBMISSION_NUMBER: str = "SubmissionNumber"
    RESPONSE_DATE_ISSUED: str = "ResponseDateIssued"
    BATCH_ID: str = "BatchID"
    TRANSACTION_ID: str = "TransactionID"
    STATUS_GENERAL_INFO: str = "StatusGeneralInfo"
    STATUS_DATA_QUALITY: str = "StatusDataQuality"
    STATUS_ELIGIBILITY: str = "StatusEligibility"
    IS_EMBEDDED_PDF: str = "isEmbeddedPDF"
    ASSIGNMENT_DATE: str = "AssignmentDate"
    ASSIGNMENT_CONFIRMATION_DATE: str = "AssignmentConfirmationDate"


@dataclass
class GetUCDFieldsKeys:
    DATA: str = "Data"


class GetUCDFields(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(GetUCDFieldsInfoKeys)]


class GetUCDFieldsList(BaseListResponse):
    _SUB_MODEL = GetUCDFields
