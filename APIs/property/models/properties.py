from dataclasses import dataclass, fields
from base.responses.base_response import BaseListResponse, BaseResponse


@dataclass
class PropertyKeys:
    CUSTOMERID: str = 'CustomerID'
    PROPERTYID: str = 'PropertyID'
    APPRAISEDVALUE: str = 'AppraisedValue'
    APPRAISEDVALUEDATE: str = 'AppraisedValueDate'
    ADDRESS: str = 'Address'
    DISTRICT: str = 'District'
    CITY: str = 'City'
    STATE: str = 'State'
    COUNTY: str = 'County'
    ZIP: str = 'Zip'
    SUITE: str = 'Suite'
    OCCUPANCY: str = 'Occupancy'
    PROPERTYTYPE: str = 'PropertyType'
    PROPERTYCLASSIFICATION: str = 'PropertyClassification'
    PUDTYPE: str = 'PUDType'
    YEARBUILT: str = 'YearBuilt'
    UNITS: str = 'Units'
    TENURE: str = 'Tenure'
    LEASEEXPIREDATE: str = 'LeaseExpireDate'
    LEASERENEGOTIATEDATE: str = 'LeaseRenegotiateDate'
    ORIGINALCOST: str = 'OriginalCost'
    SALESPRICE: str = 'SalesPrice'
    HAZARDINSURANCE: str = 'HazardInsurance'
    PROPERTYTAX: str = 'PropertyTax'
    MORTGAGEINSURANCE: str = 'MortgageInsurance'
    ASSOCIATIONDUES: str = 'AssociationDues'
    OTHERCOSTS: str = 'OtherCosts'
    TITLEHELDAS: str = 'TitleHeldAs'
    OWNRENT: str = 'OwnRent'
    OWNRENTYEARS: str = 'OwnRentYears'
    DATEACQUIRED: str = 'DateAcquired'
    NETRENTALINCOME: str = 'NetRentalIncome'
    PAYMENT: str = 'Payment'
    PURPOSEOFREFINANCE: str = 'PurposeOfRefinance'
    MARKETVALUE: str = 'MarketValue'
    FLOODINSURANCE: str = 'FloodInsurance'
    LEASERENT: str = 'LeaseRent'
    RENT: str = 'Rent'
    CONTINUEDRENTAL: str = 'ContinuedRental'
    RELOCATION: str = 'Relocation'


@dataclass
class PropertiesKeys:
    PROPERTIES: str = 'Properties'


class Property(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(PropertyKeys)]


class Properties(BaseListResponse):
    _SUB_MODEL = Property
