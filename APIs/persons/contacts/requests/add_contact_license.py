from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class AddContactLicenseParams(BaseRequestModelKeys):
    CONTACT_ID: str = "ContactID"
    LICENSE_NAME: str = "LicenseName"
    LICENSE_NUMBER: str = "LicenseNumber"
    LICENSE_START_DATE: str = "LicenseStartDate"
    LICENSE_END_DATE: str = "LicenseEndDate"
    LICENSE_STATE: str = "LicenseState"
    STATE_DEFAULT: str = "StateDefault"
    LIEN_POSITION: str = "LienPosition"
    LICENSE_TYPE: str = "LicenseType"


class AddContactLicenseRequest(SimpleRequestModel):
    def __init__(self, contact_id, license_name, license_number, license_start_date, license_end_date, license_state,
            state_default, lien_position, license_type, session_id, nonce, pretty_print):
        self.contact_id = contact_id
        self.license_name = license_name
        self.license_number = license_number
        self.license_start_date = license_start_date
        self.license_end_date = license_end_date
        self.license_state = license_state
        self.state_default = state_default
        self.lien_position = lien_position
        self.license_type = license_type
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[AddContactLicenseParams.CONTACT_ID] = self.contact_id
        args[AddContactLicenseParams.LICENSE_NAME] = self.license_name
        args[AddContactLicenseParams.LICENSE_NUMBER] = self.license_number
        args[AddContactLicenseParams.LICENSE_START_DATE] = self.license_start_date
        args[AddContactLicenseParams.LICENSE_END_DATE] = self.license_end_date
        args[AddContactLicenseParams.LICENSE_STATE] = self.license_state
        args[AddContactLicenseParams.STATE_DEFAULT] = self.state_default
        args[AddContactLicenseParams.LIEN_POSITION] = self.lien_position
        args[AddContactLicenseParams.LICENSE_TYPE] = self.license_type
        return args
