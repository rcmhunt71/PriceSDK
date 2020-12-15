from dataclasses import dataclass

from base.clients.base_client import BaseClient
from base.common.response import CommonResponse

from APIs.task_items.requests.download_image_files import DownloadImageFilesRequest
from APIs.task_items.requests.download_image_files_by_status_id_list import DownloadImageFilesByStatusIdListRequest
from APIs.task_items.requests.get_all_print_forms import GetAllPrintFormsRequest
from APIs.task_items.requests.get_image import GetImageRequest

from APIs.task_items.responses.get_all_print_forms import GetAllPrintFormsResponse


@dataclass
class ApiEndpoints:
    DOWNLOAD_IMAGE_FILES: str = "download_image_files"
    DOWNLOAD_IMAGE_FILES_BY_STATUS_ID_LIST: str = "download_image_files_by_status_id_list"
    GET_ALL_PRINT_FORMS: str = "get_all_print_forms"
    GET_IMAGE: str = "get_image"


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
