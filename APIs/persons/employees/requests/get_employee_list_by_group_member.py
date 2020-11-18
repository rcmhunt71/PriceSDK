from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class GetEmployeeListByGroupMemberRequestParams(BaseRequestModelKeys):
    MEMBER_IDS: str = "MemberIDs"
    GROUP_IDS: str = "GroupIDs"


class GetEmployeeListByGroupMemberRequest(SimpleRequestModel):
    def __init__(self, member_ids, group_ids, session_id, nonce, pretty_print):
        self.member_ids = member_ids
        self.group_ids = group_ids
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetEmployeeListByGroupMemberRequestParams.MEMBER_IDS] = self.member_ids
        args[GetEmployeeListByGroupMemberRequestParams.GROUP_IDS] = self.group_ids
        return args
