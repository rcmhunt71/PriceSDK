from dataclasses import dataclass, fields

from base.responses.base_response import BaseListResponse
from base.responses.base_response import BaseResponse


@dataclass
class AssetInfoKeys:
    CUSTOMER_ID: str = 'CustomerID'
    ASSET_ID: str = 'AssetID'
    ASSET_NAME: str = 'AssetName'
    ASSET_TYPE: str = 'AssetType'
    MARKET_VALUE: str = 'MarketValue'
    FIX_DESCRIPTION: str = 'FixDescription'
    INSURANCE_FACE_VALUE: str = 'InsuranceFaceValue'
    VERIFY: str = 'Verify'
    VERIFY_DATE: str = 'VerifyDate'
    BOTH: str = 'Both'
    LIQUID: str = 'Liquid'
    RETIREMENT_FUND_DETAIL: str = 'RetirementFundDetail'


@dataclass
class AssetsKeys:
    ASSETS: str = 'Assets'


class Asset(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(AssetInfoKeys)]


class Assets(BaseListResponse):
    _SUB_MODEL = Asset
