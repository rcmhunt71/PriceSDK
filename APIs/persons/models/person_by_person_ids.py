from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class PersonByPersonIDsInfoKeys:
    PERSON_ID: str = "PersonID"
    SPOUSE_ID: str = "SpouseID"
    PRESENT_ADDRESS_ID: str = "PresentAddressID"
    LAST_NAME: str = "LastName"
    FIRST_NAME: str = "FirstName"
    MIDDLE_NAME: str = "MiddleName"
    GENERATION: str = "Generation"
    SOCIAL_SECURITY_NUMBER: str = "SocialSecurityNumber"
    TITLE: str = "Title"
    VOICE: str = "Voice"
    WORK_NUMBER: str = "WorkNumber"
    FAX: str = "Fax"
    PAGER: str = "Pager"
    CELL: str = "Cell"
    DATA: str = "Data"
    BIRTHDATE: str = "Birthdate"
    EMAIL_ADDRESS: str = "EmailAddress"
    PERSON_INITIAL: str = "PersonInitial"
    WORK_EXTENSION: str = "WorkExtension"
    EMAIL_NAME: str = "EMailName"


@dataclass
class PersonByPersonIDsKeys:
    PERSONS: str = "Persons"


class PersonByPersonIDs(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(PersonByPersonIDsInfoKeys)]


class PersonByPersonIDsList(BaseListResponse):
    _SUB_MODEL = PersonByPersonIDs
