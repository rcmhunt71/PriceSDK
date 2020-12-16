from base.common.response import CommonResponse
from APIs.task_items.models.get_loan_status_images import GetLoanStatusImagesList, GetLoanStatusImagesKeys


class GetLoanStatusImagesResponse(CommonResponse):
    _ADD_KEYS = [GetLoanStatusImagesKeys.LOAN_STATUS_IMAGES]
    _SUB_MODELS = [GetLoanStatusImagesList]
