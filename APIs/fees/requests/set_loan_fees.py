import pprint
from dataclasses import dataclass
from typing import Dict, List, Any, Union

from base.common.models.request import BaseRequestModelKeys, KwargsRequestModel, DataKeys


@dataclass
class SetLoanFeesRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"


@dataclass
class SetLoanFeesPayload:
    LOAN_FEE_ID: str = "LoanFeeID"
    FIELDS: str = "Fields"


@dataclass
class SetLoanFeesFieldNames:
    TOTAL: str = "Total"
    POC: str = "POC"
    POINTS_PERCENT: str = "Points_Percent"
    IMPOUNDS: str = "Impounds"
    SHOW_ON_HUD: str = "Show_On_HUD"
    AMOUNT_PER_YEAR: str = "Amount_Per_Year"
    MONTHS: str = "Months"
    AMOUNT: str = "Amount"
    DAYS: str = "Days"
    MEMO: str = "Memo"
    CAN_SHOP: str = "CanShop"
    FEE_PAID_TO_AN_AFFILIATE: str = "FeePaidToAnAffiliate"
    BORROWER_SELECTED_SERVICE_PROVIDER: str = "BorrowerSelectedServiceProvider"
    PAID_TO: str = "Paid_To"
    PAID_BY: str = "Paid_By"
    PAID_BY_OTHER: str = "Paid_By_Other"
    PAID_TO_OTHER: str = "Paid_To_Other"
    FEE_NAME: str = "Fee_Name"


class SetLoanFeesRequest(KwargsRequestModel):
    data_payload = SetLoanFeesPayload
    REQUEST_PAYLOAD_KEY: str = "LoanFees"

    def __init__(self, loan_number_id, payload_dict, session_id, nonce, pretty_print, **kwargs):

        self.loan_number_id = loan_number_id
        super().__init__(session_id=session_id, nonce=nonce, payload=payload_dict, pretty_print=pretty_print, **kwargs)

    def to_params(self) -> Dict[str, Any]:
        args = super().to_params()
        args[SetLoanFeesRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        return args

    def build_payload(self) -> Dict[str, List[Dict[Any, Union[List[Dict[str, Any]], Any]]]]:
        payload_dict = {}

        for payload_key in self.attr_list:
            if getattr(self, payload_key.lower(), None) is not None:

                if payload_key.title() == SetLoanFeesPayload.FIELDS:
                    fields_list = []
                    for key, value in getattr(self, payload_key.lower()).items():
                        fields_list.append(
                            {DataKeys.FIELD_NAME: getattr(SetLoanFeesFieldNames, key.upper(), key),
                             DataKeys.FIELD_VALUE: value})
                    payload_dict.update({SetLoanFeesPayload.FIELDS: fields_list})
                    continue

                payload_dict.update(
                    {getattr(self.data_payload, payload_key.upper(), payload_key): getattr(self, payload_key.lower())})

        return {self.REQUEST_PAYLOAD_KEY: [payload_dict]}


if __name__ == "__main__":
    body = {
        "LoanFees":
            [
                {
                    "LoanFeeID": 108,
                    "Fields":
                        [
                            {
                                "FieldName": "Total",
                                "FieldValue": "75"
                            },
                            {
                                "FieldName": "FeePaidToAnAffiliate",
                                "FieldValue": "0"
                            }
                        ]
                },
                {
                    "LoanFeeID": 89,
                    "Fields":
                        [
                            {
                                "FieldName": "Impounds",
                                "FieldValue": "1"
                            },
                            {
                                "FieldName": "Total",
                                "FieldValue": "56"
                            }
                        ]
                }
            ]
    }

    kwargs = {"Loan_FEE_id": 108, "fields": {"FEE_Paid_to_AN_Affiliate": "0", "TOTAL": "75"}}

    a = SetLoanFeesRequest(loan_number_id=1111, payload_dict=None, session_id=1, nonce=1,
                           pretty_print=None)
    print(f"\nPAYLOAD: {pprint.pformat(a.payload)}")
