import datetime
import hashlib
import os
from enum import Enum
import requests
import json

from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel

from base.common.response import CommonResponse, CommonResponseKeys

from logger.logging import Logger

log = Logger()


class Methods(Enum):
    GET = 'get'
    PUT = 'put'
    POST = 'post'
    DELETE = 'delete'
    HEAD = 'head'
    OPTIONS = 'options'


class ApiEndpoints:
    CREATE_SESSION = "CREATE_SESSION"
    END_SESSION = "END_SESSION"


class BaseClient:
    headers = {'Content-Type': 'application/x-www-form-urlencoded',
               'cache-control': 'no-cache'}

    def __init__(self, base_url=None, database=None, port=None, headers=None, client=None, payload=None):

        # If provided an existing client, use that info...
        if client is not None and isinstance(client, BaseClient):
            self.client = client
            self.base_url = client.base_url
            self.url = client.url
            self.headers = client.headers
            self.port = client.port
            self.database = client.database
            self.nonce = client.nonce
            self.session_id = client.session_id
            # For writing data to test_output/file
            self.response_raw = client.response_raw
            self.request_url = client.request_url
            self.request_body = client.request_body

        # Otherwise, instantiate a client.
        else:
            self.base_url = base_url
            # self.headers = headers or {}
            self.headers = headers or self.headers
            self.payload = payload
            self.port = port
            self.database = database
            self.nonce = None
            self.session_id = None
            # For writing data to test_output/file
            self.response_raw = None
            self.request_url = None
            self.request_body = None

            port_info = '' if port is None else f":{port}"
            self.url = f"{self.base_url}{port_info}/{database}"

            if not self.url.lower().startswith("http"):
                self.url = f"https://{self.url}"

        self.test_response_data = None

    def authenticate(self, username, password, app_id, app_password):
        price_pepper = os.environ.get('PRICE_PEPPER')
        if not price_pepper:
            raise EnvironmentError('The PRICE_PEPPER environment variable must be configured')

        # Calculate AppSecret
        app_secret = price_pepper + app_id + app_password
        app_secret = hashlib.sha256(app_secret.encode())
        hashed_app_secret = app_secret.hexdigest().upper()
        # Add GMT / UTC date-time to the front and hash again
        hashed_app_secret = datetime.datetime.utcnow().strftime('%Y%m%d%H%M') + hashed_app_secret
        hashed_app_secret = hashlib.sha256(hashed_app_secret.encode())
        hashed_app_secret = hashed_app_secret.hexdigest().upper()

        # Create a session in PRICE
        params = {"AppID": app_id,
                  "AppSecret": hashed_app_secret,
                  "LoginName": username,
                  "APIVersion": "0.0.0"}
        pay_load = {"Password": password}

        # Post the request
        response_model = self._make_call(ApiEndpoints.CREATE_SESSION, CommonResponse, data=pay_load,
                                         method=Methods.POST, headers=self.headers, params=params)
        self.session_id = response_model.raw.get(BaseRequestModelKeys.SESSION_ID)
        return response_model

    def end_session(self, session_id=None, nonce=None):
        request_model = SimpleRequestModel(session_id=self._get_session_id(session_id), nonce=self._get_nonce(nonce))
        return self._make_call(ApiEndpoints.END_SESSION, CommonResponse, method=Methods.POST,
                               params=request_model.as_params_dict)

    def insert_test_response_data(self, data):
        self.test_response_data = data

    def _get_nonce(self, nonce):
        return nonce or self.nonce or self.client.nonce

    def _get_session_id(self, session_id):
        return session_id or self.session_id or self.client.session_id

    def get(self, resource_endpoint, response_model, headers=None, params=None):
        return self._make_call(resource_endpoint, response_model,
                               method=Methods.GET, headers=headers, params=params)

    def delete(self, resource_endpoint, response_model, headers=None, params=None):
        return self._make_call(resource_endpoint, response_model,
                               method=Methods.DELETE, headers=headers, params=params)

    def post(self, resource_endpoint, response_model, data, headers=None, params=None, binary_data=None):
        if binary_data is not None:
            data = binary_data
        return self._make_call(resource_endpoint, response_model, data=data,
                               method=Methods.POST, headers=headers, params=params)

    def put(self, resource_endpoint, data, response_model, headers=None, params=None):
        return self._make_call(resource_endpoint, response_model, data=data,
                               method=Methods.PUT, headers=headers, params=params)

    def _make_call(self, resource_endpoint, response_model_class, method, data=None, headers=None, params=None):
        params = params or {}
        data = data or {}
        headers = headers or self.headers
        url = f"{self.url}/{resource_endpoint}"
        args = {'url': url, 'params': params, 'headers': headers}

        log.debug(f"URL: {method.value.upper()} {self.url}")
        log.debug(f"PARAMS: {params}")
        log.debug(f"HEADERS: {headers}")

        if method in [Methods.POST, Methods.PUT]:
            args['data'] = data
            self.payload = data

        full_url_request = f"{method.value.upper()} {url}"
        if params:
            full_url_request += f"?{params}"
        log.debug(f"Making call to: {full_url_request}")
        response = getattr(requests, method.value.lower())(**args)

        # TEST: Insert test response data in call response
        response_type = "RESPONSE"
        if self.test_response_data is not None:
            response.content = self.test_response_data
            response.text = self.test_response_data
            response_type = "TEST RESPONSE"
        log.debug(f"{response_type}: {response.content}")

        response_content_type = response.headers._store['content-type'][1].partition('/')

        if response.status_code != 200:
            response_content = {
                "Successful": False,
                "ErrorMessage": response.text,
                "Nonce": self._get_nonce(None)
            }
        # For API calls returning binary file
        elif response_content_type[2] in ['csv', 'pdf', 'xml', 'octet-stream', 'tiff', 'jpeg']:
            response_content = {
                "Successful": True,
                "Tags": response_content_type[2],
                "raw_response": response.content,
                "Nonce": self._get_nonce(None)
            }
        else:
            response_content = response.content if type(response.content) is dict else json.loads(response.content)

        if resource_endpoint.lower() not in [ApiEndpoints.CREATE_SESSION.lower(), ApiEndpoints.END_SESSION.lower()]:
            if getattr(self, 'client', False):
                self.client.response_raw = response_content
                self.client.request_url = f"{response.request.method} {response.request.url}"
                self.client.request_body = response.request.body
            self.response_raw = response_content
            self.request_url = f"{response.request.method} {response.request.url}"
            self.request_body = response.request.body

        response_model = response_model_class(**response_content)
        log.debug(f"Response Model: {type(response_model)}")

        response_model.response = response
        response_model.status = response.status_code
        response_model.content = response_content

        self.nonce = getattr(response_model, CommonResponseKeys.NONCE)
        if getattr(self, 'client', None):
            if self.nonce:
                self.client.nonce = self.nonce

        return response_model
