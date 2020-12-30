from base.common.response import CommonResponse
from APIs.interfaces.models.auto_import_pca_do_du_download import AutoImportDownloadKeys


class AutoImportPcadoDownloadResponse(CommonResponse):
    _ADD_KEYS = [AutoImportDownloadKeys.IMPORTED]
    _SUB_MODELS = [None]
