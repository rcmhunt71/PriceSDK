from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class ExportLoanInfoKeys:
    LOAN_NUMBER_ID: str = "LoanNumberID"
    GENERAL_INFORMATION: str = "GeneralInformation"
    LOAN_DATES: str = "LoanDates"
    DATA_OPTIONS: str = "DataOptions"


@dataclass
class ExportLoanKeys:
    LOAN: str = "Loan"


@dataclass
class ExportLoanGeneralInformationKeys:
    LOAN_NUMBER: str = "LoanNumber"
    AGENCY_CASE_NUMBER: str = "AgencyCaseNumber"
    MERS_NUMBER: str = "MERSNumber"


@dataclass
class ExportLoanDateValues:
    DATE_NAME: str = "DateName"
    DATE_VALUE: str = "DateValue"


class ExportLoanDates(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(ExportLoanDateValues)]


class ExportLoanDatesList(BaseListResponse):
    _SUB_MODEL = ExportLoanDates


class ExportLoanGeneralInformation(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(ExportLoanGeneralInformationKeys)]


class ExportLoanList(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(ExportLoanInfoKeys)]
    _SUB_MODELS = [(ExportLoanDatesList if x is ExportLoanInfoKeys.LOAN_DATES else
                        (ExportLoanGeneralInformation if x is ExportLoanInfoKeys.GENERAL_INFORMATION else None))
                            for x in _ADD_KEYS]
