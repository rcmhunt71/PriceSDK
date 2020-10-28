from typing import List, Dict, Any, Union
from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, KwargsRequestModel, DataKeys


@dataclass
class SetCustomerRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"


@dataclass
class SetCustomerPayload:
    CUSTOMER_ID: str = "CustomerID"
    FIELDS: str = "Fields"


@dataclass
class SetCustomerFieldNames:
    PERSON_ID: str = "Person_ID"
    DECLARE_A: str = "Declare_A"
    DECLARE_B: str = "Declare_B"
    DECLARE_C: str = "Declare_C"
    DECLARE_D: str = "Declare_D"
    DECLARE_E: str = "Declare_E"
    DECLARE_F: str = "Declare_F"
    DECLARE_G: str = "Declare_G"
    DECLARE_H: str = "Declare_H"
    DECLARE_I: str = "Declare_I"
    DECLARE_J: str = "Declare_J"
    DECLARE_K: str = "Declare_K"
    DECLARE_L: str = "Declare_L"
    DECLARE_M: str = "Declare_M"
    RACE_AMERICAN_ALASKA: str = "Race_American_Alaska"
    RACE_ASIAN: str = "Race_Asian"
    RACE_WHITE: str = "Race_White"
    RACE_BLACK: str = "Race_Black"
    RACE_HAWAIIAN_PACIFIC: str = "Race_Hawaiian_Pacific"
    RACE_NOT_PROVIDED: str = "Race_Not_Provided"
    RACE_NOT_APPLICABLE: str = "Race_Not_Applicable"
    RACE_OTHER: str = "Race_Other"
    ETHNICITY: str = "Ethnicity"
    SEX: str = "Sex"
    NOT_FURNISH_INFORMATION: str = "Not_Furnish_Information"
    COBORROWER_INCOME_USED: str = "Coborrower_Income_Used"
    COMPLETED_JOINTLY: str = "Completed_Jointly"
    DEPENDENTS_AGES: str = "Dependents_Ages"
    DEPENDENTS: str = "Dependents"
    MARITAL_STATUS: str = "Marital_Status"
    APPLICATION_TAKEN_BY: str = "Application_Taken_By"
    CREDIT_REPORT_AUTH: str = "Credit_Report_Auth"
    EFX_CREDIT_SCORE: str = "EFX_Credit_Score"
    XPN_CREDIT_SCORE: str = "XPN_Credit_Score"
    TUC_CREDIT_SCORE: str = "TUC_Credit_Score"
    CREDIT_REFERENCE_VENDOR: str = "Credit_Reference_Vendor"
    ALIMONY_OWED_TO: str = "Alimony_Owed_To"
    ALIMONY: str = "Alimony"
    ALIMONY_MONTHS_LEFT: str = "Alimony_Months_Left"
    CUSTOMER_FORECLOSURE_DATE: str = "Customer_Foreclosure_Date"
    PREVIOUS_ADDRESS_1: str = "Previous_Address_1"
    PREVIOUS_ADDRESS_2: str = "Previous_Address_2"
    MAILING_ADDRESS_ID: str = "Mailing_Address_ID"
    INTERVIEW_CONTACT_ID: str = "Interview_Contact_ID"
    INTERVIEW_CONTACT_COMP_ID: str = "Interview_Contact_Comp_ID"
    INTERVIEWED_BY: str = "Interviewed_By"
    INTERVIEW_COMPANY_ID: str = "Interview_Company_ID"
    INTERVIEW_EMPLOYEE_ID: str = "Interview_Employee_ID"
    HMDAGENDER_TYPE_MALE: str = "HMDAGenderTypeMale"
    HMDAGENDER_TYPE_FEMALE: str = "HMDAGenderTypeFemale"
    HMDAGENDER_REFUSAL_INDICATOR: str = "HMDAGenderRefusalIndicator"
    HMDAGENDER_COLLECTED_BASED_ON_VISUAL_OBSERVATION_OR_NAME_INDICATOR: str = "HMDAGenderCollectedBasedOnVisualObservationOrNameIndicator"
    HMDAETHNICITY_TYPE_HISPANIC: str = "HMDAEthnicityTypeHispanic"
    HMDAETHNICITY_TYPE_NOT_HISPANIC: str = "HMDAEthnicityTypeNotHispanic"
    HMDAETHNICITY_ORIGIN_TYPE_CUBAN: str = "HMDAEthnicityOriginTypeCuban"
    HMDAETHNICITY_ORIGIN_TYPE_MEXICAN: str = "HMDAEthnicityOriginTypeMexican"
    HMDAETHNICITY_ORIGIN_TYPE_PUERTO_RICAN: str = "HMDAEthnicityOriginTypePuertoRican"
    HMDAETHNICITY_ORIGIN_TYPE_OTHER: str = "HMDAEthnicityOriginTypeOther"
    HMDAETHNICITY_ORIGIN_TYPE_OTHER_DESCRIPTION: str = "HMDAEthnicityOriginTypeOtherDescription"
    HMDARACE_TRIBE: str = "HMDARaceTribe"
    HMDARACE_DESIGNATION_TYPE_ASIAN_INDIAN: str = "HMDARaceDesignationTypeAsianIndian"
    HMDARACE_DESIGNATION_TYPE_CHINESE: str = "HMDARaceDesignationTypeChinese"
    HMDARACE_DESIGNATION_TYPE_FILIPINO: str = "HMDARaceDesignationTypeFilipino"
    HMDARACE_DESIGNATION_TYPE_JAPANESE: str = "HMDARaceDesignationTypeJapanese"
    HMDARACE_DESIGNATION_TYPE_KOREAN: str = "HMDARaceDesignationTypeKorean"
    HMDARACE_DESIGNATION_TYPE_VIETNAMESE: str = "HMDARaceDesignationTypeVietnamese"
    HMDARACE_DESIGNATION_TYPE_OTHER_ASIAN: str = "HMDARaceDesignationTypeOtherAsian"
    HMDARACE_DESIGNATION_TYPE_OTHER_ASIAN_DESCRIPTION: str = "HMDARaceDesignationTypeOtherAsianDescription"
    HMDARACE_DESIGNATION_TYPE_HAWAIIAN: str = "HMDARaceDesignationTypeHawaiian"
    HMDARACE_DESIGNATION_TYPE_GUAMANIAN: str = "HMDARaceDesignationTypeGuamanian"
    HMDARACE_DESIGNATION_TYPE_SAMOAN: str = "HMDARaceDesignationTypeSamoan"
    HMDARACE_DESIGNATION_TYPE_OTHER_PACIFIC_ISLANDER: str = "HMDARaceDesignationTypeOtherPacificIslander"
    HMDARACE_DESIGNATION_TYPE_OTHER_PACIFIC_ISLANDER_DESCRIPTION: str = "HMDARaceDesignationTypeOtherPacificIslanderDescription"
    HMDARACE_COLLECTED_BASED_ON_VISUAL_OBSERVATION_OR_SURNAME_INDICATOR: str = "HMDARaceCollectedBasedOnVisualObservationOrSurnameIndicator"
    HMDA2018ETHNICITY1: str = "HMDA2018Ethnicity1"
    HMDA2018ETHNICITY2: str = "HMDA2018Ethnicity2"
    HMDA2018ETHNICITY3: str = "HMDA2018Ethnicity3"
    HMDA2018ETHNICITY4: str = "HMDA2018Ethnicity4"
    HMDA2018ETHNICITY5: str = "HMDA2018Ethnicity5"
    HMDA2018RACE1: str = "HMDA2018Race1"
    HMDA2018RACE2: str = "HMDA2018Race2"
    HMDA2018RACE3: str = "HMDA2018Race3"
    HMDA2018RACE4: str = "HMDA2018Race4"
    HMDA2018RACE5: str = "HMDA2018Race5"
    APPLICATION_TAKEN_METHOD_TYPE: str = "ApplicationTakenMethodType"
    VESTING_LANGUAGE: str = "Vesting_Language"
    FIRST_TIME_HOME_BUYER: str = "First_Time_Home_Buyer"
    IS_VETERAN: str = "IsVeteran"
    RACE: str = "Race"
    CREDIT_SCORE: str = "Credit_Score"
    CREDIT_SCORE_DATE: str = "Credit_Score_Date"
    CREDIT_REFERENCE_NUMBER: str = "CreditReferenceNumber"
    CREDIT_REFERENCE_DATE: str = "CreditReferenceDate"
    LAST_SHORT_SALE_DATE: str = "LastShortSaleDate"
    PROPERTY_TYPE: str = "Property_Type"
    TITLE_HELD_AS: str = "Title_Held_As"
    PREVIOUS_PROPERTY_FHASECONDARY_RESIDENCE: str = "PreviousPropertyFHASecondaryResidence"
    MILITARY_SERVICE_INDICATOR: str = "MilitaryServiceIndicator"
    MILITARY_ACTIVE_DUTY: str = "MilitaryActiveDuty"
    MILITARY_SERVICE_EXPECTED_COMPLETION_DATE: str = "MilitaryServiceExpectedCompletionDate"
    MILITARY_RETIRED: str = "MilitaryRetired"
    MILITARY_RESERVE_NATIONAL_GUARD_NEVER_ACTIVATED: str = "MilitaryReserveNationalGuardNeverActivated"
    MILITARY_SURVIVING_SPOUSE: str = "MilitarySurvivingSpouse"
    DOMESTIC_RELATIONSHIP_TYPE: str = "DomesticRelationshipType"
    DOMESTIC_RELATIONSHIP_TYPE_OTHER_DESCRIPTION: str = "DomesticRelationshipTypeOtherDescription"
    DOMESTIC_RELATIONSHIP_STATE_CODE: str = "DomesticRelationshipStateCode"
    DOMESTIC_RELATIONSHIP_INDICATOR: str = "DomesticRelationshipIndicator"
    SPECIAL_BORROWER_SELLER_RELATIONSHIP_INDICATOR: str = "SpecialBorrowerSellerRelationshipIndicator"
    UNDISCLOSED_BORROWED_FUNDS_AMOUNT: str = "UndisclosedBorrowedFundsAmount"
    UNDISCLOSED_MORTGAGE_APPLICATION_INDICATOR: str = "UndisclosedMortgageApplicationIndicator"
    UNDISCLOSED_CREDIT_APPLICATION_INDICATOR: str = "UndisclosedCreditApplicationIndicator"
    UNDISCLOSED_COMAKER_OF_NOTE_INDICATOR: str = "UndisclosedComakerOfNoteIndicator"
    PRIOR_PROPERTY_DEED_IN_LIEU_CONVEYED_INDICATOR: str = "PriorPropertyDeedInLieuConveyedIndicator"
    PRIOR_PROPERTY_SHORT_SALE_COMPLETED_INDICATOR: str = "PriorPropertyShortSaleCompletedIndicator"
    PRIOR_PROPERTY_FORECLOSURE_COMPLETED_INDICATOR: str = "PriorPropertyForeclosureCompletedIndicator"
    BANKRUPTCY_CHAPTER_TYPE7: str = "BankruptcyChapterType7"
    BANKRUPTCY_CHAPTER_TYPE11: str = "BankruptcyChapterType11"
    BANKRUPTCY_CHAPTER_TYPE12: str = "BankruptcyChapterType12"
    BANKRUPTCY_CHAPTER_TYPE13: str = "BankruptcyChapterType13"
    NON_PERMANENT_RESIDENT_ALIEN: str = "NonPermanentResidentAlien"
    NON_RESIDENT_ALIEN: str = "NonResidentAlien"
    DOMESTIC_RELATIONSHIP_PRINT_INDICATOR: str = "DomesticRelationshipPrintIndicator"
    NOTES_FOR_1003: str = "Notes_For_1003"


