from APIs.persons.contacts.models.contact_user_groups import ContactUserGroupsKeys, ContactUserGroups
from base.common.response import CommonResponse


class GetContactUserGroupsResponse(CommonResponse):
    _ADD_KEYS = [ContactUserGroupsKeys.CONTACT_USER_GROUPS]
    _SUB_MODELS = [ContactUserGroups]
