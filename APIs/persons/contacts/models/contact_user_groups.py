from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse

@dataclass
class ContactUserGroupInfoKeys:
    GROUP_ID: str = "GroupID"
    GROUP_NAME: str = "GroupName"


@dataclass
class ContactUserGroupsKeys:
    CONTACT_USER_GROUPS: str = "ContactUserGroups"


class ContactUserGroup(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(ContactUserGroupInfoKeys)]


class ContactUserGroups(BaseListResponse):
    _SUB_MODEL = ContactUserGroup
