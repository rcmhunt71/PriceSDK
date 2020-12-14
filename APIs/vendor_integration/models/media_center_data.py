from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class MediaCenterDataInfoKeys:
    LOAN_ID: str = "LoanID"
    LO_ID: str = "LOID"
    LO_NMLS_ID: str = "LONMLSID"
    LO_LIEN_POSITION: str = "LOLienPosition"
    LO_FNAME: str = "LOFName"
    LO_LNAME: str = "LOLName"
    LOAN_STATUS: str = "LoanStatus"
    PROPERTY_ADDRESS: str = "PropertyAddress"
    PROPERTY_CITY: str = "PropertyCity"
    PROPERTY_STATE: str = "PropertyState"
    PROPERTY_ZIP: str = "PropertyZip"
    BORROWER_HASH_ID: str = "BorrowerHashID"
    BORROWER_FNAME: str = "BorrowerFName"
    BORROWER_LNAME: str = "BorrowerLName"
    BORROWER_MNAME: str = "BorrowerMName"
    BORROWER_SALUTATION: str = "BorrowerSalutation"
    BORROWER_WORK_PHONE: str = "BorrowerWorkPhone"
    BORROWER_WORK_PHONE_EXT: str = "BorrowerWorkPhoneExt"
    BORROWER_HOME_PHONE: str = "BorrowerHomePhone"
    BORROWER_MOBILE: str = "BorrowerMobile"
    BORROWER_EMAIL: str = "BorrowerEmail"
    BORROWER_FAX: str = "BorrowerFax"
    BORROWER_COMPANY_NAME: str = "BorrowerCompanyName"
    BORROWER_BEST_WAY_TO_CONTACT: str = "BorrowerBestWayToContact"
    BORROWER_PROPERTY_ADDRESS: str = "BorrowerPropertyAddress"
    BORROWER_PROPERTY_CITY: str = "BorrowerPropertyCity"
    BORROWER_PROPERTY_STATE: str = "BorrowerPropertyState"
    BORROWER_PROPERTY_ZIP: str = "BorrowerPropertyZip"
    OWN_PRESENT_RESIDENCE: str = "OwnPresentResidence"
    BORROWER_JOB_TITLE: str = "BorrowerJobTitle"
    BORROWER_BIRTHDAY: str = "BorrowerBirthday"
    CD_SENT: str = "CDSent"
    CD_RECEIPT: str = "CDReceipt"
    CO_BORROWER_LNAME: str = "CoBorrowerLName"
    CO_BORROWER_FNAME: str = "CoBorrowerFName"
    CO_BORROWER_MNAME: str = "CoBorrowerMName"
    CO_BORROWER_SALUTATION: str = "CoBorrowerSalutation"
    CO_BORROWER_WORK_PHONE: str = "CoBorrowerWorkPhone"
    CO_BORROWER_WORK_PHONE_EXT: str = "CoBorrowerWorkPhoneExt"
    CO_BORROWER_MOBILE: str = "CoBorrowerMobile"
    CO_BORROWER_EMAIL: str = "CoBorrowerEmail"
    CO_BORROWER_BEST_WAY_TO_CONTACT: str = "CoBorrowerBestWayToContact"
    CONTACT_DISPLAY_NAME: str = "ContactDisplayName"
    CO_BORROWER_BIRTHDAY: str = "CoBorrowerBirthday"
    REFERRER_LAST_NAME: str = "ReferrerLastName"
    REFERRER_FIRST_NAME: str = "ReferrerFirstName"
    APPLICATION_DATE: str = "ApplicationDate"
    DATE_FUNDED: str = "DateFunded"
    ESTIMATED_CLOSING_DATE: str = "EstimatedClosingDate"
    APPRAISAL_ORDERED_DATE: str = "AppraisalOrderedDate"
    APPRAISAL_RECEIVED_DATE: str = "AppraisalReceivedDate"
    APPROVAL_DATE: str = "ApprovalDate"
    LOCK_EXPIRATION_DATE: str = "LockExpirationDate"
    CONSTRUCTION_CLOSE_DATE: str = "ConstructionCloseDate"
    FIRST_PAYMENT_DUE_DATE: str = "FirstPaymentDueDate"
    DOCS_TO_ESCROW_TITLE_DATE: str = "DocsToEscrowTitleDate"
    CANCELLATION_DATE: str = "CancellationDate"
    PURCHASE_PRICE: str = "PurchasePrice"
    APPRAISED_VALUE: str = "AppraisedValue"
    TOTAL_LOAN_AMOUNT: str = "TotalLoanAmount"
    PMI: str = "PMI"
    LOAN_PURPOSE: str = "LoanPurpose"
    TOTAL_DOWN_PAYMENT: str = "TotalDownPayment"
    IMPOUNDS_ESCROWS: str = "ImpoundsEscrows"
    OCCUPANCY: str = "Occupancy"
    TOTAL_MONTHLY_PAYMENT: str = "TotalMonthlyPayment"
    PREPAY_PENALTY_DATE: str = "PrepayPenaltyDate"
    DOCUMENTATION_TYPE: str = "DocumentationType"
    CLTV: str = "CLTV"
    LOAN_1_LOAN_NUMBER: str = "Loan1LoanNumber"
    LOAN_1_LOAN_AMOUNT: str = "Loan1LoanAmount"
    LOAN_1_INT_RATE: str = "Loan1IntRate"
    LOAN_1_LTV: str = "Loan1LTV"
    LOAN_1_LOAN_PRODUCT: str = "Loan1LoanProduct"
    LOAN_1_LOAN_TYPE: str = "Loan1LoanType"
    LOAN_1_ARM_MARGIN: str = "Loan1ARMMargin"
    LOAN_1_ARM_INDEX: str = "Loan1ARMIndex"
    LOAN_1_MONTHLY_PAYMENT: str = "Loan1MonthlyPayment"
    LOAN_2_LOAN_NUMBER: str = "Loan2LoanNumber"
    LOAN_2_LOAN_AMOUNT: str = "Loan2LoanAmount"
    LOAN_2_INT_RATE: str = "Loan2IntRate"
    LOAN_2_LTV: str = "Loan2LTV"
    LOAN_2_LOAN_PRODUCT: str = "Loan2LoanProduct"
    LOAN_2_LOAN_TYPE: str = "Loan2LoanType"
    LOAN_2_ARM_MARGIN: str = "Loan2ARMMargin"
    LOAN_2_ARM_INDEX: str = "Loan2ARMIndex"
    LOAN_2_MONTHLY_PAYMENT: str = "Loan2MonthlyPayment"
    BUYER_AGENT_ID: str = "BuyerAgentID"
    BUYER_AGENT_FNAME: str = "BuyerAgentFName"
    BUYER_AGENT_LNAME: str = "BuyerAgentLName"
    BUYER_AGENT_COMPANY: str = "BuyerAgentCompany"
    BUYER_AGENT_PHONE: str = "BuyerAgentPhone"
    BUYER_AGENT_EMAIL: str = "BuyerAgentEmail"
    LISTING_AGENT_ID: str = "ListingAgentID"
    LISTING_AGENT_NAME: str = "ListingAgentName"
    LISTING_AGENT_COMPANY: str = "ListingAgentCompany"
    LISTING_AGENT_PHONE: str = "ListingAgentPhone"
    LISTING_AGENT_EMAIL: str = "ListingAgentEmail"
    ESCROW_COMPANY_NAME: str = "EscrowCompanyName"
    ESCROW_ADDRESS: str = "EscrowAddress"
    ESCROW_CITY: str = "EscrowCity"
    ESCROW_STATE: str = "EscrowState"
    ESCROW_ZIP: str = "EscrowZip"
    ESCROW_PHONE_AREA_CODE: str = "EscrowPhoneAreaCode"
    ESCROW_PHONE: str = "EscrowPhone"
    ESCROW_FAX_AREA_CODE: str = "EscrowFaxAreaCode"
    ESCROW_FAX: str = "EscrowFax"
    ESCROW_NO: str = "EscrowNo"
    TITLE_ATTN: str = "TitleAttn"


@dataclass
class MediaCenterDataKeys:
    DATA: str = "Data"


class MediaCenterData(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(MediaCenterDataInfoKeys)]