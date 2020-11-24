from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class SetCompanyLicenseTypeParams(BaseRequestModelKeys):
    COMPANY_ID: str = "CompanyID"
    LICENSE_NUMBER: str = "LicenseNumber"
    COMPANY_TYPE: str = "CompanyType"


class SetCompanyLicenseTypeRequest(SimpleRequestModel):
    def __init__(self, company_id, license_number, company_type, session_id, nonce, pretty_print):
        self.company_id = company_id
        self.license_number = license_number
        self.company_type = company_type
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[SetCompanyLicenseTypeParams.COMPANY_ID] = self.company_id
        args[SetCompanyLicenseTypeParams.LICENSE_NUMBER] = self.license_number
        args[SetCompanyLicenseTypeParams.COMPANY_TYPE] = self.company_type
        return args
