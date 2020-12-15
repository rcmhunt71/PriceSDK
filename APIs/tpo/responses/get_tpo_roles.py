from APIs.tpo.models.tpo_roles import TPORolesKeys, TPORolesList
from base.common.response import CommonResponse


class GetTPORolesResponse(CommonResponse):
    _ADD_KEYS = [TPORolesKeys.TPO_ROLES]
    _SUB_MODELS = [TPORolesList]
