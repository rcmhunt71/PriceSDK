from dataclasses import dataclass, fields

from base.responses.base_response import BaseResponse


# ===================
# SERVER_TIME
# ===================
@dataclass
class ServerTimeKeys:
    API_SERVER_TIME: str = "APIServerTime"


# ===================
# VERSION
# ===================
@dataclass
class VersionInfoKeys:
    MAJOR_VERSION: str = "MajorVersion"
    MINOR_VERSION: str = "MinorVersion"
    HOT_FIX: str = "Hotfix"
    BUILD: str = "Build"


@dataclass
class VersionKeys:
    PRICE_VERSION: str = "PRICEVersion"
    LOS_VERSION: str = "LOSVersion"


class Version(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(VersionInfoKeys)]
