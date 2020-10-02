from typing import List, Dict, Any, Union
from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, KwargsRequestModel, DataKeys


@dataclass
class SetIncomesRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"


@dataclass
class SetIncomesPayload:
    CUSTOMER_ID: str = "CustomerID"
    INCOME_ID: str = "IncomeID"
    FIELDS: str = "Fields"


@dataclass
class SetIncomesFieldNames:
    INCOME_TYPE: str = "IncomeType"
    TITLE_POSITION: str = "TitlePosition"
    BASE_INCOME: str = "BaseIncome"
    OVERTIME: str = "Overtime"
    BONUSES: str = "Bonuses"
    COMMISSION: str = "Commission"
    OTHER: str = "Other"
    OTHER_DESCRIPTION: str = "OtherDescription"
    START_DATE: str = "StartDate"
    END_DATE: str = "EndDate"
    MILITARY_ENTITLEMENTS: str = "MilitaryEntitlements"
    EMPLOYER_RELATIONSHIP_INDICATOR: str = "EmployerRelationshipIndicator"


class SetIncomesRequest(KwargsRequestModel):
    data_payload = SetIncomesPayload
    REQUEST_PAYLOAD_KEY: str = "Incomes"

    def __init__(self, loan_number_id, payload_dict, session_id, nonce, pretty_print, **kwargs):
        self.loan_number_id = loan_number_id
        super().__init__(session_id=session_id, nonce=nonce, payload=payload_dict, pretty_print=pretty_print, **kwargs)

    def to_params(self) -> Dict[str, Any]:
        args = super().to_params()
        args[SetIncomesRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        return args

    def build_payload(self) -> Dict[str, List[Dict[Any, Union[List[Dict[str, Any]], Any]]]]:
        payload_dict = {}
        for payload_key in self.attr_list:
            if getattr(self, payload_key.lower(), None) is not None:
                if payload_key.title() == SetIncomesPayload.FIELDS:
                    fields_list = []
                    for key, value in getattr(self, payload_key.lower()).items():
                        fields_list.append(
                            {DataKeys.FIELD_NAME: getattr(SetIncomesFieldNames, key.upper(), key),
                            DataKeys.FIELD_VALUE: value})
                    payload_dict.update({SetIncomesPayload.FIELDS: fields_list})
                    continue
                payload_dict.update({getattr(self.data_payload, payload_key.upper(), payload_key): getattr(self, payload_key.lower())})
        return {self.REQUEST_PAYLOAD_KEY: [payload_dict]}


if __name__ == "__main__":
    import pprint
    kwargs = {
        "IncomeID": 12345,
        "CustomerID": 98765,
        "Fields": {
            SetIncomesFieldNames.INCOME_TYPE: 1,
            SetIncomesFieldNames.TITLE_POSITION: "TestQA",
            SetIncomesFieldNames.BASE_INCOME: "12500",
            SetIncomesFieldNames.OVERTIME: "1200",
            SetIncomesFieldNames.BONUSES: "500",
            SetIncomesFieldNames.COMMISSION: "300",
            SetIncomesFieldNames.OTHER: "456",
            SetIncomesFieldNames.OTHER_DESCRIPTION: "Test",
            SetIncomesFieldNames.START_DATE: "01/01/2015",
            SetIncomesFieldNames.END_DATE: "01/01/2020",
            SetIncomesFieldNames.MILITARY_ENTITLEMENTS: "2000",
            SetIncomesFieldNames.EMPLOYER_RELATIONSHIP_INDICATOR: "Y"
        }
    }
    print(f"KWARGS: {pprint.pformat(kwargs)}")

    obj = SetIncomesRequest(loan_number_id=10000001, payload_dict=None, session_id=123456, nonce=123245687, pretty_print=False, **kwargs)
    print(f"\nPAYLOAD: {pprint.pformat(obj.payload)}")

    print("\nTesting SetIncomesRequest - payload_dict")
    obj_args = SetIncomesRequest(loan_number_id=986532147, vendor_name= "test_vendor", payload_dict=obj.payload,
                                              pretty_print=False, session_id=123456, nonce=123245687)
    print(f"PAYLOAD: {pprint.pformat(obj_args.payload)}")