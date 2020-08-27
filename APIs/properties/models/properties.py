from dataclasses import dataclass, fields
from base.responses.base_response import BaseListResponse, BaseResponse


@dataclass
class PropertyKeys:
    CUSTOMER_ID: str = 'CustomerID'
    PROPERTY_ID: str = 'PropertyID'
    APPRAISED_VALUE: str = 'AppraisedValue'
    APPRAISED_VALUE_DATE: str = 'AppraisedValueDate'
    ADDRESS: str = 'Address'
    DISTRICT: str = 'District'
    CITY: str = 'City'
    STATE: str = 'State'
    COUNTY: str = 'County'
    ZIP: str = 'Zip'
    SUITE: str = 'Suite'
    OCCUPANCY: str = 'Occupancy'
    PROPERTY_TYPE: str = 'PropertyType'
    PROPERTY_CLASSIFICATION: str = 'PropertyClassification'
    PUD_TYPE: str = 'PUDType'
    YEAR_BUILT: str = 'YearBuilt'
    UNITS: str = 'Units'
    TENURE: str = 'Tenure'
    LEASE_EXPIRE_DATE: str = 'LeaseExpireDate'
    LEASE_RENEGOTIATE_DATE: str = 'LeaseRenegotiateDate'
    ORIGINAL_COST: str = 'OriginalCost'
    SALES_PRICE: str = 'SalesPrice'
    HAZARD_INSURANCE: str = 'HazardInsurance'
    PROPERTY_TAX: str = 'PropertyTax'
    MORTGAGE_INSURANCE: str = 'MortgageInsurance'
    ASSOCIATION_DUES: str = 'AssociationDues'
    OTHER_COSTS: str = 'OtherCosts'
    TITLE_HELD_AS: str = 'TitleHeldAs'
    OWN_RENT: str = 'OwnRent'
    OWN_RENT_YEARS: str = 'OwnRentYears'
    DATE_ACQUIRED: str = 'DateAcquired'
    NET_RENTAL_INCOME: str = 'NetRentalIncome'
    PAYMENT: str = 'Payment'
    PURPOSE_OF_REFINANCE: str = 'PurposeOfRefinance'
    MARKET_VALUE: str = 'MarketValue'
    FLOOD_INSURANCE: str = 'FloodInsurance'
    LEASE_RENT: str = 'LeaseRent'
    RENT: str = 'Rent'
    CONTINUED_RENTAL: str = 'ContinuedRental'
    RELOCATION: str = 'Relocation'


@dataclass
class PropertiesKeys:
    PROPERTIES: str = 'Properties'


class Property(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(PropertyKeys)]


class Properties(BaseListResponse):
    _SUB_MODEL = Property
