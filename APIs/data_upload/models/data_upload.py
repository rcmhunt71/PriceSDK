from dataclasses import dataclass


@dataclass
class ProcessStringKeys:
    DL_RESULT: str = "DLResult"
    LOAN_NUMBER_ID: str = "LoanNumberID"
    DATA_LANGUAGE: str = "DataLanguage"


@dataclass
class RegisterParameterSetKeys:
    PARAMETER_SET_KEY: str = "ParameterSetKey"


@dataclass
class UploadDataKeys:
    TOKEN: str = "Token"
    VALID_UNTIL: str = "ValidUntil"
