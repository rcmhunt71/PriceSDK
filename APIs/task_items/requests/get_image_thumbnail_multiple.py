from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel


@dataclass
class GetImageThumbnailMultipleRequestParams:
    LOAN_NUMBER_ID: str = "LoanNumberID"


class GetImageThumbnailMultipleRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, payload_dict, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        super().__init__(payload=payload_dict, session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetImageThumbnailMultipleRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        return args


if __name__ == '__main__':
    sample_load = {
        "Thumbnails": [
            {
                "StatusID": 529,
                "ImageIDs": [
                    {
                        "ImageID": 3,
                        "PageNumbers": [
                            {
                                "PageNumber": 1
                            }
                        ]
                    }
                ],
                "Height": 200,
                "Width": 200
            }
        ]
    }
