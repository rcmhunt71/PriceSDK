import pprint
from dataclasses import dataclass

from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class PutVirtualDataRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    VIRTUAL_DATA: str = "VirtualData-"


class PutVirtualDataRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, auto_append, session_id, nonce, pretty_print, **kwargs):
        self.loan_number_id = loan_number_id
        self.auto_append = auto_append
        self.kwargs = kwargs
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[PutVirtualDataRequestParams.LOAN_NUMBER_ID] = self.loan_number_id

        for key, value in self.kwargs.items():
            if not key.lower().startswith(PutVirtualDataRequestParams.VIRTUAL_DATA.lower()) and self.auto_append:
                args[PutVirtualDataRequestParams.VIRTUAL_DATA + key] = value
            else:
                args[key] = value
        return args


if __name__ == "__main__":

    # TURNED ON
    data = {"test1": 11, "VirtualData-test2": 22, "virtualdata-test3": 33, "aVirtualData-test3": 44}
    data_after = {"VirtualData-test1": 11, "VirtualData-test2": 22, "virtualdata-test3": 33,
                  "VirtualData-aVirtualData-test3": 44}
    res = PutVirtualDataRequest(loan_number_id=0, auto_append=True, session_id=1, nonce=1, pretty_print=None, **data)
    print(f"\nPAYLOAD [ON]: {pprint.pformat(res.as_params_dict)}")
    assert data_after.items() <= res.as_params_dict.items(), "expected dict() is not in actual dict()"

    # TURNED OFF
    load = {"parameter": 55, "VirtualData-value": 66, "virtualdata-key": 77, "_VirtualData-attr": 88}
    response = PutVirtualDataRequest(loan_number_id=0, auto_append=False, session_id=1, nonce=1,
                                     pretty_print=None, **load)
    print(f"\nPAYLOAD [OFF]: {pprint.pformat(response.as_params_dict)}")
    assert load.items() <= response.as_params_dict.items(), "expected dict() is not in actual dict()"
