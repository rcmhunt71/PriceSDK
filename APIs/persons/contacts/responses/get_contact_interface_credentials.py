from APIs.persons.contacts.models.contact_interface_credentials import ContactInterfaceCredentials, ContactInterfaceCredentialsKeys
from base.common.response import CommonResponse


class GetContactInterfaceCredentialsResponse(CommonResponse):
    _ADD_KEYS = [ContactInterfaceCredentialsKeys.INTERFACE_CREDENTIALS]
    _SUB_MODELS = [ContactInterfaceCredentials]
