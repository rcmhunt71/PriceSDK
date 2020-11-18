from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class AddContactParams(BaseRequestModelKeys):
    CONTACT_TYPE: str = "ContactType"
    FIELD_NAME: str = "FieldName"
    FIELD_VALUE: str = "FieldValue"


class AddContactRequest(SimpleRequestModel):
    def __init__(self, contact_type, field_name, field_value, session_id, nonce, pretty_print):
        self.contact_type = contact_type
        self.field_name = field_name
        self.field_value = field_value
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[AddContactParams.CONTACT_TYPE] = self.contact_type
        args[AddContactParams.FIELD_NAME] = self.field_name
        args[AddContactParams.FIELD_VALUE] = self.field_value
        return args
