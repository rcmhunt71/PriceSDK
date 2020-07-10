from dataclasses import dataclass

from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class BaseImportParamKeys(BaseRequestModelKeys):
    LOAN_NUMBER: str = "LoanNumber"
    FILE_TYPE: str = "FileType"
    DATE_NAME: str = "DateName"


@dataclass
class ImportFromFileParamKeys(BaseImportParamKeys):
    BASE64_FILE_DATA: str = "Base64FileData"


@dataclass
class ImportFromFileWithDataParamKeys(BaseImportParamKeys):
    UPLOAD_TOKEN: str = "UploadToken"
    B2B_FLAG: str = "B2BFlag"


class ImportFromFileRequest(SimpleRequestModel):
    def __init__(self, loan_number, base64_file_data, file_type, date_name, session_id, nonce):
        self.loan_number = loan_number
        self.file_type = file_type
        self.date_name = date_name
        self.base64_file_data = base64_file_data
        super().__init__(session_id=session_id, nonce=nonce)

    def to_params(self):
        args = super().to_params()
        args.update({
            ImportFromFileParamKeys.FILE_TYPE: self.file_type.value,
            ImportFromFileParamKeys.LOAN_NUMBER: self.loan_number,
            ImportFromFileParamKeys.DATE_NAME: self.date_name,
        })
        return args


class ImportFromFileWithDateRequest(SimpleRequestModel):
    def __init__(self, loan_number, upload_token, b2b_flag, file_type, date_name, session_id, nonce):
        self.loan_number = loan_number
        self.upload_token = upload_token
        self.file_type = file_type
        self.date_name = date_name
        self.b2b_flag = b2b_flag
        super().__init__(session_id=session_id, nonce=nonce)

    def to_params(self):
        return {
            ImportFromFileWithDataParamKeys.SESSION_ID: self.session_id,
            ImportFromFileWithDataParamKeys.NONCE: self.nonce,
            ImportFromFileWithDataParamKeys.FILE_TYPE: self.file_type.value,
            ImportFromFileWithDataParamKeys.LOAN_NUMBER: self.loan_number,
            ImportFromFileWithDataParamKeys.DATE_NAME: self.date_name,
            ImportFromFileWithDataParamKeys.UPLOAD_TOKEN: self.upload_token,
            ImportFromFileWithDataParamKeys.B2B_FLAG: int(self.b2b_flag),
        }