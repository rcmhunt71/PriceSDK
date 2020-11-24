from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse

@dataclass
class CompanyMembersInfoKeys:
    CONTACT_ID: str = "ContactID"
    FIRST_NAME: str = "FirstName"
    MIDDLE_NAME: str = "MiddleName"
    LAST_NAME: str = "LastName"
    EMAIL_ADDRESS: str = "EmailAddress"
    PHONE: str = "Phone"
    EXTENSION: str = "Extension"
    MOBILE: str = "Mobile"
    TITLE: str = "Title"
    NMLS_ID: str = "NMLSID"
    NMLS_ID_EXPIRATION: str = "NMLSIDExpiration"
    CONTACT_TYPE: str = "ContactType"
    PREVIOUS_CONTACT: str = "PreviousContact"
    USER_NAME: str = "UserName"
    TPO_ROLE_ID: str = "TPORoleID"
    TPO_ROLE_NAME: str = "TPORoleName"
    CONTACT_GROUPS: str = "ContactGroups"
    QUEUE_STATUS: str = "QueueStatus"


@dataclass
class CompanyMembersKeys:
    MEMBERS: str = "Members"


class CompanyMembers(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(CompanyMembersInfoKeys)]


class CompanyMembersList(BaseListResponse):
    _SUB_MODEL = CompanyMembers

