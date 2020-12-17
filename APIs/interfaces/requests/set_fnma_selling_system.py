from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, KwargsRequestModel


@dataclass
class SetFNMASellingSystemRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"


@dataclass
class SetFNMASellingSystemFieldNames:
    LOAN_COMMENT: str = "LoanComment"
    LOAN_STATE_TYPE: str = "LoanStateType"
    SELLER_LOAN_IDENTIFIER: str = "SellerLoanIdentifier"
    LOAN_STATE_DATE: str = "LoanStateDate"
    UNPAID_BALANCE: str = "UnpaidBalance"
    DELINQUENT_PAYMENTS: str = "DelinquentPayments"
    LAST_PAID_INSTALLMENT: str = "LastPaidInstallment"
    PRIMARY_MI_ABSENCE_REASON: str = "PrimaryMIAbsenceReason"
    SPECIAL_FLOOD_AREA: str = "SpecialFloodArea"
    MI_COMPANY_NAME_OTHER: str = "MICompanyNameOther"
    COMMITMENT_IDENTIFIER: str = "CommitmentIdentifier"
    OWNERSHIP_PERCENTAGE: str = "OwnershipPercentage"
    PRODUCT_PLAN_IDENTIFIER: str = "ProductPlanIdentifier"
    CLOSING_LOAN_ROLE_TYPE: str = "ClosingLoanRoleType"
    CLOSING_LOAN_STATE_TYPE: str = "ClosingLoanStateType"
    CLOSING_LOAN_STATE_DATE: str = "ClosingLoanStateDate"
    CLOSING_RELOCATION: str = "ClosingRelocation"
    CLOSING_SHARE_EQUITY: str = "ClosingShareEquity"
    LOAN_MODIFICATION_EFFECTIVE_DATE: str = "LoanModificationEffectiveDate"
    POOL_INVESTOR_REMITTANCE_TYPE: str = "PoolInvestorRemittanceType"
    POOL_LOAN_ACQUISITION_SCHEDULED_UPB_AMOUNT: str = "PoolLoanAcquisitionScheduledUPBAmount"
    NEXT_RATE_ADJUSTMENT_EFFECTIVE_DATE: str = "NextRateAdjustmentEffectiveDate"
    FREDDIE_MAC_CREDIT_SCORE_IMPAIRMENT: str = "FreddieMacCreditScoreImpairment"
    FREDDIE_MAC_DOWNPAYMENT_SOURCE: str = "FreddieMacDownpaymentSource"
    FREDDIE_MAC_BUY_DOWN_UP_BASIS_POINTS: str = "FreddieMacBuyDownUpBasisPoints"
    FREDDIE_MAC_CREDIT_SCORE_SELECTION_METHOD: str = "FreddieMacCreditScoreSelectionMethod"
    FREDDIE_MAC_LOAN_BUY_UP_DOWN_TYPE: str = "FreddieMacLoanBuyUpDownType"
    FREDDIE_MAC_CONVERSION_TYPE: str = "FreddieMacConversionType"
    FREDDIE_MAC_GUARANTEE_FEE_ADD_ON: str = "FreddieMacGuaranteeFeeAddOn"
    FREDDIE_MAC_CONVERTIBLE_STATUS_TYPE: str = "FreddieMacConvertibleStatusType"
    MBS_LOAN_SELLER_IDENTIFIER: str = "MBSLoanSellerIdentifier"
    MI_COMPANY_NAME_TYPE: str = "MICompanyNameType"
    MI_CERTIFICATE_NUMBER: str = "MICertificateNumber"
    AGGREGATE_LOAN_CURTAILMENT_AMOUNT: str = "AggregateLoanCurtailmentAmount"
    MAX_HELOC_BALANCE: str = "MaxHELOCBalance"
    HELOC_INDICATOR: str = "HELOCIndicator"
    INVESTOR_COLLATERAL_PROGRAM_IDENTIFIER: str = "InvestorCollateralProgramIdentifier"
    INVESTOR_FEATURE_IDENTIFIER5: str = "InvestorFeatureIdentifier5"
    FHLMC_REFINANCE_PROGRAM_IDENTIFIER: str = "FHLMCRefinanceProgramIdentifier"
    VALUATION_METHOD_OTHER_TYPE_ID: str = "ValuationMethodOtherTypeID"
    LENDER_PAID_RATE_ADJUSTMENT: str = "LenderPaidRateAdjustment"


class SetFNMASellingSystemRequest(KwargsRequestModel):
    data_payload = SetFNMASellingSystemFieldNames
    REQUEST_PAYLOAD_KEY: str = "FNMAFields"

    def __init__(self, loan_number_id, payload_dict, session_id, nonce, pretty_print, **kwargs):
        self.loan_number_id = loan_number_id
        super().__init__(payload=payload_dict, session_id=session_id, nonce=nonce, pretty_print=pretty_print, **kwargs)

    def to_params(self):
        args = super().to_params()
        args[SetFNMASellingSystemRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        return args
