from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class GetCountiesRequestParams(BaseRequestModelKeys):
    ZIP_CODE: str = "ZipCode"
    STATE: str = "State"
    COUNTY_NAME: str = "CountyName"


class GetCountiesRequest(SimpleRequestModel):
    def __init__(self, zip_code, state, county_name, session_id, nonce, pretty_print):
        self.zip_code = zip_code
        self.state = state
        self.county_name = county_name
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetCountiesRequestParams.ZIP_CODE] = self.zip_code
        args[GetCountiesRequestParams.STATE] = self.state
        args[GetCountiesRequestParams.COUNTY_NAME] = self.county_name
        return args
