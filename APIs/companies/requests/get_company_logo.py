from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class GetCompanyLogoParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoannumberID"
    HEIGHT: str = "Height"
    WIDTH: str = "Width"


class GetCompanyLogoRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, height, width, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.height = height
        self.width = width
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetCompanyLogoParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[GetCompanyLogoParams.HEIGHT] = self.height
        args[GetCompanyLogoParams.WIDTH] = self.width
        return args