class SetCustomerRequest(KwargsRequestModel):
    data_payload = SetCustomerPayload
    REQUEST_PAYLOAD_KEY: str = "Customers"

    def __init__(self, loan_number_id, payload_dict, session_id, nonce, pretty_print, **kwargs):
        self.loan_number_id = loan_number_id
        super().__init__(session_id=session_id, nonce=nonce, payload=payload_dict, pretty_print=pretty_print, **kwargs)

    def to_params(self) -> Dict[str, Any]:
        args = super().to_params()
        args[SetCustomerRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        return args

    def build_payload(self) -> Dict[str, List[Dict[Any, Union[List[Dict[str, Any]], Any]]]]:
        payload_dict = {}
        for payload_key in self.attr_list:
            if getattr(self, payload_key.lower(), None) is not None:
                if payload_key.title() == SetCustomerPayload.FIELDS:
                    fields_list = []
                    for key, value in getattr(self, payload_key.lower()).items():
                        fields_list.append(
                            {DataKeys.FIELD_NAME: getattr(SetCustomerFieldNames, key.upper(), key),
                            DataKeys.FIELD_VALUE: value})
                    payload_dict.update({SetCustomerPayload.FIELDS: fields_list})
                    continue
                payload_dict.update({getattr(self.data_payload, payload_key.upper(), payload_key): getattr(self, payload_key.lower())})
        return {self.REQUEST_PAYLOAD_KEY: [payload_dict]}


if __name__ == "__main__":
    import pprint
    kwargs = {
        "CustomerID": 98765,
        "Fields": {
            SetCustomerFieldNames.PERSON_ID: 126597,
            SetCustomerFieldNames.SEX: "F",
            SetCustomerFieldNames.DECLARE_A: "N",
            SetCustomerFieldNames.DECLARE_B: "N",
            SetCustomerFieldNames.DECLARE_C: "N",
            SetCustomerFieldNames.DECLARE_D: "Y",
            SetCustomerFieldNames.DECLARE_E: "Y",
            SetCustomerFieldNames.CREDIT_SCORE: "750",
            SetCustomerFieldNames.BANKRUPTCY_CHAPTER_TYPE7: False,
            SetCustomerFieldNames.RACE: "White, not of Hispanic Origin",
            SetCustomerFieldNames.ETHNICITY: "O",
            SetCustomerFieldNames.NON_PERMANENT_RESIDENT_ALIEN: False
        }
    }
    print(f"KWARGS: {pprint.pformat(kwargs)}")

    obj = SetCustomerRequest(loan_number_id=10000001, payload_dict=None, session_id=123456, nonce=123245687, pretty_print=False, **kwargs)
    print(f"\nPAYLOAD: {pprint.pformat(obj.payload)}")

    print("\nTesting SetCustomerRequest - payload_dict")
    obj_args = SetCustomerRequest(loan_number_id=986532147, vendor_name= "test_vendor", payload_dict=obj.payload,
                                              pretty_print=False, session_id=123456, nonce=123245687)
    print(f"PAYLOAD: {pprint.pformat(obj_args.payload)}")
