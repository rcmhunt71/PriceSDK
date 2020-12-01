from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class PullQualifiedLoanProgramsInfoKeys:
    PROGRAM_NAME: str = "ProgramName"
    LOAN_TERM: str = "LoanTerm"
    FINANCE_METHOD: str = "FinanceMethod"
    FIRST_ADJUSTMENT: str = "FirstAdjustment"
    LOAN_TYPE: str = "LoanType"
    RATES: str = "Rates"
    POINTS: str = "Points"
    CLOSING_COST: str = "ClosingCost"
    PAYMENT: str = "Payment"
    APR: str = "APR"
    PROGRAM_ID: str = "ProgramID"
    WEB_FRIENDLY_DESCRIPTION: str = "WebFriendlyDescription"
    WEB_IMPORTANT_NOTICES: str = "WebImportantNotices"
    WEB_DISCLOSURE_NOTICE: str = "WebDisclosureNotice"
    VIIA: str = "VIIA"
    VIIB: str = "VIIB"
    VIIC: str = "VIIC"
    VIIF: str = "VIIF"


@dataclass
class PullQualifiedLoanProgramsFeeKeys:
    FEE_NAME: str = "FeeName"
    FEE_AMOUNT: str = "FeeAmount"


@dataclass
class PullQualifiedLoanProgramsKeys:
    QUALIFIED_LOAN_PROGRAMS: str = "QualifiedLoanPrograms"


class ProgramFee(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(PullQualifiedLoanProgramsFeeKeys)]


class ProgramFees(BaseListResponse):
    _SUB_MODEL = ProgramFee


class Program(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(PullQualifiedLoanProgramsInfoKeys)]
    _SUB_MODELS = [None if _ is not PullQualifiedLoanProgramsInfoKeys.VIIF else ProgramFees for _ in _ADD_KEYS]


class Programs(BaseListResponse):
    _SUB_MODEL = Program
