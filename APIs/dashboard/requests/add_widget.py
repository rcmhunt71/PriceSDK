from dataclasses import dataclass
from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class AddWidgetRequestParams(BaseRequestModelKeys):
    WIDGET_HTML: str = "WidgetHTML"
    WIDGET_CODE: str = "WidgetCode"
    WIDGET_TITLE: str = "WidgetTitle"
    IS_VENDOR_MAINTAINED: str = "IsVendorMaintained"
    IS_PUBLIC: str = "IsPublic"
    CACHE_EXPIRATION: str = "CacheExpiration"
    CACHE_SCOPE: str = "CacheScope"


class AddWidgetRequest(SimpleRequestModel):
    def __init__(self, widget_html, widget_code, widget_title, is_vendor_maintained, is_public, cache_expiration,
                 cache_scope, session_id, nonce, pretty_print):
        self.widget_html = widget_html
        self.widget_code = widget_code
        self.widget_title = widget_title
        self.is_vendor_maintained = is_vendor_maintained
        self.is_public = is_public
        self.cache_expiration = cache_expiration
        self.cache_scope = cache_scope
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[AddWidgetRequestParams.WIDGET_HTML] = self.widget_html
        args[AddWidgetRequestParams.WIDGET_CODE] = self.widget_code
        args[AddWidgetRequestParams.WIDGET_TITLE] = self.widget_title
        args[AddWidgetRequestParams.IS_VENDOR_MAINTAINED] = self.is_vendor_maintained
        args[AddWidgetRequestParams.IS_PUBLIC] = self.is_public
        args[AddWidgetRequestParams.CACHE_EXPIRATION] = self.cache_expiration
        args[AddWidgetRequestParams.CACHE_SCOPE] = self.cache_scope
        return args
