from dataclasses import dataclass
from enum import Enum

from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class BaseImportParamKeys(BaseRequestModelKeys):
    LOAN_NUMBER: str = "LoanNumber"
    FILE_TYPE: str = "FileType"
    DATE_NAME: str = "DateName"
    OFFICER_ID: str = "OfficerID"


@dataclass
class ImportFromFileWithDataParamKeys(BaseImportParamKeys):
    UPLOAD_TOKEN: str = "UploadToken"
    B2B_FLAG: str = "B2BFlag"


class ImportFromFileFileTypes(Enum):
    LOS_FILE = 0
    FANNIE_MAE = 1
    MISMO_AUS = 2
    IHM = 3
    MISMO_NYLX = 4
    IPA = 5
    URLA_MISMO = 6


class ImportFromFileRequest(SimpleRequestModel):
    def __init__(self, loan_number, base64_file_data, file_type, date_name, officer_id, session_id, nonce):
        self.loan_number = loan_number
        self.file_type = file_type
        self.date_name = date_name
        self.base64_file_data = base64_file_data
        self.officer_id = officer_id
        super().__init__(session_id=session_id, nonce=nonce)

    def to_params(self):
        args = super().to_params()
        args[ImportFromFileWithDataParamKeys.FILE_TYPE] = self.file_type
        args[ImportFromFileWithDataParamKeys.LOAN_NUMBER] = self.loan_number
        args[ImportFromFileWithDataParamKeys.DATE_NAME] = self.date_name
        args[ImportFromFileWithDataParamKeys.OFFICER_ID] = self.officer_id
        return args


class ImportFromFileWithDateRequest(SimpleRequestModel):
    def __init__(self, loan_number, upload_token, b2b_flag, file_type, date_name, officer_id, session_id, nonce,
            pretty_print):
        self.loan_number = loan_number
        self.upload_token = upload_token
        self.file_type = file_type
        self.date_name = date_name
        self.b2b_flag = b2b_flag
        self.officer_id = officer_id
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[ImportFromFileWithDataParamKeys.FILE_TYPE] = self.file_type
        args[ImportFromFileWithDataParamKeys.LOAN_NUMBER] = self.loan_number
        args[ImportFromFileWithDataParamKeys.DATE_NAME] = self.date_name
        args[ImportFromFileWithDataParamKeys.UPLOAD_TOKEN] = self.upload_token
        args[ImportFromFileWithDataParamKeys.B2B_FLAG] = int(self.b2b_flag)
        args[ImportFromFileWithDataParamKeys.OFFICER_ID] = self.officer_id
        return args
