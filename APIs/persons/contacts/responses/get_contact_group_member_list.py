from APIs.persons.contacts.models.contact_group_member_list import ContactGroupMemberLists, ContactGroupMemberListsKeys
from base.common.response import CommonResponse


class GetContactGroupMemberListResponse(CommonResponse):
    _ADD_KEYS = [ContactGroupMemberListsKeys.CONTACT_GROUP_MEMBER_LIST]
    _SUB_MODELS = [ContactGroupMemberLists]
