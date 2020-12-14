from dataclasses import dataclass


@dataclass
class GetVerificationDataKeys:
    VERIFICATION_OUTCOME: str = "VerificationOutcome"
    VERIFICATION_DATE: str = "VerificationDate"
