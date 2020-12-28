from dataclasses import dataclass
from base.clients.base_client import BaseClient
from base.common.models.request import SimpleRequestModel
from base.common.response import CommonResponse

from APIs.dashboard.requests.add_dashboard import AddDashboardRequest
from APIs.dashboard.requests.add_widget import AddWidgetRequest
from APIs.dashboard.requests.delete_dashboard import DeleteDashboardRequest
from APIs.dashboard.requests.delete_widget import DeleteWidgetRequest
from APIs.dashboard.requests.get_db_column_info import GetDbColumnInfoRequest
from APIs.dashboard.requests.set_dashboard_permissions import SetDashboardPermissionsRequest
from APIs.dashboard.requests.set_widget_permissions import SetWidgetPermissionsRequest

from APIs.dashboard.responses.get_all_dashboards import GetAllDashboardsResponse
from APIs.dashboard.responses.get_all_widgets import GetAllWidgetsResponse
from APIs.dashboard.responses.get_db_column_info import GetDbColumnInfoResponse
from APIs.dashboard.responses.get_permitted_dashboards import GetPermittedDashboardsResponse


@dataclass
class ApiEndpoints:
    ADD_WIDGET: str = "add_widget"
    ADD_DASHBOARD: str = "add_dashboard"
    DELETE_DASHBOARD: str = "delete_dashboard"
    DELETE_WIDGET: str = "delete_widget"
    GET_ALL_DASHBOARDS: str = "get_all_dashboards"
    GET_ALL_WIDGETS: str = "get_all_widgets"
    GET_DB_COLUMN_INFO: str = "get_db_column_info"
    GET_PERMITTED_DASHBOARDS: str = "get_permitted_dashboards"
    SET_DASHBOARD_PERMISSIONS: str = "set_dashboard_permissions"
    SET_WIDGET_PERMISSIONS: str = "set_widget_permissions"


class DashboardClient(BaseClient):

    def add_widget(self, widget_code, widget_title, widget_html, is_vendor_maintained, is_public, cache_expiration,
                   cache_scope, session_id=None, nonce=None, pretty_print=False):
        request_model = AddWidgetRequest(widget_code=widget_code, widget_title=widget_title, widget_html=widget_html,
                                         is_vendor_maintained=is_vendor_maintained, is_public=is_public,
                                         cache_expiration=cache_expiration, cache_scope=cache_scope,
                                         session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
                                         pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.ADD_WIDGET, response_model=CommonResponse,
                         data=request_model.payload, params=request_model.as_params_dict)

    def delete_widget(self, widget_code, session_id=None, nonce=None, pretty_print=False):
        request_model = DeleteWidgetRequest(widget_code=widget_code, nonce=self._get_nonce(nonce),
                                            session_id=self._get_session_id(session_id), pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.DELETE_WIDGET, response_model=CommonResponse,
                         data=request_model.payload, params=request_model.as_params_dict)

    def add_dashboard(self, dashboard_code, dashboard_title, dashboard_html, is_vendor_maintained,
                      session_id=None, nonce=None, pretty_print=False):
        request_model = AddDashboardRequest(dashboard_code=dashboard_code, dashboard_title=dashboard_title,
                                            dashboard_html=dashboard_html, is_vendor_maintained=is_vendor_maintained,
                                            session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce),
                                            pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.ADD_DASHBOARD, response_model=CommonResponse,
                         data=request_model.payload, params=request_model.as_params_dict)

    def delete_dashboard(self, dashboard_code, session_id=None, nonce=None, pretty_print=False):
        request_model = DeleteDashboardRequest(dashboard_code=dashboard_code, nonce=self._get_nonce(nonce),
                                               session_id=self._get_session_id(session_id), pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.DELETE_DASHBOARD, response_model=CommonResponse,
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

    def get_db_column_info(self, table_name, session_id=None, nonce=None, pretty_print=False):
        request_model = GetDbColumnInfoRequest(table_name=table_name, session_id=self._get_session_id(session_id),
                                               nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_DB_COLUMN_INFO, response_model=GetDbColumnInfoResponse,
                        params=request_model.as_params_dict)

    def get_permitted_dashboards(self, session_id=None, nonce=None, pretty_print=False):
        request_model = SimpleRequestModel(session_id=self._get_session_id(session_id),
                                           nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_PERMITTED_DASHBOARDS,
                        response_model=GetPermittedDashboardsResponse, params=request_model.as_params_dict)

    def set_dashboard_permissions(self, dashboard_code, security_levels, session_id=None, nonce=None,
                                  pretty_print=False):
        request_model = SetDashboardPermissionsRequest(dashboard_code=dashboard_code, security_levels=security_levels,
                                                       session_id=self._get_session_id(session_id),
                                                       nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.SET_DASHBOARD_PERMISSIONS, response_model=CommonResponse,
                         data=request_model.payload, params=request_model.as_params_dict)

    def set_widget_permissions(self, widget_code, security_levels, session_id=None, nonce=None, pretty_print=False):
        request_model = SetWidgetPermissionsRequest(widget_code=widget_code, security_levels=security_levels,
                                                    session_id=self._get_session_id(session_id),
                                                    nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.SET_WIDGET_PERMISSIONS, response_model=CommonResponse,
                         data=request_model.payload, params=request_model.as_params_dict)
