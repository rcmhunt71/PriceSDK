from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse

@dataclass
class ContactInterfaceCredentialsInfoKeys:
    INTERFACE_TYPE: str = "InterfaceType"
    DATA_NAME: str = "DataName"
    DATA_NAME_CAPTION: str = "DataNameCaption"
    DATA_NAME_VALUE: str = "DataNameValue"
    IS_PASSWORD_FIELD: str = "IsPasswordField"


@dataclass
class ContactInterfaceCredentialsKeys:
    INTERFACE_CREDENTIALS: str = "InterfaceCredentials"


class ContactInterfaceCredential(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(ContactInterfaceCredentialsInfoKeys)]


class ContactInterfaceCredentials(BaseListResponse):
    _SUB_MODEL = ContactInterfaceCredential
