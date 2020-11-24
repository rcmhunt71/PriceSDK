from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse

@dataclass
class CompaniesInfoKeys:
    COMPANY_ID: str = "CompanyID"
    COMPANY_NAME: str = "CompanyName"
    VOICE: str = "Voice"
    ADDRESS: str = "Address"
    CITY: str = "City"
    STATE: str = "State"
    ZIP: str = "Zip"
    SUITE: str = "Suite"
    COUNTY: str = "County"
    VERIFY_ATTENTION: str = "VerifyAttention"
    FAX1: str = "Fax1"
    FAX2: str = "Fax2"
    NMLS_ID: str = "NMLSID"
    COMPANY_STATUS: str = "CompanyStatus"
    EMAIL_ADDRESS: str = "EMailAddress"
    WIRE_BANK_NAME: str = "WireBankName"
    WIRE_ABA_ROUTING_NUMBER: str = "WireABARoutingNumber"
    WIRE_ACCOUNT_NUMBER: str = "WireAccountNumber"
    WIRE_FURTHER_CREDIT_TO_BANK_NAME: str = "WireFurtherCreditToBankName"
    WIRE_FURTHER_CREDIT_TO_BANK_CITY: str = "WireFurtherCreditToBankCity"
    WIRE_FURTHER_CREDIT_TO_ABA_ROUTING_NUMBER: str = "WireFurtherCreditToABARoutingNumber"
    WIRE_FURTHER_CREDIT_TO_ACCOUNT_NUMBER: str = "WireFurtherCreditToAccountNumber"
    WIRE_FURTHER_CREDIT_TO_INSTRUCTIONS: str = "WireFurtherCreditToInstructions"
    NMLS_ID_EXPIRATION_DATE: str = "NMLSIDExpirationDate"
    COUNTRY: str = "Country"


@dataclass
class CompaniesKeys:
    COMPANIES: str = "Companies"


class Company(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(CompaniesInfoKeys)]


class Companies(BaseListResponse):
    _SUB_MODEL = Company

