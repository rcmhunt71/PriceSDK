from dataclasses import dataclass
from base.common.models.request import KwargsRequestModel


@dataclass
class GetFeatureSettingsFieldNames:
    pass


class GetFeatureSettingsRequest(KwargsRequestModel):
    data_payload = GetFeatureSettingsFieldNames
    REQUEST_PAYLOAD_KEY: str = "FeatureSettings"

    def __init__(self, payload_dict, session_id, nonce, pretty_print, **kwargs):
        super().__init__(payload=payload_dict, session_id=session_id, nonce=nonce, pretty_print=pretty_print, **kwargs)
