from dataclasses import dataclass

from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class GetPropertiesRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberId"


class GetPropertiesRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetPropertiesRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        return args


class GetPropertyLiensRequest(GetPropertiesRequest):
    pass

class IsPresentAddressAndSubjectPropertyLinkedRequest(GetPropertiesRequest):
    pass



if __name__ == "__main__":
    import pprint

    obj = GetPropertiesRequest(loan_number_id=10000001, session_id=123456, nonce=123245687, pretty_print=False)
    print(f"\nPARAMS: {pprint.pformat(obj.as_json)}")