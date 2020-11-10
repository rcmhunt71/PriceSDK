from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse

@dataclass
class ContactGroupMemberListsInfoKeys:
    GROUP_ID: str = "GroupID"
    GROUP_NAME: str = "GroupName"
    DESCRIPTION: str = "Description"
    CONTACT_ID: str = "ContactID"
    LAST_NAME: str = "LastName"
    FIRST_NAME: str = "FirstName"
    CONTACT_TYPE: str = "ContactType"


@dataclass
class ContactGroupMemberListsKeys:
    CONTACT_GROUP_MEMBER_LIST: str = "ContactGroupMemberList"


class ContactGroupMemberList(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(ContactGroupMemberListsInfoKeys)]


class ContactGroupMemberLists(BaseListResponse):
    _SUB_MODEL = ContactGroupMemberList
