import pprint
from typing import Dict, Any
from dataclasses import dataclass

from base.common.models.request import BaseRequestModelKeys, KwargsRequestModel


@dataclass
class SetAdjustmentRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"


@dataclass
class SetAdjustmentInfoKeys:
    PURCHASE_ADJUSTMENT: str = "PurchaseAdjustment"  # key
    LOCK_CONFIRM_DATA: str = "LockConfirmData"  # key
    PURCHASE_ADJUSTMENT_DATA: str = "PurchaseAdjustmentsData"  # FieldName value
    LOCK_CONFIRM_ADJ_DATA: str = "Lock_Confirm_Adj_Data"  # FieldName value


@dataclass
class SetAdjustmentFieldNames:
    COMMIT_PROGRAM_ID: str = "Commit_Program_Id"
    COMMIT_LOCK_TYPE_ID: str = "Commit_Lock_Type_ID"
    COMMIT_INVESTOR_ID: str = "CommitInvestorID"
    INVESTOR_LOAN_NUMBER: str = "Investor_Loan_Number"
    COMMITMENT_NUMBER: str = "Commitment_Number"
    POOL_NUMBER: str = "Pool_Number"
    GROSS_REVENUE: str = "Gross_Revenue"
    LOAN_COMMIT_BASE_PRICE_DOLLAR: str = "Loan_Commit_Base_Price_Dollar"
    COMMIT_BASE_PRICE: str = "Commit_Base_Price"
    LOAN_COMMIT_ADJ_TOTAL_DOLLAR_2: str = "Loan_Commit_Adj_Total_Dollar_2"
    COMMIT_ADJ_TOTAL: str = "Commit_Adj_Total"
    LOAN_COMMIT_SRP_DOLLAR: str = "Loan_Commit_SRP_Dollar"
    COMMIT_SRP: str = "Commit_SRP"
    COMMIT_SRP_ADJUSTMENT_DOLLAR: str = "CommitSRPAdjustmentDollar"
    COMMIT_SRP_ADJUSTMENT: str = "CommitSRPAdjustment"
    LOCK_EXTENSION_FEES: str = "Lock_Extension_Fees"
    LOCK_EXTENSION_FEES_PCT: str = "Lock_Extension_Fees_Pct"
    LOCK_CONFIRM_EMAILS: str = "Lock_Confirm_Emails"
    LOCK_REQUEST_BASE_PRICE: str = "Lock_Request_Base_Price"
    LOCK_REQUEST_FINAL_PRICE: str = "Lock_Request_Final_Price"
    LOCK_REQUEST_LOCK_TYPE_ID: str = "Lock_Request_Lock_Type_ID"
    LOCK_REQUEST_POINTS: str = "Lock_Request_Points"
    LOCK_REQUEST_ADJ_TOTAL: str = "Lock_Request_Adj_Total"
    LOCK_REQUEST_ADJ_REASONS: str = "Lock_Request_Adj_Reasons"
    LOCK_REQUEST_NOTES: str = "Lock_Request_Notes"
    LOAN_COMMIT_POINTS_DOLLAR: str = "Loan_Commit_Points_Dollar"
    COMMIT_POINTS: str = "Commit_Points"
    SECONDARY_GAIN_LOSS: str = "Secondary_Gain_Loss"
    PAIR_OFF: str = "Pairoff"
    PAIR_OFF_PERCENT: str = "Pairoff_Percent"
    COMMIT_NOTES: str = "CommitNotes"
    LO_COMPENSATION_DOLLARS: str = "LOCompensationDollars"
    LO_COMPENSATION_MAX_CAP_DOLLARS: str = "LOCompensationMaxCapDollars"
    LO_COMPENSATION_MIN_CAP_DOLLARS: str = "LOCompensationMinCapDollars"
    LO_COMPENSATION_NET_COMPENSATION_DOLLARS: str = "LOCompensationNetCompensationDollars"
    LO_COMPENSATION_NET_COMPENSATION_PERCENT: str = "LOCompensationNetCompensationPercent"
    LO_COMPENSATION_PERCENT: str = "LOCompensationPercent"
    LOAN_LEVEL_BASE_PRICE_WITH_LO_COMPENSATION: str = "LoanLevelBasePriceWithLOCompensation"
    LO_REQUEST_COMPENSATION_IN_PRICING: str = "LORequestCompensationInPricing"
    COMPENSATION_PAID_BY: str = "CompensationPaidBy"


class SetAdjustmentRequest(KwargsRequestModel):
    data_payload = SetAdjustmentFieldNames
    REQUEST_PAYLOAD_KEY: str = "Adjustments"

    def __init__(self, loan_number_id, payload_dict, session_id, nonce, pretty_print, **kwargs):
        self.loan_number_id = loan_number_id
        super().__init__(session_id=session_id, nonce=nonce, payload=payload_dict, pretty_print=pretty_print, **kwargs)

    def to_params(self) -> Dict[str, Any]:
        args = super().to_params()
        args[SetAdjustmentRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        return args


if __name__ == "__main__":
    lock_confirm = {"Adjustments": [{"FieldName": "Lock_Confirm_Adj_Data", "FieldValue": "",
                                     "LockConfirmData": [
                                         {"SectionData": "test", "SectionField": "id", "SectionValue": "1"}],
                                     "PurchaseAdjustment": []}]}

    purchase = {"Adjustments": [{"FieldName": "PurchaseAdjustmentsData", "FieldValue": "", "LockConfirmData": [],
                                 "PurchaseAdjustment": [
                                     {"SectionData": "test", "SectionField": "id", "SectionValue": "1"}]}]}

    kwargs = {
        "GROSS_REVENUe": 1000.1,
        "Pool_Number": 102,
        "COMMIT_investor_ID": 107
    }
    res = SetAdjustmentRequest(loan_number_id=100, payload_dict=None, session_id=1, nonce=2,
                               pretty_print=False, **kwargs)

    print(f"KWARGS: {pprint.pformat(res.payload)}")
