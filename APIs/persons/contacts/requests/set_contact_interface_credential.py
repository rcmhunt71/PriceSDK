from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class SetContactInterfaceCredentialRequestParams(BaseRequestModelKeys):
    COMPANY_ID: str = "CompanyID"
    CONTACT_ID: str = "ContactID"
    INTERFACE_TYPE: str = "InterfaceType"
    INTERFACE_DATA_NAME: str = "InterfaceDataName"
    INTERFACE_PASSWORD: str = "InterfacePassword"


class SetContactInterfaceCredentialRequest(SimpleRequestModel):
    def __init__(self, company_id, contact_id, interface_type, interface_data_name, interface_password,
            session_id, nonce, pretty_print):
        self.company_id = company_id
        self.contact_id = contact_id
        self.interface_type = interface_type
        self.interface_data_name = interface_data_name
        self.interface_password = interface_password
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[SetContactInterfaceCredentialRequestParams.COMPANY_ID] = self.company_id
        args[SetContactInterfaceCredentialRequestParams.CONTACT_ID] = self.contact_id
        args[SetContactInterfaceCredentialRequestParams.INTERFACE_TYPE] = self.interface_type
        args[SetContactInterfaceCredentialRequestParams.INTERFACE_DATA_NAME] = self.interface_data_name
        args[SetContactInterfaceCredentialRequestParams.INTERFACE_PASSWORD] = self.interface_password
        return args
