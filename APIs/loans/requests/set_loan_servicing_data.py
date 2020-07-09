import typing
from dataclasses import dataclass, fields

from base.common.models.request import BaseRequestModelKeys, KwargsRequestModel, DataKeys


@dataclass
class SetLoanServicingDataRequestKeys(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"


@dataclass
class SetLoanServicingDataPayload:
    LOANSERVICING_CURRENT_ESCROW_BALANCE: str = "LoanServicing_Current_Escrow_Balance"
    LOANSERVICING_CURRENT_ESCROW_PAYMENT: str = "LoanServicing_Current_Escrow_Payment"
    LOANSERVICING_CURRENT_LATE_BALANCE: str = "LoanServicing_Current_Late_Balance"
    LOANSERVICING_CURRENT_MISCELLANEOUS_FEE_BALANCE: str = "LoanServicing_Current_Miscellaneous_Fee_Balance"
    LOANSERVICING_CURRENT_MONTHLY_LOAN_PAYMENT: str = "LoanServicing_Current_Monthly_Loan_Payment"
    LOANSERVICING_CURRENT_OTHER_BALANCE: str = "LoanServicing_Current_Other_Balance"
    LOANSERVICING_CURRENT_PRINCIPAL_BALANCE: str = "LoanServicing_Current_Principal_Balance"
    LOANSERVICING_CURRENT_TOTAL_PAYMENT: str = "LoanServicing_Current_Total_Payment"
    LOANSERVICING_EXTRA_FUNDS_TO: str = "LoanServicing_Extra_Funds_To"
    LOANSERVICING_FIRST_PAYMENT_DATE: str = "LoanServicing_First_Payment_Date"
    LOANSERVICING_INITIAL_ESCROW_BALANCE: str = "LoanServicing_Initial_Escrow_Balance"
    LOANSERVICING_INITIAL_ESCROW_PAYMENT: str = "LoanServicing_Initial_Escrow_Payment"
    LOANSERVICING_INITIAL_MONTHLY_LOAN_PAYMENT: str = "LoanServicing_Initial_Monthly_Loan_Payment"
    LOANSERVICING_INITIAL_PRINCIPAL_BALANCE: str = "LoanServicing_Initial_Principal_Balance"
    LOANSERVICING_INITIAL_RATE: str = "LoanServicing_Initial_Rate"
    LOANSERVICING_INITIAL_TOTAL_PAYMENT: str = "LoanServicing_Initial_Total_Payment"
    LOANSERVICING_INTEREST_RECEIVED: str = "LoanServicing_Interest_Received"
    LOANSERVICING_LATE_RECEIVED: str = "LoanServicing_Late_Received"
    LOANSERVICING_MISCELLANEOUS_FEE_RECEIVED: str = "LoanServicing_Miscellaneous_Fee_Received"
    LOANSERVICING_NEXT_RATE: str = "LoanServicing_Next_Rate"
    LOANSERVICING_NOTES: str = "LoanServicing_Notes"
    LOANSERVICING_PREPAID_INTEREST: str = "LoanServicing_Prepaid_Interest"
    LOANSERVICING_PRINCIPAL_RECEIVED: str = "LoanServicing_Principal_Received"


class SetLoanServicingDataRequest(KwargsRequestModel):
    data_payload = SetLoanServicingDataPayload
    REQUEST_PAYLOAD_KEY: str = "LoanServicingFields"

    def __init__(self, loan_number_id, payload_dict, session_id, nonce, pretty_print, **kwargs):

        self.loan_number_id = loan_number_id
        super().__init__(session_id=session_id, nonce=nonce, payload=payload_dict, pretty_print=pretty_print, **kwargs)

    def to_params(self) -> typing.Dict[str, typing.Any]:
        args = super().to_params()
        args[SetLoanServicingDataRequestKeys.LOAN_NUMBER_ID] = self.loan_number_id
        return args


if __name__ == "__main__":
    import pprint
    args = {
        SetLoanServicingDataPayload.LOANSERVICING_CURRENT_ESCROW_BALANCE: 123456
    }

    obj = SetLoanServicingDataRequest(loan_number_id=986532147, payload_dict=None, session_id=123456, nonce=123245687, pretty_print=False, **args)
    print(f"PAYLOAD: {pprint.pformat(obj.payload)}")

    print("\nTesting SetLoanDataRequest - payload_dict")
    obj_args = SetLoanServicingDataRequest(loan_number_id=986532147, vendor_name="test_vendor", payload_dict=obj.payload,
                                              pretty_print=False, session_id=123456, nonce=123245687)
    print(f"PAYLOAD: {pprint.pformat(obj_args.payload)}")