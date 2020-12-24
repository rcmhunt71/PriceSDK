from dataclasses import dataclass
from base.clients.base_client import BaseClient
from base.common.models.request import SimpleRequestModel
from base.common.response import CommonResponse

from APIs.dashboard.requests.add_widget import AddWidgetRequest

from APIs.dashboard.responses.get_all_dashboards import GetAllDashboardsResponse
from APIs.dashboard.responses.get_all_widgets import GetAllWidgetsResponse


@dataclass
class ApiEndpoints:
    ADD_WIDGET: str = "add_widget"
    GET_ALL_DASHBOARDS: str = "get_all_dashboards"
    GET_ALL_WIDGETS: str = "get_all_widgets"


class DashboardClient(BaseClient):

    def add_widget(self, widget_html, widget_code, widget_title, is_vendor_maintained, is_public, cache_expiration,
                   cache_scope, session_id=None, nonce=None, pretty_print=False):
        request_model = AddWidgetRequest(widget_html=widget_html, widget_code=widget_code, widget_title=widget_title,
                                         is_vendor_maintained=is_vendor_maintained, is_public=is_public,
                                         cache_expiration=cache_expiration, cache_scope=cache_scope,
                                         session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
                                         pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.ADD_WIDGET, response_model=CommonResponse,
                         data=request_model.payload, params=request_model.as_params_dict)

    def get_all_dashboards(self, session_id=None, nonce=None, pretty_print=False):
        request_model = SimpleRequestModel(session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
                                           pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_ALL_DASHBOARDS, response_model=GetAllDashboardsResponse,
                        params=request_model.as_params_dict)

    def get_all_widgets(self, session_id=None, nonce=None, pretty_print=False):
        request_model = SimpleRequestModel(session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
                                           pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_ALL_WIDGETS, response_model=GetAllWidgetsResponse,
                        params=request_model.as_params_dict)
