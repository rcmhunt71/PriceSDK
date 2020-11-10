from APIs.persons.contacts.models.contact import ContactsKeys, Contacts
from base.common.response import CommonResponse


class GetContactsResponse(CommonResponse):
    _ADD_KEYS = [ContactsKeys.CONTACTS]
    _SUB_MODELS = [Contacts]
