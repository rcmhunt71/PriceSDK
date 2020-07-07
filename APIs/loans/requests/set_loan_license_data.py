import os
import typing
from dataclasses import dataclass

from base.common.models.request import BaseRequestModelKeys, KwargsRequestModel


@dataclass
class SetLoanLicenseDataParams:
    DATA_FROM: str = "DataFrom"
    LICENSE_ID: str = "LicenseID"
    LICENSE_NAME: str = "LicenseName"
    LICENSE_NUMBER: str = "LicenseNumber"
    LICENSE_EXPIRATION_DATA: str = "LicenseExpirationDate"
    LICENSE_TYPE: str = "LicenseType"
    LICENSE_STATE: str = "LicenseState"


@dataclass
class SetLoanLicenseDataRequestKeys(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"


class SetLoanLicenseDataRequest(KwargsRequestModel):
    def __init__(self, loan_number_id, session_id, nonce, pretty_print, **kwargs):
        '''
        This request does not rely on json payload, only URL parameters are used
        '''
        self.data_payload = SetLoanLicenseDataParams

        self.loan_number_id = loan_number_id
        super().__init__(session_id=session_id, nonce=nonce, payload=None, pretty_print=pretty_print, **kwargs)

    def to_params(self) -> typing.Dict[str, typing.Any]:
        args = super().to_params()
        args[SetLoanLicenseDataRequestKeys.LOAN_NUMBER_ID] = self.loan_number_id

        args.update(
            dict([(getattr(SetLoanLicenseDataParams, key.upper()), getattr(self, key)) for key in self.attr_list])
        )
        return args

    def build_payload(self):
        return {}