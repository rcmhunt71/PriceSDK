from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class PullQualifiedLoanScenarioProgramsInfoKeys:
    PROGRAM_NAME: str = "ProgramName"
    LOAN_TERM: str = "LoanTerm"
    FINANCE_METHOD: str = "FinanceMethod"
    FIRST_ADJUSTMENT: str = "FirstAdjustment"
    LOAN_TYPE: str = "LoanType"
    PROGRAM_ID: str = "ProgramID"
    WEB_FRIENDLY_DESCRIPTION: str = "WebFriendlyDescription"
    WEB_DISCLOSURE_NOTICE: str = "WebDisclosureNotice"
    VIIA: str = "VIIA"
    VIIB: str = "VIIB"
    VIIC: str = "VIIC"
    LOAN_SCENARIO: str = "LoanScenario"


@dataclass
class PullQualifiedLoanScenarioInfoKeys:
    RATES: str = "Rates"
    POINTS: str = "Points"
    CLOSING_COST: str = "ClosingCost"
    PAYMENT: str = "Payment"
    APR: str = "APR"
    VIIF_TOTAL: str = "VIIFTotal"
    VIIE_TOTAL: str = "VIIETotal"
    VIIH_TOTAL: str = "VIIHTotal"
    LENDER_CREDIT_TOTAL: str = "LenderCreditTotal"
    VIIE: str = "VIIE"
    VIIF: str = "VIIF"
    VIIH: str = "VIIH"
    LENDER_CREDIT: str = "LenderCredit"


@dataclass
class PullQualifiedLoanScenarioProgramsFeeKeys:
    FEE_NAME: str = "FeeName"
    FEE_AMOUNT: str = "FeeAmount"


@dataclass
class PullQualifiedLoanScenarioProgramsKeys:
    QUALIFIED_LOAN_SCENARIO_PROGRAMS: str = "QualifiedLoanScenarioPrograms"


class ProgramFee(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(PullQualifiedLoanScenarioProgramsFeeKeys)]


class ProgramFees(BaseListResponse):
    _SUB_MODEL = ProgramFee


class LoanScenario(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(PullQualifiedLoanScenarioInfoKeys)]
    _SUB_MODELS = [None if _ not in [PullQualifiedLoanScenarioInfoKeys.VIIE,
                                     PullQualifiedLoanScenarioInfoKeys.VIIF,
                                     PullQualifiedLoanScenarioInfoKeys.VIIH,
                                     PullQualifiedLoanScenarioInfoKeys.LENDER_CREDIT]
                   else ProgramFees for _ in _ADD_KEYS]


class LoanScenarios(BaseListResponse):
    _SUB_MODEL = LoanScenario


class Program(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(PullQualifiedLoanScenarioProgramsInfoKeys)]
    _SUB_MODELS = [None if _ not in [PullQualifiedLoanScenarioProgramsInfoKeys.LOAN_SCENARIO]
                   else LoanScenarios for _ in _ADD_KEYS]


class Programs(BaseListResponse):
    _SUB_MODEL = Program
