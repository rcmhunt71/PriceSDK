from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class DownloadVisionetDocumentRequestParams(BaseRequestModelKeys):
    JOB_ID: str = "JobID"
    APP_ID: str = "AppID"
    APP_SECRET: str = "AppSecret"


class DownloadVisionetDocumentRequest(SimpleRequestModel):
    def __init__(self, job_id, app_id, app_secret, session_id, nonce, pretty_print):
        self.job_id = job_id
        self.app_id = app_id
        self.app_secret = app_secret
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[DownloadVisionetDocumentRequestParams.JOB_ID] = self.job_id
        args[DownloadVisionetDocumentRequestParams.APP_ID] = self.app_id
        args[DownloadVisionetDocumentRequestParams.APP_SECRET] = self.app_secret
        return args
