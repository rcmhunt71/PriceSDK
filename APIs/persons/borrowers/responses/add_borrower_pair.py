from dataclasses import dataclass
from base.common.response import CommonResponse

@dataclass
class BorrowerPairsInfoKeys:
    PRIMARY_BORROWER_ID: str = "PrimaryBorrowerId"
    SECONDARY_BORROWER_ID: str = "SecondaryBorrowerId"


class AddBorrowerPairResponse(CommonResponse):
    _ADD_KEYS = [BorrowerPairsInfoKeys.PRIMARY_BORROWER_ID, BorrowerPairsInfoKeys.SECONDARY_BORROWER_ID]
    _SUB_MODELS = [None, None]


if __name__ == "__main__":
    import pprint

    sample_response = {"PrimaryBorrowerId": 123456,
        "SecondaryBorrowerId": 654321,
        "Successful": True}

    obj = AddBorrowerPairResponse(**sample_response)
    print(f"\nPrimaryBorrowerId: {pprint.pformat(getattr(obj, BorrowerPairsInfoKeys.PRIMARY_BORROWER_ID))}",
    f"\nSecondaryBorrowerId: {pprint.pformat(getattr(obj, BorrowerPairsInfoKeys.SECONDARY_BORROWER_ID))}")
