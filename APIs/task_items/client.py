from dataclasses import dataclass

from base.clients.base_client import BaseClient
from base.common.response import CommonResponse

from APIs.task_items.requests.download_image_files import DownloadImageFilesRequest
from APIs.task_items.requests.download_image_files_by_status_id_list import DownloadImageFilesByStatusIdListRequest


@dataclass
class ApiEndpoints:
    DOWNLOAD_IMAGE_FILES: str = "download_image_files"
    DOWNLOAD_IMAGE_FILES_BY_STATUS_ID_LIST: str = "download_image_files_by_status_id_list"


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
