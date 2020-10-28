from APIs.persons.borrowers.models.borrower import Borrowers, BorrowersKeys
from base.common.response import CommonResponse


class GetBorrowerResponse(CommonResponse):
    _ADD_KEYS = [BorrowersKeys.BORROWER_DETAIL]
    _SUB_MODELS = [Borrowers]
