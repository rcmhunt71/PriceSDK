from dataclasses import dataclass, fields
from typing import Any, Dict, List
from base.common.models.request import BaseRequestModel


@dataclass
class GetFeatureSettingsDataPayload:
    PASSWORD_LOCKOUT_DURATION: str = "PasswordLockoutDuration"
    PASSWORD_LOCKOUT_FOREVER: str = "PasswordLockoutForever"


class GetFeatureSettingsRequest(BaseRequestModel):
    REQUEST_PAYLOAD_KEY: str = "FeatureSettings"

    def __init__(self, payload_dict, session_id, nonce, pretty_print):
        super().__init__(payload=payload_dict, session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def build_payload(self) -> Dict[str, List[Any]]:
        payload_list = []
        for payload_key in [elem.name for elem in fields(GetFeatureSettingsDataPayload)]:
            if getattr(self, payload_key.lower(), None) is not None:
                payload_list[payload_key.lower()] = getattr(self, payload_key.lower())
        payload = {self.REQUEST_PAYLOAD_KEY: payload_list}
        return payload
