from APIs.dates.client import DatesClient
from APIs.deposits.client import DepositsClient
from base.clients.base_client import BaseClient
from APIs.loans.client import LoanClient
from APIs.assets.client import AssetsClient
from APIs.properties.client import PropertiesClient
from APIs.liabilities.client import LiabilitiesClient
from APIs.incomes.client import IncomesClient


class Client(BaseClient):
    def __init__(self, base_url, database, port=None, headers=None):
        super().__init__(base_url=base_url, database=database, port=port, headers=headers)
        self.assets = AssetsClient(client=self)
        self.dates = DatesClient(client=self)
        self.deposits = DepositsClient(client=self)
        self.incomes = IncomesClient(client=self)
        self.liabilities = LiabilitiesClient(client=self)
        self.loan = LoanClient(client=self)
        self.properties = PropertiesClient(client=self)
