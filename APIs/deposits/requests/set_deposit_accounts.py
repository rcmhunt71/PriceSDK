import pprint
from dataclasses import dataclass
from typing import Dict, List, Any, Union

from base.common.models.request import KwargsRequestModel, DataKeys, BaseRequestModelKeys


@dataclass
class SetDepositAccountsRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"


@dataclass
class SetDepositAccountsPayload:
    CUSTOMER_ID: str = "CustomerID"
    DEPOSIT_ID: str = "DepositID"
    DEPOSIT_ACCOUNT_ID: str = "DepositAccountID"
    FIELDS: str = "Fields"


@dataclass
class SetDepositAccountsFieldNames:
    ACCOUNT_TYPE: str = "Account_Type"
    ACCOUNT_NUMBER: str = "Account_Number"
    ACCOUNT_NAME: str = "Account_Name"
    BALANCE: str = "Balance"
    GIFT_DEPOSITED: str = "GiftDeposited"
    GIFT_SOURCE: str = "GiftSource"
    GIFT_DEPOSITED_AMOUNT: str = "GiftDepositedAmount"


class SetDepositAccountsRequest(KwargsRequestModel):
    data_payload = SetDepositAccountsPayload
    REQUEST_PAYLOAD_KEY = "DepositAccounts"

    def __init__(self, loan_number_id, payload_dict, session_id, nonce, pretty_print, **kwargs):

        self.loan_number_id = loan_number_id
        super().__init__(session_id=session_id, nonce=nonce, payload=payload_dict, pretty_print=pretty_print, **kwargs)

    def to_params(self) -> Dict[str, Any]:
        args = super().to_params()
        args[SetDepositAccountsRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        return args

    def build_payload(self) -> Dict[str, List[Dict[Any, Union[List[Dict[str, Any]], Any]]]]:
        payload_dict = {}

        for payload_key in self.attr_list:
            if getattr(self, payload_key.lower(), None) is not None:

                if payload_key.title() == SetDepositAccountsPayload.FIELDS:
                    fields_list = []
                    for key, value in getattr(self, payload_key.lower()).items():
                        fields_list.append(
                            {DataKeys.FIELD_NAME: getattr(SetDepositAccountsFieldNames, key.upper(), key),
                             DataKeys.FIELD_VALUE: value})
                    payload_dict.update({SetDepositAccountsPayload.FIELDS: fields_list})
                    continue

                payload_dict.update(
                    {getattr(self.data_payload, payload_key.upper(), payload_key): getattr(self, payload_key.lower())})

        return {self.REQUEST_PAYLOAD_KEY: [payload_dict]}


if __name__ == "__main__":

    body = {"DepositAccounts": [
        {
            "CustomerID": 11157144,
            "DepositID": 3,
            "DepositAccountID": 1,
            "Fields": [
                {
                    "FieldName": "Account_Type",
                    "FieldValue": "Savings"
                }, {
                    "FieldName": "Account_Name",
                    "FieldValue": "John Homeowner123"
                }
            ]
         }
    ]
    }

    kwargs = {
        "customer_iD": 11157144, "DEPosit_ID": 3, "Deposit_Account_id": 1, "fields": {
            "Account_Type": "Savings", "Account_Name": "John Homeowner123"
        }
    }

    a = SetDepositAccountsRequest(loan_number_id=1111, payload_dict=None, session_id=1, nonce=1,
                                  pretty_print=None, **kwargs)
    print(f"\nPAYLOAD: {pprint.pformat(a.payload)}")
