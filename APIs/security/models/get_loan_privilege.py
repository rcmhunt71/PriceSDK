from dataclasses import dataclass, fields

from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class GetLoanPrivilegeInfoKeys:
    FNM: str = "FNM"
    FM: str = "FM"
    FM_LPI_S2S: str = "FMLPIS2S"
    FM_LPI_W2W: str = "FMLPIW2W"
    EDIT_CONTACT_ESCROW: str = "EditContactEscrow"
    EDIT_CONTACT_TITLE: str = "EditContactTitle"


@dataclass
class GetLoanPrivilegeKeys:
    DATA: str = "Data"


class GetLoanPrivilege(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(GetLoanPrivilegeInfoKeys)]


class GetLoanPrivilegeList(BaseListResponse):
    _SUB_MODEL = GetLoanPrivilege
