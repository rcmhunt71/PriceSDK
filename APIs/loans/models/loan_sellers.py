from dataclasses import dataclass, fields

from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass()
class LoanSellersInfoKeys:
    SELLER_NUMBER: str = "SellerNumber"
    FIRST_NAME: str = "FirstName"
    LAST_NAME: str = "LastName"
    GENERATION: str = "Generation"
    TITLE: str = "Title"
    ADDRESS: str = "Address"
    SUITE: str = "Suite"
    CITY: str = "City"
    ZIP: str = "Zip"
    SAME_AS_SUBJECT_PROPERTY_ADDRESS: str = "SameAsSubjectPropertyAddress"
    PARTIAL_EXEMPTION: str = "PartialExemption"


@dataclass()
class LoanSellersKeys:
    LOAN_SELLERS: str = "LoanSellers"


class LoanSeller(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(LoanSellersInfoKeys)]


class LoanSellers(BaseListResponse):
    _SUB_MODEL = LoanSeller
