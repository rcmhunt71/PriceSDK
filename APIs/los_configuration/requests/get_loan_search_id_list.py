from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class GetLoanSearchIdListRequestParams(BaseRequestModelKeys):
    QUERY_ID: str = "QueryId"
    OTHER_PARAMS: str = "OtherParams"
    FIELD_TO_SEARCH: str = "FieldToSearch"
    CONDITION_CODE: str = "ConditionCode"
    SEARCH_DATA: str = "SearchData"
    CHECK_SECURITY_PRIVILEGE: str = "CheckSecurityPrivilege"


class GetLoanSearchIdListRequest(SimpleRequestModel):
    def __init__(self, query_id, other_params, field_to_search, condition_code, search_data, check_security_privilege,
                 session_id, nonce, pretty_print):
        self.query_id = query_id
        self.other_params = other_params
        self.field_to_search = field_to_search
        self.condition_code = condition_code
        self.search_data = search_data
        self.check_security_privilege = check_security_privilege
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetLoanSearchIdListRequestParams.QUERY_ID] = self.query_id
        args[GetLoanSearchIdListRequestParams.OTHER_PARAMS] = self.other_params
        args[GetLoanSearchIdListRequestParams.FIELD_TO_SEARCH] = self.field_to_search
        args[GetLoanSearchIdListRequestParams.CONDITION_CODE] = self.condition_code
        args[GetLoanSearchIdListRequestParams.SEARCH_DATA] = self.search_data
        args[GetLoanSearchIdListRequestParams.CHECK_SECURITY_PRIVILEGE] = self.check_security_privilege
        return args
