from dataclasses import dataclass
from APIs.creating_loan.requests.import_from_file import ImportFromFileRequest, ImportFromFileWithDateRequest
from APIs.creating_loan.responses.add_a_loan import AddALoanResponse, ImportFromFileWithDateResponse, \
    ImportFromFileResponse
from base.clients.base_client import BaseClient
from base.common.models.request import SimpleRequestModel


@dataclass
class ApiEndpoints:
    ADD_A_LOAN: str = "add_a_loan"
    IMPORT_FROM_FILE: str = "import_from_file"
    IMPORT_FROM_FILE_WITH_DATE: str = "import_from_file_with_date"


class CreatingLoanClient(BaseClient):
    CONTENT_ENCODING = "Content-Encoding"
    BASE64_COMPRESS = "base64-compress"
    ACCEPT_ENCODING = "Accept-Encoding"
    ENCODING_FORMAT = "deflate, gzip, identity"
    import_from_file_headers = {CONTENT_ENCODING: BASE64_COMPRESS, ACCEPT_ENCODING: ENCODING_FORMAT}

    def add_a_loan(self, session_id=None, nonce=None):
        request_model = SimpleRequestModel(session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce))

        return self.post(resource_endpoint=ApiEndpoints.ADD_A_LOAN, response_model=AddALoanResponse,
            data=request_model.payload, params=request_model.as_params_dict)

    def import_from_file(self, base64_file_data, file_type, loan_number, date_name, officer_id=None,
                         session_id=None, nonce=None):
        """ 'Base64FileData' key needs to be encoded along with binary file """
        request_model = ImportFromFileRequest(base64_file_data=base64_file_data, file_type=file_type,
                                              loan_number=loan_number, date_name=date_name, officer_id=officer_id,
                                              session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce))

        return self.post(resource_endpoint=ApiEndpoints.IMPORT_FROM_FILE, response_model=ImportFromFileResponse,
                         data={}, binary_data=request_model.base64_file_data, headers=self.import_from_file_headers,
                         params=request_model.as_params_dict)

    def import_from_file_with_date(self, upload_token, b2b_flag, file_type, loan_number, date_name, officer_id=None,
            session_id=None, nonce=None, pretty_print=False):
        request_model = ImportFromFileWithDateRequest(upload_token=upload_token, b2b_flag=b2b_flag, file_type=file_type,
            loan_number=loan_number, date_name=date_name, officer_id=officer_id,
            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.IMPORT_FROM_FILE_WITH_DATE,
            response_model=ImportFromFileWithDateResponse, data=request_model.payload,
            params=request_model.as_params_dict)
