from dataclasses import dataclass
from typing import List, Dict, Any
from base.common.models.request import BaseRequestModelKeys, KwargsRequestModel, DataKeys


@dataclass
class SetTPOApprovalQueueDataRequestParams(BaseRequestModelKeys):
    COMPANY_ID: str = "CompanyID"
    CONTACT_ID: str = "ContactID"
    EDITED_BY_ID: str = "EditedByID"
    ACTION_FLAG: str = "ActionFlag"
    MAC_ADDRESS: str = "MacAddress"
    RESET_LINK: str = "ResetLink"


@dataclass
class SetTPOApprovalQueueDataFieldNames:
    FIRST_NAME: str = "FirstName"
    MIDDLE_NAME: str = "MiddleName"
    LAST_NAME: str = "LastName"
    EMAIL_ADDRESS: str = "EmailAddress"
    MOBILE: str = "Mobile"
    PHONE: str = "Phone"
    EXTENSION: str = "Extension"
    TITLE: str = "Title"
    NMLS_ID: str = "NMLSID"
    USER_NAME: str = "UserName"
    PREVIOUS_CONTACT: str = "PreviousContact"
    CONTACT_TYPE: str = "ContactType"
    NMLS_ID_EXPIRATION: str = "NMLSIDExpiration"
    GROUPS: str = "Groups"


class SetTPOApprovalQueueDataRequest(KwargsRequestModel):
    data_payload = SetTPOApprovalQueueDataFieldNames
    REQUEST_PAYLOAD_KEY: str = "TPOApprovalQueues"

    def __init__(self, company_id, contact_id, edited_by_id, action_flag, mac_address, reset_link, payload_dict,
            session_id, nonce, pretty_print, **kwargs):
        self.company_id = company_id
        self.contact_id = contact_id
        self.edited_by_id = edited_by_id
        self.action_flag = action_flag
        self.mac_address = mac_address
        self.reset_link = reset_link
        super().__init__(payload=payload_dict, session_id=session_id, nonce=nonce, pretty_print=pretty_print, **kwargs)

    def to_params(self):
        args = super().to_params()
        args[SetTPOApprovalQueueDataRequestParams.COMPANY_ID] = self.company_id
        args[SetTPOApprovalQueueDataRequestParams.CONTACT_ID] = self.contact_id
        args[SetTPOApprovalQueueDataRequestParams.EDITED_BY_ID] = self.edited_by_id
        args[SetTPOApprovalQueueDataRequestParams.ACTION_FLAG] = self.action_flag
        args[SetTPOApprovalQueueDataRequestParams.MAC_ADDRESS] = self.mac_address
        args[SetTPOApprovalQueueDataRequestParams.RESET_LINK] = self.reset_link
        return args

    def build_payload(self) -> Dict[str, List[Dict[str, Any]]]:
        payload_list = []
        for payload_key in self.attr_list:
            if getattr(self, payload_key.lower(), None) is not None:
                payload_list.append(
                    {DataKeys.FIELD_NAME: getattr(self.data_payload, payload_key.upper(), payload_key),
                     "FieldNewValue": getattr(self, payload_key.lower())})
        payload = {self.REQUEST_PAYLOAD_KEY: payload_list}
        return payload
