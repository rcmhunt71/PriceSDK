from APIs.companies.client import CompaniesClient
from APIs.extra_and_virtual_data.client import ExtraDataClient, VirtualDataClient
from APIs.passwords.client import PasswordsClient
from APIs.persons.employees.client import EmployeesClient
from APIs.persons.client import PersonsClient
from APIs.persons.contacts.client import ContactsClient
from APIs.credits.client import CreditsClient
from APIs.data_checks.client import DataChecksClient
from APIs.dates.client import DatesClient
from APIs.deposits.client import DepositsClient
from APIs.fees.client import FeesClient
from APIs.persons.borrowers.client import BorrowersClient
from APIs.price_and_lock.client import PriceAndLockClient
from base.clients.base_client import BaseClient
from APIs.loans.client import LoanClient
from APIs.assets.client import AssetsClient
from APIs.properties.client import PropertiesClient
from APIs.liabilities.client import LiabilitiesClient
from APIs.incomes.client import IncomesClient
from APIs.security.client import SecurityClient


class Client(BaseClient):
    def __init__(self, base_url, database, port=None, headers=None):
        super().__init__(base_url=base_url, database=database, port=port, headers=headers)
        self.assets = AssetsClient(client=self)
        self.borrowers = BorrowersClient(client=self)
        self.companies = CompaniesClient(client=self)
        self.contacts = ContactsClient(client=self)
        self.credits = CreditsClient(client=self)
        self.data_checks = DataChecksClient(client=self)
        self.dates = DatesClient(client=self)
        self.deposits = DepositsClient(client=self)
        self.employees = EmployeesClient(client=self)
        self.extra_data = ExtraDataClient(client=self)
        self.fees = FeesClient(client=self)
        self.incomes = IncomesClient(client=self)
        self.liabilities = LiabilitiesClient(client=self)
        self.loan = LoanClient(client=self)
        self.passwords = PasswordsClient(client=self)
        self.persons = PersonsClient(client=self)
        self.price_and_lock = PriceAndLockClient(client=self)
        self.properties = PropertiesClient(client=self)
        self.security = SecurityClient(client=self)
        self.virtual_data = VirtualDataClient(client=self)
