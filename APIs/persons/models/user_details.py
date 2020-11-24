from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class UserDetailsLoginTypeKeys:
    LOGIN_TYPE: str = "LoginType"


@dataclass
class UserDetailsFannieMaeTabKeys:
    SHOW_FANNIE_MAE_TAB_ON_B2B: str = "ShowFannieMaeTabOnB2B"


# EMPLOYEE MODEL
@dataclass
class UserDetailsEmployeeInfoKeys:
    EMPLOYEE_ID: str = "EmployeeID"
    PERSON_ID: str = "PersonID"
    FIRST_NAME: str = "FirstName"
    MIDDLE_NAME: str = "MiddleName"
    LAST_NAME: str = "LastName"
    NO_LONGER_EMPLOYED: str = "NoLongerEmployed"
    LOCKOUT: str = "Lockout"
    EMPLOYEE_TYPE: str = "EmployeeType"
    EMAIL_ADDRESS: str = "EMailAddress"
    TITLE: str = "Title"
    VOICE: str = "Voice"
    CELL: str = "Cell"
    EXTENSION: str = "Extension"
    NMLS_ID: str = "NMLSID"
    LENDER_OFFICE_ID: str = "LenderOfficeID"


@dataclass
class UserDetailsEmployeeKeys:
    EMPLOYEE: str = "Employee"


class UserDetailsEmployee(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(UserDetailsEmployeeInfoKeys)]


class UserDetailsEmployeeList(BaseListResponse):
    _SUB_MODEL = UserDetailsEmployee


# CONTACT MODEL
@dataclass
class UserDetailsContactInfoKeys:
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
class UserDetailsContactKeys:
    CONTACT: str = "Contact"


class UserDetailsContact(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(UserDetailsContactInfoKeys)]


class UserDetailsContactList(BaseListResponse):
    _SUB_MODEL = UserDetailsContact


# FULL MODEL
@dataclass
class UserDetailsKeys:
    USER_DETAILS: str = "UserDetails"


class UserDetails(BaseResponse):
    _ADD_KEYS = [UserDetailsLoginTypeKeys.LOGIN_TYPE, UserDetailsEmployeeKeys.EMPLOYEE, UserDetailsContactKeys.CONTACT,
        UserDetailsFannieMaeTabKeys.SHOW_FANNIE_MAE_TAB_ON_B2B]
    _SUB_MODEL = [None, UserDetailsEmployeeList, UserDetailsContactList, None]
