import os
import typing
from dataclasses import dataclass, fields

from base.common.models.request import BaseRequestModel, BaseRequestModelKeys


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


class SetLoanLicenseDataRequest(BaseRequestModel):
    def __init__(self, session_id, nonce, loan_number_id, payload_dict=None, **kwargs):

        # Kwargs are key/value pairs where a key can be a lower-case SetLoanHDMAPayload attribute
        # e.g. -  HDMA_2018_NMLS_ID -->> hdma_2018_nmls_id

        # Dynamically set all attributes based kwargs that match a SetLoanDataPayload attribute
        valid_keys = [elem.name for elem in fields(SetLoanLicenseDataParams)]
        self.attr_list = []
        is_test = os.environ.get('TEST_ENV')

        # Iterate through the kwargs
        for attr in kwargs.keys():

            # If kwargs.UPPER() matches a SetLoanHDMAPayload attribute
            # Create a model attribute and store the value.
            # Record the name of the created attribute for more efficient payload generation later in the process.

            if attr.upper() in valid_keys or is_test:
                setattr(self, attr.lower(), kwargs[attr])
                self.attr_list.append(attr.lower())

        self.loan_number_id = loan_number_id
        super().__init__(session_id=session_id, nonce=nonce, payload=payload_dict)

    def to_params(self) -> typing.Dict[str, typing.Any]:
        args = super().to_params()
        args[SetLoanLicenseDataRequestKeys.LOAN_NUMBER_ID] = self.loan_number_id

        args.update(
            dict([(getattr(SetLoanLicenseDataParams, key.upper()), getattr(self, key)) for key in self.attr_list])
        )
        return args
