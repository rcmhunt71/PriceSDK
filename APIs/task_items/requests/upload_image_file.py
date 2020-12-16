from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel


@dataclass
class UploadImageFileRequestParams:
    LOAN_NUMBER_ID: str = "LoanNumberID"
    STATUS_ID: str = "StatusID"
    MIME_SUB_TYPE: str = "MIMESubType"
    IMAGE_FILE: str = "ImageFile"
    SEND_EMAIL_NOTIFICATION: str = "SendEmailNotification"
    B2B_FLAG: str = "B2BFlag"
    IMAGE_TOKEN: str = "ImageToken"
    HASH: str = "Hash"
    PORTAL: str = "Portal"
    CONTACT_NAME: str = "ContactName"


class UploadImageFileRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, status_id, mime_sub_type, image_file, send_email_notification,
                 b2b_flag, image_token, hash, portal, contact_name, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.status_id = status_id
        self.mime_sub_type = mime_sub_type
        self.image_file = image_file
        self.send_email_notification = send_email_notification
        self.b2b_flag = b2b_flag
        self.image_token = image_token
        self.hash = hash
        self.portal = portal
        self.contact_name = contact_name
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[UploadImageFileRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[UploadImageFileRequestParams.STATUS_ID] = self.status_id
        args[UploadImageFileRequestParams.MIME_SUB_TYPE] = self.mime_sub_type
        args[UploadImageFileRequestParams.SEND_EMAIL_NOTIFICATION] = self.send_email_notification
        args[UploadImageFileRequestParams.B2B_FLAG] = self.b2b_flag
        args[UploadImageFileRequestParams.IMAGE_TOKEN] = self.image_token
        args[UploadImageFileRequestParams.HASH] = self.hash
        args[UploadImageFileRequestParams.PORTAL] = self.portal
        args[UploadImageFileRequestParams.CONTACT_NAME] = self.contact_name
        return args
