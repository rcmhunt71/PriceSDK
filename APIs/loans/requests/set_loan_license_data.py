import typing
from dataclasses import dataclass
from enum import Enum

from base.common.models.request import BaseRequestModelKeys, KwargsRequestModel


@dataclass
class SetLoanLicenseDetailsRequestParams:
    DATA_FROM: str = "DataFrom"
    LICENSE_ID: str = "LicenseID"
    LICENSE_NAME: str = "LicenseName"
    LICENSE_NUMBER: str = "LicenseNumber"
    LICENSE_EXPIRATION_DATE: str = "LicenseExpirationDate"
    LICENSE_TYPE: str = "LicenseType"
    LICENSE_STATE: str = "LicenseState"


@dataclass
class SetLoanLicenseDataRequestKeys(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"


class LoanLicenseType(Enum):
    BLANK = 0  # Will not set/update value
    REMOVE_VALUE = 1  # Remove whatever value was before
    GENERAL = 2
    FHA = 3
    VA = 4
    GENERAL_FHA_VA = 5
    GENERAL_FHA = 6
    GENERAL_VA = 7
    FHA_VA = 8


class SetLoanLicenseDataRequest(KwargsRequestModel):
    data_payload = SetLoanLicenseDetailsRequestParams
    REQUEST_PAYLOAD_KEY = None

    def __init__(self, loan_number_id, session_id, nonce, pretty_print, **kwargs):
        """ This request does not rely on json payload, only URL parameters are used """
        self.loan_number_id = loan_number_id
        super().__init__(session_id=session_id, nonce=nonce, payload=None, pretty_print=pretty_print, **kwargs)

    def to_params(self) -> typing.Dict[str, typing.Any]:
        args = super().to_params()
        args[SetLoanLicenseDataRequestKeys.LOAN_NUMBER_ID] = self.loan_number_id

        args.update(
            dict(
                [(getattr(SetLoanLicenseDetailsRequestParams, key.upper()), getattr(self, key.lower()))
                 for key in self.attr_list]
            )
        )

        return args

    def build_payload(self) -> typing.Dict[str, typing.List[typing.Dict[str, typing.Any]]]:
        # When no kwargs, request body should be None in order to send headers "Content-Length": 0
        if not len(self.attr_list):
            return None
        else:
            super().build_payload()


if __name__ == "__main__":
    import pprint
    args = {
        "data_from": "This is data from",
        "license_id": "This is license id",
    }

    obj = SetLoanLicenseDataRequest(loan_number_id=986532147, session_id=123456, nonce=123245687, pretty_print=False, **args)
    print(f"PARAMS: {pprint.pformat(obj.to_params())}")