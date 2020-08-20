from base.clients.base_client import BaseClient

from APIs.loans.client import LoanClient
from APIs.assets.client import AssetsClient

class Client(BaseClient):
    def __init__(self, base_url, database, port=None, headers=None):
        super().__init__(base_url=base_url, database=database, port=port, headers=headers)
        self.loan = LoanClient(client=self)
        self.assets = AssetsClient(client = self)