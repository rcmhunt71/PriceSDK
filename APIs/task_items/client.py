from dataclasses import dataclass

from base.clients.base_client import BaseClient
from base.common.response import CommonResponse

from APIs.task_items.requests.download_image_files import DownloadImageFilesRequest
from APIs.task_items.requests.download_image_files_by_status_id_list import DownloadImageFilesByStatusIdListRequest
from APIs.task_items.requests.get_all_print_forms import GetAllPrintFormsRequest
from APIs.task_items.requests.get_image import GetImageRequest
from APIs.task_items.requests.get_image_access_logs import GetImageAccessLogsRequest
from APIs.task_items.requests.get_image_thumbnail import GetImageThumbnailRequest
from APIs.task_items.requests.get_loan_conditions_with_param import GetLoanConditionsWithParamRequest
from APIs.task_items.requests.get_loan_print_forms import GetLoanPrintFormsRequest

from APIs.task_items.responses.get_all_print_forms import GetAllPrintFormsResponse
from APIs.task_items.responses.get_image_access_logs import GetImageAccessLogsResponse
from APIs.task_items.responses.get_loan_conditions_with_param import GetLoanConditionsWithParamResponse
from APIs.task_items.responses.get_loan_print_forms import GetLoanPrintFormsResponse


@dataclass
class ApiEndpoints:
    DOWNLOAD_IMAGE_FILES: str = "download_image_files"
    DOWNLOAD_IMAGE_FILES_BY_STATUS_ID_LIST: str = "download_image_files_by_status_id_list"
    GET_ALL_PRINT_FORMS: str = "get_all_print_forms"
    GET_IMAGE: str = "get_image"
    GET_IMAGE_ACCESS_LOGS: str = "get_image_access_logs"
    GET_IMAGE_THUMBNAIL: str = "get_image_thumbnail"
    GET_LOAN_CONDITIONS_WITH_PARAM: str = "get_loan_conditions_with_param"
    GET_LOAN_PRINT_FORMS: str = "get_loan_print_forms"


class TaskItemsClient(BaseClient):

    def download_image_files(self, loan_number_id, status_id, session_id=None, nonce=None, pretty_print=False):
        request_model = DownloadImageFilesRequest(loan_number_id=loan_number_id, status_id=status_id,
                                                  session_id=self._get_session_id(session_id),
                                                  nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.DOWNLOAD_IMAGE_FILES, response_model=CommonResponse,
                        params=request_model.as_params_dict)

    def download_image_files_by_status_id_list(self, loan_number_id, status_id_list, doc_password=None,
                                               session_id=None, nonce=None, pretty_print=False):
        request_model = DownloadImageFilesByStatusIdListRequest(loan_number_id=loan_number_id,
                                                                status_id_list=status_id_list,
                                                                doc_password=doc_password,
                                                                session_id=self._get_session_id(session_id),
                                                                nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.DOWNLOAD_IMAGE_FILES_BY_STATUS_ID_LIST,
                        response_model=CommonResponse, params=request_model.as_params_dict)

    def get_all_print_forms(self, newest_first, session_id=None, nonce=None, pretty_print=False):
        request_model = GetAllPrintFormsRequest(newest_first=newest_first, session_id=self._get_session_id(session_id),
                                                nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_ALL_PRINT_FORMS, response_model=GetAllPrintFormsResponse,
                        params=request_model.as_params_dict)

    def get_image(self, loan_number_id, page_number, image_id, status_id, session_id=None, nonce=None,
                  pretty_print=False):
        request_model = GetImageRequest(loan_number_id=loan_number_id, page_number=page_number, image_id=image_id,
                                        status_id=status_id, session_id=self._get_session_id(session_id),
                                        nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_IMAGE, response_model=CommonResponse,
                        params=request_model.as_params_dict)

    def get_image_access_logs(self, loan_number_id, status_id, limit, session_id=None, nonce=None, pretty_print=False):
        request_model = GetImageAccessLogsRequest(loan_number_id=loan_number_id, status_id=status_id, limit=limit,
                                                  session_id=self._get_session_id(session_id),
                                                  nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_IMAGE_ACCESS_LOGS, response_model=GetImageAccessLogsResponse,
                        params=request_model.as_params_dict)

    def get_image_thumbnail(self, loan_number_id, status_id, image_id, page_number, height=None, width=None,
                            session_id=None, nonce=None, pretty_print=False):
        request_model = GetImageThumbnailRequest(loan_number_id=loan_number_id, status_id=status_id, image_id=image_id,
                                                 page_number=page_number, height=height, width=width,
                                                 session_id=self._get_session_id(session_id),
                                                 nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_IMAGE_THUMBNAIL, response_model=CommonResponse,
                        params=request_model.as_params_dict)

    def get_loan_conditions_with_param(self, loan_number_id, other_params, session_id=None, nonce=None,
                                       pretty_print=False):
        request_model = GetLoanConditionsWithParamRequest(loan_number_id=loan_number_id, other_params=other_params,
                                                          session_id=self._get_session_id(session_id),
                                                          nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_LOAN_CONDITIONS_WITH_PARAM,
                        response_model=GetLoanConditionsWithParamResponse, params=request_model.as_params_dict)

    def get_loan_print_forms(self, loan_number_id, sort_by=None, session_id=None, nonce=None, pretty_print=False):
        request_model = GetLoanPrintFormsRequest(loan_number_id=loan_number_id, sort_by=sort_by,
                                                          session_id=self._get_session_id(session_id),
                                                          nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_LOAN_PRINT_FORMS, response_model=GetLoanPrintFormsResponse,
                        params=request_model.as_params_dict)
