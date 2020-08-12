import typing
from dataclasses import dataclass

from base.common.models.request import BaseRequestModelKeys, KwargsRequestModel, DataKeys


@dataclass
class SetLoanRateQuoteDataPayload:
    MI_QUOTE_VENDOR: str = "MIQuoteVendor"
    MI_PAYMENT_PERIOD: str = "MIPaymentPeriod"
    MGIC_RENEWAL_CALCULATION_TYPE: str = "MGICRenewalCalculationType"
    MI_ZERO_DUE_AT_CLOSING: str = "MIZeroDueAtClosing"
    MGIC_PREMIUM_REFUNDABLE_TYPE: str = "MGICPremiumRefundableType"
    COVERAGE: str = "Coverage"
    MGIC_PREMIUM_PAYMENT_TYPE: str = "MGICPremiumPaymentType"
    MI_SPECIAL_DEAL: str = "MISpecialDeal"
    RATE_QUOTE_ID: str = "RateQuoteID"
    MGIC_PREMIUM_RATE_PLAN_TYPE: str = "MGICPremiumRatePlanType"
    STATUS_DESCRIPTION: str = "StatusDescription"


@dataclass
class SetLoanRateQuoteDetailsRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    VENDOR_NAME: str = "VendorName"


class SetLoanRateQuoteDetailsRequest(KwargsRequestModel):
    data_payload = SetLoanRateQuoteDataPayload
    REQUEST_PAYLOAD_KEY: str = "LoanRateQuoteDetails"

    def __init__(self, loan_number_id, vendor_name, payload_dict, session_id, nonce, pretty_print, **kwargs):
        self.loan_number_id = loan_number_id
        self.vendor_name = vendor_name
        super().__init__(session_id=session_id, nonce=nonce, payload=payload_dict, pretty_print=pretty_print, **kwargs)

    def to_params(self) -> typing.Dict[str, typing.Any]:
        args = super().to_params()
        args.update({
            SetLoanRateQuoteDetailsRequestParams.LOAN_NUMBER_ID: self.loan_number_id,
            SetLoanRateQuoteDetailsRequestParams.VENDOR_NAME: self.vendor_name
        })
        return args


if __name__ == "__main__":
    import pprint

    args = {
        "coverage": "This is coverage --> here",
        "rate_quote_id": 34537349857,
        "status_description": "This is the status_description",
    }

    def _build_payload(data_dict):
        primary_key = SetLoanRateQuoteDetailsRequest.REQUEST_PAYLOAD_KEY
        payload_list = [{DataKeys.FIELD_NAME: key,
                         DataKeys.FIELD_VALUE: value} for key, value in args.items()]
        return {primary_key: payload_list}

    print("Testing SetLoanRateQuoteDetailsRequest - payload_dict()")
    obj_payload = SetLoanRateQuoteDetailsRequest(loan_number_id=986532147, vendor_name="test_vendor", payload_dict=_build_payload(args),
                                                 pretty_print=False, session_id=123456, nonce=123245687)
    print(f"PAYLOAD: {pprint.pformat(obj_payload.payload)}")

    print("Testing SetLoanRateQuoteDetailsRequest - kwargs")
    obj_args = SetLoanRateQuoteDetailsRequest(loan_number_id=986532147, vendor_name="test_vendor", payload_dict=None,
                                              pretty_print=False, session_id=123456, nonce=123245687, **args)
    print(f"PAYLOAD: {pprint.pformat(obj_args.payload)}")
