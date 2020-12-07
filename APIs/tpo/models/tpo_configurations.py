from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class ContactGroupsInfoKeys:
    GROUP_ID: str = "GroupID"
    GROUP_NAME: str = "GroupName"
    GROUP_DESCRIPTION: str = "GroupDescription"


@dataclass
class CompanyTPOAdminsInfoKeys:
    CONTACT_ID: str = "ContactID"
    CAN_ADD: str = "CanAdd"
    CAN_EDIT: str = "CanEdit"
    CAN_DEACTIVATE: str = "CanDeactivate"


@dataclass
class TPOConfigurationsKeys:
    CONTACT_GROUPS: str = "ContactGroups"
    COMPANY_TPO_ADMINS: str = "CompanyTPOAdmins"


class ContactGroups(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(ContactGroupsInfoKeys)]


class ContactGroupsList(BaseListResponse):
    _SUB_MODEL = ContactGroups


class CompanyTPOAdmins(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(CompanyTPOAdminsInfoKeys)]


class CompanyTPOAdminsList(BaseListResponse):
    _SUB_MODEL = ContactGroups
