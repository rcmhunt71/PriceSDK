from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse

@dataclass
class ContactsInfoKeys:
    CONTACT_ID: str = "ContactID"
    PERSON_ID: str = "PersonID"
    COMPANY_ID: str = "CompanyID"
    COMPANY_NAME: str = "CompanyName"
    COMPANY_STATUS: str = "CompanyStatus"
    COMPANY_CITY: str = "CompanyCity"
    COMPANY_STATE: str = "CompanyState"
    LOGIN_NAME: str = "LoginName"
    FIRST_NAME: str = "FirstName"
    MIDDLE_NAME: str = "MiddleName"
    LAST_NAME: str = "LastName"
    NO_LONGER_EMPLOYED: str = "NoLongerEmployed"
    LOCKOUT: str = "Lockout"
    CONTACT_TYPE: str = "ContactType"
    EMAIL_ADDRESS: str = "EMailAddress"
    TITLE: str = "Title"
    VOICE: str = "Voice"
    CELL: str = "Cell"
    EXTENSION: str = "Extension"
    NMLS_ID: str = "NMLSID"
    DESIGNATION: str = "Designation"
    LICENSE_NUMBER: str = "LicenseNumber"
    FAX: str = "Fax"
    NOTIFICATION_EMAILS: str = "NotificationEmails"
    CONTACT_SECURITY_LEVEL: str = "ContactSecurityLevel"
    PRINT_FORM_CATEGORY: str = "PrintFormCategory"
    INTERNAL_CONTACT: str = "InternalContact"
    NMLS_ID_EXPIRATION_DATE: str = "NMLSIDExpirationDate"


@dataclass
class ContactsKeys:
    CONTACTS: str = "Contacts"


class Contact(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(ContactsInfoKeys)]


class Contacts(BaseListResponse):
    _SUB_MODEL = Contact
