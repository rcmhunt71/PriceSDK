from dataclasses import dataclass, fields
from base.responses.base_response import BaseListResponse, BaseResponse


@dataclass
class BorrowersInfoKeys:
    PERSON_ID: str = "PersonID"
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
    DOCUMENT_PASSWORD: str = "DocumentPassword"
    PERSON_INITIAL: str = "PersonInitial"
    WORK_EXTENSION: str = "WorkExtension"
    EMAIL_NAME: str = "EMailName"
    MEMBER_NUMBER: str = "MemberNumber"


@dataclass
class BorrowersKeys:
    BORROWER_DETAIL: str = "BorrowerDetail"


class Borrower(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(BorrowersInfoKeys)]


class Borrowers(BaseListResponse):
    _SUB_MODEL = Borrower

