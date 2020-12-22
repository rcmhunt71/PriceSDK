from dataclasses import dataclass

from base.clients.base_client import BaseClient
from base.common.models.request import LoanNumberIdRequestModel
from base.common.response import CommonResponse

from APIs.deposits.requests.add_deposit import AddDepositRequest
from APIs.deposits.requests.clear_deposit_account import ClearDepositAccountRequest
from APIs.deposits.requests.set_deposit_accounts import SetDepositAccountsRequest

from APIs.deposits.responses.add_deposit import AddDepositResponse
from APIs.deposits.responses.get_deposit_accounts import GetDepositAccountsResponse
from APIs.deposits.responses.get_deposits import GetDepositsResponse


@dataclass
class ApiEndpoints:
    GET_DEPOSIT_ACCOUNTS: str = "get_deposit_accounts"
    GET_DEPOSITS: str = "get_deposits"
    ADD_DEPOSIT: str = "add_deposit"
    CLEAR_DEPOSIT_ACCOUNT: str = "clear_deposit_account"
    SET_DEPOSIT_ACCOUNTS: str = "set_deposit_accounts"


class DepositsClient(BaseClient):
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"
    json_headers = {
        CONTENT_TYPE: APPLICATION_JSON
    }

    def get_deposit_accounts(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
                                                 session_id=self._get_session_id(session_id),
                                                 nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_DEPOSIT_ACCOUNTS, response_model=GetDepositAccountsResponse,
                        params=request_model.as_params_dict)

    def get_deposits(self, loan_number_id, session_id=None, nonce=None, pretty_print=False):
        request_model = LoanNumberIdRequestModel(loan_number_id=loan_number_id,
                                                 session_id=self._get_session_id(session_id),
                                                 nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.GET_DEPOSITS, response_model=GetDepositsResponse,
                        params=request_model.as_params_dict)

    def add_deposit(self, loan_number_id, customer_id, session_id=None, nonce=None, pretty_print=False):
        request_model = AddDepositRequest(loan_number_id=loan_number_id, customer_id=customer_id,
                                          session_id=self._get_session_id(session_id),
                                          nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.ADD_DEPOSIT, response_model=AddDepositResponse,
                         params=request_model.as_params_dict, data=request_model.payload)

    def clear_deposit_account(self, loan_number_id, customer_id, deposit_id, deposit_account_id, session_id=None,
                              nonce=None, pretty_print=False):
        request_model = ClearDepositAccountRequest(loan_number_id=loan_number_id, customer_id=customer_id,
                                                   deposit_id=deposit_id, deposit_account_id=deposit_account_id,
                                                   session_id=self._get_session_id(session_id),
                                                   nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.post(resource_endpoint=ApiEndpoints.CLEAR_DEPOSIT_ACCOUNT, response_model=CommonResponse,
                         params=request_model.as_params_dict, data=request_model.payload)

    def set_deposit_accounts(self, loan_number_id, payload_dict=None, session_id=None, nonce=None,
                             pretty_print=False, **kwargs):
        request_model = SetDepositAccountsRequest(loan_number_id=loan_number_id, payload_dict=payload_dict,
                                                  session_id=self._get_session_id(session_id),
                                                  nonce=self._get_nonce(nonce),
                                                  pretty_print=pretty_print, **kwargs)

        return self.post(resource_endpoint=ApiEndpoints.SET_DEPOSIT_ACCOUNTS, response_model=CommonResponse,
                         params=request_model.as_params_dict, data=request_model.as_json, headers=self.json_headers)
