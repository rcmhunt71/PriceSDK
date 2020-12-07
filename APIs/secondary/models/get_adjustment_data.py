from dataclasses import dataclass, fields

from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class GetAdjustmentDataInfoKeys:
    PROGRAM_ID: str = "ProgramID"
    COMMITMENT_PERIOD_ID: str = "CommitmentPeriodID"
    INVESTOR_ID: str = "InvestorID"
    INVESTOR_LOAN_NUMBER: str = "InvestorLoanNumber"
    COMMITMENT_NUMBER: str = "CommitmentNumber"
    POOL_NUMBER: str = "PoolNumber"
    REVENUE: str = "Revenue"
    INVESTOR_BASE_PRICE_DOLLAR: str = "InvestorBasePriceDollar"
    INVESTOR_BASE_PRICE_POINTS: str = "InvestorBasePricePoints"
    INVESTOR_ADJUSTMENT_DOLLAR: str = "InvestorAdjustmentDollar"
    INVESTOR_ADJUSTMENT_POINTS: str = "InvestorAdjustmentPoints"
    SRP_BASE_DOLLAR: str = "SRPBaseDollar"
    SRP_BASE_POINTS: str = "SRPBasePoints"
    SRP_ADJUSTMENT_DOLLAR: str = "SRPAdjustmentDollar"
    SRP_ADJUSTMENT_POINTS: str = "SRPAdjustmentPoints"
    EXTENSION_FEES_DOLLAR: str = "ExtensionFeesDollar"
    EXTENSION_FEES_POINTS: str = "ExtensionFeesPoints"
    NET_SALES_PRICE_DOLLAR: str = "NetSalesPriceDollar"
    NET_SALES_PRICE_POINTS: str = "NetSalesPricePoints"
    SECONDARY_GAIN_LOSS: str = "SecondaryGainLoss"
    PAIR_OFF_DOLLAR: str = "PairoffDollar"
    PAIR_OFF_POINTS: str = "PairoffPoints"
    NOTES: str = "Notes"
    LOCK_CONFIRM_ADJUSTMENT_DATA: str = "LockConfirmAdjustmentData"


@dataclass
class GetAdjustmentDataKeys:
    ADJUSTMENTS: str = "Adjustments"


@dataclass
class GetAdjustmentDataSectionKeys:
    SECTION_NAME: str = "SectionName"
    SECTION_VALUE: str = "SectionValue"


@dataclass
class GetAdjustmentDataSectionInfoKeys:
    DATA_NAME: str = "DataName"
    DATA_VALUE: str = "DataValue"


class GetAdjustmentDataName(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(GetAdjustmentDataSectionInfoKeys)]


class GetAdjustmentDataNames(BaseListResponse):
    _SUB_MODEL = GetAdjustmentDataName


class GetAdjustmentDataSection(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(GetAdjustmentDataSectionKeys)]
    _SUB_MODELS = [GetAdjustmentDataNames if _ is GetAdjustmentDataSectionKeys.SECTION_VALUE else None
                   for _ in _ADD_KEYS]


class GetAdjustmentDataSectionList(BaseListResponse):
    _SUB_MODEL = GetAdjustmentDataSection


class GetAdjustmentData(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(GetAdjustmentDataInfoKeys)]
    _SUB_MODELS = [GetAdjustmentDataSectionList if _ is GetAdjustmentDataInfoKeys.LOCK_CONFIRM_ADJUSTMENT_DATA else None
                   for _ in _ADD_KEYS]


class GetAdjustmentDataList(BaseListResponse):
    _SUB_MODEL = GetAdjustmentData
