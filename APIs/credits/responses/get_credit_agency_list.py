from base.common.response import CommonResponse
from APIs.credits.models.get_credit_agency_list import GetCreditAgencyListKeys, GetCreditAgencyList


class GetCreditAgencyListResponse(CommonResponse):
    _ADD_KEYS = [GetCreditAgencyListKeys.DATA]
    _SUB_MODELS = [GetCreditAgencyList]
