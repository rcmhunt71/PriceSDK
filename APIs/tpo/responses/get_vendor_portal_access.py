from dataclasses import dataclass
from base.common.response import CommonResponse


@dataclass
class GetVendorPortalAccessKeys:
    VENDOR_PORTAL_ACCESS: str = "VendorPortalAccess"


class GetVendorPortalAccessResponse(CommonResponse):
    _ADD_KEYS = [GetVendorPortalAccessKeys.VENDOR_PORTAL_ACCESS]
    _SUB_MODELS = [None]
