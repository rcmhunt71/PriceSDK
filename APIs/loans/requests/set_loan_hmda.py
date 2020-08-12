import typing
from dataclasses import dataclass

from base.common.models.request import BaseRequestModelKeys, KwargsRequestModel


@dataclass
class SetLoanHMDARequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"


@dataclass
class SetLoanHMDAPayload:
    HMDA_STATE: str = "HMDAState"
    HMDA_COUNTY: str = "HMDACounty"
    HMDA_MSA: str = "HMDAMSA"
    HMDA_CENSUS: str = "HMDACensus"
    HMDA_2018_LOAN_PURPOSE_OVERRIDE: str = "HMDA2018LoanPurposeOverride"
    HMDA_2018_DENIAL_REASON_1: str = "HMDA2018DenialReason1"
    HMDA_2018_DENIAL_REASON_2: str = "HMDA2018DenialReason2"
    HMDA_2018_DENIAL_REASON_3: str = "HMDA2018DenialReason3"
    HMDA_2018_DENIAL_REASON_4: str = "HMDA2018DenialReason4"
    HMDA_2018_DENIAL_REASON_OTHER: str = "HMDA2018DenialReasonOther"
    HMDA_2018_INTRODUCTORY_RATE_PERIOD: str = "HMDA2018IntroductoryRatePeriod"
    HMDA_2018_NMLS_ID: str = "HMDA2018NMLSID"
    HMDA_2018_AUS_DECISION: str = "HMDA2018AUSDecisison"
    HMDA_2018_AUS_DECISION_OTHER: str = "HMDA2018AUSDecisisonOther"
    HMDA_LOCK: str = "HMDALock"


class SetLoanHMDARequest(KwargsRequestModel):
    data_payload = SetLoanHMDAPayload
    REQUEST_PAYLOAD_KEY = "LoanHMDAFields"

    def __init__(self, loan_number_id, payload_dict, session_id, nonce, pretty_print, **kwargs):

        self.loan_number_id = loan_number_id
        super().__init__(session_id=session_id, nonce=nonce, payload=payload_dict, pretty_print=pretty_print, **kwargs)

    def to_params(self) -> typing.Dict[str, typing.Any]:
        args = super().to_params()
        args[SetLoanHMDARequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        return args


if __name__ == "__main__":
    import pprint
    args = {
        "hmda_2018_denial_reason_1": "This is reason #1",
        "hmda_2018_denial_reason_2": "This is reason #2",
        "hmda_2018_denial_reason_3": "This is reason #3",
        "hmda_2018_denial_reason_4": "This is reason #4",
    }

    obj = SetLoanHMDARequest(loan_number_id=986532147, payload_dict=None, session_id=123456, nonce=123245687, pretty_print=False, **args)
    print(f"PAYLOAD: {pprint.pformat(obj.payload)}")

    print("\nTesting SetLoanHMDARequest - payload_dict")
    obj_args = SetLoanHMDARequest(loan_number_id=986532147, payload_dict=obj.payload,
                                  pretty_print=False, session_id=123456, nonce=123245687)
    print(f"PAYLOAD: {pprint.pformat(obj_args.payload)}")