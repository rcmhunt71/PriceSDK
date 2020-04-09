from dataclasses import dataclass


@dataclass
class ProcessStringKeys:
    DL_RESULT: str = "DLResult"
    LOAN_NUMBER_IDS: str = "LoanNumberID"
    DATA_LANGUAGE: str = "DataLanguage"
