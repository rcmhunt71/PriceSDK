from APIs.person.borrower.models.borrower import BorrowerDetailKeys, BorrowerDetailList
from base.common.response import CommonResponse


class GetBorrower(CommonResponse):
    _ADD_KEYS = [BorrowerDetailKeys.BORROWER_DETAIL]
    _SUB_MODELS = [BorrowerDetailList]

