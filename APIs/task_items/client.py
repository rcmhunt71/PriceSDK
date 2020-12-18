from dataclasses import dataclass

from base.clients.base_client import BaseClient
from base.common.models.request import LoanNumberIdRequestModel, SimpleRequestModel
from base.common.response import CommonResponse

from APIs.task_items.requests.download_image_files import DownloadImageFilesRequest
from APIs.task_items.requests.download_image_files_by_status_id_list import DownloadImageFilesByStatusIdListRequest
from APIs.task_items.requests.get_all_print_forms import GetAllPrintFormsRequest
from APIs.task_items.requests.get_image import GetImageRequest
from APIs.task_items.requests.get_image_access_logs import GetImageAccessLogsRequest
from APIs.task_items.requests.get_image_thumbnail import GetImageThumbnailRequest
from APIs.task_items.requests.get_image_thumbnail_multiple import GetImageThumbnailMultipleRequest
from APIs.task_items.requests.get_loan_conditions_with_param import GetLoanConditionsWithParamRequest
from APIs.task_items.requests.get_loan_print_forms import GetLoanPrintFormsRequest
from APIs.task_items.requests.get_print_form_pdf import GetPrintFormPdfRequest
from APIs.task_items.requests.add_disclosure_histories import AddDisclosureHistoriesRequest
from APIs.task_items.requests.log_image_access import LogImageAccessRequest

from APIs.task_items.responses.get_all_print_forms import GetAllPrintFormsResponse
from APIs.task_items.responses.get_image_access_logs import GetImageAccessLogsResponse
from APIs.task_items.responses.get_image_thumbnail_multiple import GetImageThumbnailMultipleResponse
from APIs.task_items.responses.get_loan_conditions_with_param import GetLoanConditionsWithParamResponse
from APIs.task_items.responses.get_loan_print_forms import GetLoanPrintFormsResponse
from APIs.task_items.responses.get_loan_status_images import GetLoanStatusImagesResponse
from APIs.task_items.responses.get_task_item_group_list import GetTaskItemGroupListResponse
from APIs.task_items.responses.add_disclosure_histories import AddDisclosureHistoriesResponse


@dataclass
class ApiEndpoints:
    DOWNLOAD_IMAGE_FILES: str = "download_image_files"
    DOWNLOAD_IMAGE_FILES_BY_STATUS_ID_LIST: str = "download_image_files_by_status_id_list"
    GET_ALL_PRINT_FORMS: str = "get_all_print_forms"
    GET_IMAGE: str = "get_image"
    GET_IMAGE_ACCESS_LOGS: str = "get_image_access_logs"
    GET_IMAGE_THUMBNAIL: str = "get_image_thumbnail"
    GET_IMAGE_THUMBNAIL_MULTIPLE: str = "get_image_thumbnail_multiple"
    GET_LOAN_CONDITIONS_WITH_PARAM: str = "get_loan_conditions_with_param"
    GET_LOAN_PRINT_FORMS: str = "get_loan_print_forms"
    GET_LOAN_STATUS_IMAGES: str = "get_loan_status_images"
    GET_LOAN_STATUS_PDF: str = "get_loan_status_pdf"
    GET_PRINT_FORM_PDF: str = "get_print_form_pdf"
    GET_TASK_ITEM_GROUP_LIST: str = "get_task_item_group_list"
    ADD_DISCLOSURE_HISTORIES: str = "add_disclosure_histories"
    LOG_IMAGE_ACCESS: str = "log_image_access"


class TaskItemsClient(BaseClient):
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"
    json_headers = {
        CONTENT_TYPE: APPLICATION_JSON
    }

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

    def get_image_thumbnail_multiple(self, loan_number_id, payload_dict, session_id=None, nonce=None,
                                     pretty_print=False):
        request_model = GetImageThumbnailMultipleRequest(loan_number_id=loan_number_id, payload_dict=payload_dict,
                                                         session_id=self._get_session_id(session_id),
                                                         nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.GET_IMAGE_THUMBNAIL_MULTIPLE, data=request_model.as_json,
                         response_model=GetImageThumbnailMultipleResponse, params=request_model.as_params_dict,
                         headers=self.json_headers)

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

    def get_loan_status_images(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
                                                 session_id=self._get_session_id(session_id),
                                                 nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_LOAN_STATUS_IMAGES,
                        response_model=GetLoanStatusImagesResponse, params=request_model.as_params_dict)

    def get_loan_status_pdf(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
                                                 session_id=self._get_session_id(session_id),
                                                 nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_LOAN_STATUS_PDF, response_model=CommonResponse,
                        params=request_model.as_params_dict)

    def get_print_form_pdf(self, loan_number_id, print_form_comma_list, document_password=None, print_ln_name=None,
                           session_id=None, nonce=None, pretty_print=False):
        request_model = GetPrintFormPdfRequest(loan_number_id=loan_number_id,
                                               print_form_comma_list=print_form_comma_list,
                                               document_password=document_password, print_ln_name=print_ln_name,
                                               session_id=self._get_session_id(session_id),
                                               nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_PRINT_FORM_PDF, response_model=CommonResponse,
                        params=request_model.as_params_dict)

    def get_task_item_group_list(self, session_id=None, nonce=None, pretty_print=False):
        request_model = SimpleRequestModel(session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
                                           pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_TASK_ITEM_GROUP_LIST,
                        response_model=GetTaskItemGroupListResponse, params=request_model.as_params_dict)

    def add_disclosure_histories(self, loan_number_id, event, document_type_ids, upload_token, session_id=None,
                                 nonce=None, pretty_print=False):
        request_model = AddDisclosureHistoriesRequest(loan_number_id=loan_number_id, event=event,
                                                      document_type_ids=document_type_ids, upload_token=upload_token,
                                                      session_id=self._get_session_id(session_id),
                                                      nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.ADD_DISCLOSURE_HISTORIES, data=request_model.payload,
                         response_model=AddDisclosureHistoriesResponse, params=request_model.as_params_dict)

    def log_image_access(self, loan_number_id, image_id, person_id, log_option, status_id, session_id=None,
                         nonce=None, pretty_print=False):
        request_model = LogImageAccessRequest(loan_number_id=loan_number_id, image_id=image_id, person_id=person_id,
                                              log_option=log_option, status_id=status_id,
                                              session_id=self._get_session_id(session_id),
                                              nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.LOG_IMAGE_ACCESS, data=request_model.payload,
                         response_model=CommonResponse, params=request_model.as_params_dict)
