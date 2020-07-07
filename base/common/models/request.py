import os
from abc import ABC, abstractmethod
from dataclasses import dataclass, fields
import json

@dataclass
class DataPayload:
    pass


@dataclass
class BaseRequestModelKeys:
    SESSION_ID: str = "SessionID"
    NONCE: str = "Nonce"
    PRETTY_PRINT: bool = "PrettyPrint"


class BaseRequestModel(ABC):
    def __init__(self, session_id, nonce, payload=None, pretty_print=False):
        self.session_id = session_id
        self.nonce = nonce
        self.pretty_print = pretty_print
        self.as_params_dict = self.to_params()
        self.as_json = self.to_json()
        self.payload = payload if payload is not None else self.build_payload()

    def to_params(self):
        args = {
            BaseRequestModelKeys.SESSION_ID: self.session_id,
            BaseRequestModelKeys.NONCE: self.nonce,
        }
        if self.pretty_print:
            args[BaseRequestModelKeys.PRETTY_PRINT] = self.pretty_print
        return args

    def to_json(self):
        return json.dumps(self.to_params())

    @abstractmethod
    def build_payload(self):
        pass


class KwargsRequestModel(BaseRequestModel):
    data_payload = DataPayload

    def __init__(self, session_id, nonce, payload=None, pretty_print=False, **kwargs):
        # Kwargs are key/value pairs where a key can be a lower-case SetLoanDataPayload attribute
        # e.g. -  SUB_FINANCE_HELOC_AMOUNT -->> sub_finance_heloc_amount

        # Dynamically set all attributes based kwargs that match a DataPayload attribute
        valid_keys = [elem.name for elem in fields(self.data_payload)]
        self.attr_list = []

        # Iterate through the kwargs
        for attr in kwargs.keys():

            # If kwargs.UPPER() matches a SetLoanDataPayload attribute, create a model attribute and store the value.
            # Also record the name of the attribute for more efficient payload generation
            if attr.upper() in valid_keys or os.environ.get('TEST_ENV'):
                setattr(self, attr.lower(), kwargs[attr])
                self.attr_list.append(attr.lower())

        super().__init__(session_id=session_id, nonce=nonce, payload=payload, pretty_print=pretty_print)

    @abstractmethod
    def build_payload(self):
        pass